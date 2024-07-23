#!/bin/bash
# moves the posts into yearly directories

script_dir=$(dirname "$0")
SOURCE_DIR="$script_dir/../docs/posts"
TARGET_DIR="$script_dir/../docs/posts"

mkdir -p "$TARGET_DIR"

for file in "$SOURCE_DIR"/*; do
    if [ -f "$file" ]; then
        year=$(basename "$file" | cut -d'-' -f1)
        mkdir -p "$TARGET_DIR/$year"
        mv "$file" "$TARGET_DIR/$year/"
        echo "Moved $(basename "$file") to $TARGET_DIR/$year/"
    fi
done

echo "organized into yearly dirs.."