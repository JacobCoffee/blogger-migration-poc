"""
Unused now, but would take the pandoc-converted rst files and add some more metadata to them.
"""

import os
import re


def format_title(filename):
    # Remove date and file extension
    title = re.sub(r"^\d{4}-\d{2}-", "", filename[:-4])
    # Replace hyphens with spaces and capitalize words
    return " ".join(word.capitalize() for word in title.split("-"))


def get_date_from_filename(filename):
    if match := re.match(r"(\d{4}-\d{2})", filename):
        return match[1]
    return "Unknown"


def process_file(input_path, output_path):
    with open(input_path, "r") as file:
        content = file.read()

    filename = os.path.basename(input_path)
    title = format_title(filename)
    date = get_date_from_filename(filename)

    header = f""":blogpost: true
:date: {date or 'Unknown'}
:author: Python Software Foundation
:location: World
:category: Manual
:language: English

{'=' * len(title)}
{title}
{'=' * len(title)}

"""

    with open(output_path, "w") as file:
        file.write(header + content)


def main():
    print("Sphinxifying blog posts...")
    input_dir = "docs/posts_unprocessed"
    output_dir = "docs/posts"

    if not os.path.exists(output_dir):
        print(f"Creating output directory: {output_dir}")
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".rst"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            process_file(input_path, output_path)
            print(f"Processed: {filename}")

    # os.system(f"rm -r {input_dir}")
    print("Done!")


if __name__ == "__main__":
    main()
