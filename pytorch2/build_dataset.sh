#!/bin/bash

echo "Script started"

TARGET=20000
BASE_DIR="dataset"
mkdir -p $BASE_DIR/{sfw,borderline,nsfw}

# File extension filter: jpg, jpeg, png
EXT_FILTER="extension in ['jpg', 'jpeg', 'png']"

# Check gallery-dl installed
if ! command -v gallery-dl &> /dev/null; then
    echo "gallery-dl not found! Run: pip install gallery-dl"
    exit 1
fi

# 1. Borderline from Danbooru (rating:safe)
echo "[1/3] Downloading borderline (Danbooru: rating:safe)"
gallery-dl "https://danbooru.donmai.us/posts?tags=rating:sensitive" \
    -d $BASE_DIR/borderline \
    --download-archive borderline_archive.txt \
    --range "1-$TARGET" \
    --filter "$EXT_FILTER"

echo "[2/3] Downloading NSFW (Danbooru: rating:explicit)"
gallery-dl "https://danbooru.donmai.us/posts?tags=rating:explicit" \
    -d $BASE_DIR/nsfw \
    --download-archive nsfw_archive.txt \
    --range "1-$TARGET" \
    --filter "$EXT_FILTER"

# 3. SFW from 4Chan (cleaner than Konachan)
echo "[3/3] Downloading SFW (4Chan: rating:safe)"
gallery-dl "https://boards.4chan.org/a/" \
    -d dataset/sfw \
    --download-archive archive.txt \
    --filter "extension in ['jpg', 'jpeg', 'png']" \
    --range 1-15000

echo "✅ All downloads started. Leave this running overnight."
