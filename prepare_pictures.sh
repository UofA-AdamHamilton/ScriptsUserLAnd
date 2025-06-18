#!/usr/bin/env bash
# First line of the script is the shebang which tells the system how to execute
# the script: https://en.wikipedia.org/wiki/Shebang_(Unix)
# As you already figured, comments start with #. Shebang is also a comment.

# downloads the image folder called Public_images
python3 google_drive_downloader.py

# Collect all files in the input directory (non-re
directory="./Public_images"

# Iterate over all files in the target directory
for file in "./Public_images"/*; do
  # Check if the current item is a regular file (not a directory)
  if [ -f "$file" ]; then
    echo "Processing file: $file"
    # moves the file to the laton inputs folder
    mv "$file" ~/ScriptsUserLAnd/latex_example/laton_inputs
  fi
done
