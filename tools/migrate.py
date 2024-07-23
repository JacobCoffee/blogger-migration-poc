"""Ingest an XML export of a Blogger blog and convert it to RST files for ablog.

Modified from https://daniel.feldroy.com/posts/2022-02-blogger-to-markdown-script

Usage:
    python tools/migrate.py export.xml docs/posts/ --tag legacy-blogger
"""

import argparse
import datetime
import re
from pathlib import Path

import feedparser
import html2text


def parse_date(date_string):
    date_string = re.sub(r"\.\d+", "", date_string)
    date_string = re.sub(r"(-\d{2}):(\d{2})$", r"\1\2", date_string)
    return datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S%z").strftime(
        "%Y-%m-%d"
    )


def convert_html_to_rst(html_content):
    h = html2text.HTML2Text()
    h.ignore_links = False
    markdown = h.handle(html_content)
    header_chars = ["=", "-", "~", "^", '"']

    lines = markdown.split("\n")
    for i, line in enumerate(lines):
        if header_match := re.match(r"^(#+)\s*(.*)", line):
            level = len(header_match[1]) - 1
            title = header_match[2]
            underline_char = header_chars[min(level, len(header_chars) - 1)]
            lines[i] = f"{title}\n{underline_char * len(title)}"

    rst = "\n".join(lines)
    rst = rst.replace("**", "*")

    return re.sub(r"\[([^]]+)]\(([^)]+)\)", r"`\1 <\2>`_", rst)


def filter_entry(entry):
    if "tag:blogger.com" in entry.link:
        return False
    if "comments" in entry.get("href", ""):
        return False
    return "#settings" not in entry.category


def process_entries(data):
    posts = {}
    for entry in data.entries:
        if not filter_entry(entry):
            continue

        if "#comment" in entry.category:
            posts[entry["thr_in-reply-to"]["href"]].comments.append(entry)
        else:
            entry["comments"] = []
            posts[entry.link] = entry
    return posts


def generate_filename(key, feed_link):
    filename = key.replace(".html", ".rst").replace(feed_link, "")
    link = feed_link.replace("http", "https")
    filename = filename.replace(link, "").replace("/", "-")
    return filename


def write_rst_file(file_path, post, date, tags, show_original):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f".. post:: {date}\n")
        f.write(f"   :tags: {', '.join(tags)}\n")
        f.write("   :author: Python Software Foundation\n")
        f.write("   :category: Legacy\n")
        f.write("   :location: World\n")
        f.write("   :language: en\n\n")

        f.write(f"{post['title']}\n")
        f.write("=" * len(post["title"]) + "\n\n")

        if show_original:
            f.write(
                f"*This was originally posted on blogger* `here <{post['link']}>`_.\n\n"
            )

        rst_content = convert_html_to_rst(post["summary"])
        f.write(rst_content)


def main(input_file, output_dir, tag="legacy-blogger", show_original=True):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Parsing data from '{input_file}'")
    raw_text = Path(input_file).read_text(encoding="utf-8")
    data = feedparser.parse(raw_text)

    posts = process_entries(data)

    print(f"Writing {len(posts)} blogger posts to RST files")
    for key, post in posts.items():
        filename = generate_filename(key, data["feed"]["link"])
        if not filename.strip() or filename.startswith("p-"):
            continue

        tags = [
            x["term"]
            for x in post.tags
            if x["term"] != "https://schemas.google.com/blogger/2008/kind#post"
        ]
        tags.append(tag)
        tags = [x for x in tags if not x.startswith("https://schemas.google.com")]

        date = parse_date(post["published"])

        write_rst_file(output_dir / filename, post, date, tags, show_original)
        print(f"Processed: {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert Blogger XML export to RST files for ablog."
    )
    parser.add_argument(
        "input_file", type=str, help="Path to the input XML file", nargs='?', default="export.xml"
    )
    parser.add_argument(
        "output_dir",
        type=str,
        help="Path to the output directory",
        nargs='?',
        default="docs/posts/",
    )
    parser.add_argument(
        "--tag", type=str, default="legacy-blogger", help="Tag to add to all posts"
    )
    parser.add_argument(
        "--no-show-original",
        action="store_false",
        dest="show_original",
        help="Don't include link to original post",
    )

    args = parser.parse_args()

    main(args.input_file, args.output_dir, args.tag, args.show_original)
