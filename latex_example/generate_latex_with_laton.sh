#!/bin/bash

# Set the input directory and output file
INPUT_DIR="${1:-.}"  # Default to current directory if no argument

# Check if laton is installed
if ! command -v laton &> /dev/null; then
    echo "Error: 'laton' is not installed or not in your PATH."
    exit 1
fi

# Collect all files in the input directory (non-recursive)
FILES=()
while IFS= read -r -d $'\0' file; do
    FILES+=("$file")
done < <(find "$INPUT_DIR" -maxdepth 2 -type f -print0)

# Exit if no files found
if [ ${#FILES[@]} -eq 0 ]; then
    echo "No files found in $INPUT_DIR"
    exit 1
fi

# Run laton with the files
echo "Running laton with the following files:"
printf " - %s\n" "${FILES[@]}"

laton "${FILES[@]}"

# Confirm success
if [ $? -eq 0 ]; then
    echo "LaTeX document compiled successfully"
else
    echo "An error occurred while running laton."
    exit 1
fi







