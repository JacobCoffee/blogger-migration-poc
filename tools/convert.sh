# unused now, originally we used the original script into md, then this into rst, then another to massage the rst
# to not suck
mkdir -p out docs/posts_unprocessed

for file in out/*.md; do
    filename=$(basename "$file" .md)
    echo "Converting $file to docs/posts_unprocessed/${filename}.rst"
    pandoc --from=markdown --to=rst --output="docs/posts_unprocessed/${filename}.rst" "$file"
done

rm -f out/*.md
echo "Conversion complete - check above warnings and re-run 'make migrate' if necessary"
