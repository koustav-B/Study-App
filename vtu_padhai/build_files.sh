#!/bin/bash

# Exit on error
set -e

# Display the current directory
echo "Current directory: $(pwd)"

# Ensure the output directory exists
OUTPUT_DIR="output"
if [ ! -d "$OUTPUT_DIR" ]; then
  echo "Creating output directory..."
  mkdir "$OUTPUT_DIR"
fi

# Copy HTML, CSS, and JS files to the output directory
echo "Copying files to $OUTPUT_DIR..."
cp index.html $OUTPUT_DIR/
cp -r styles/ $OUTPUT_DIR/
cp -r scripts/ $OUTPUT_DIR/
cp -r assets/ $OUTPUT_DIR/

# If you have any other build steps (e.g., minification, bundling), add them here
# Example: minifying CSS files
# echo "Minifying CSS files..."
# for file in styles/*.css; do
#   npx clean-css -o "${OUTPUT_DIR}/$(basename "$file")" "$file"
# done

# Output the contents of the output directory
echo "Contents of $OUTPUT_DIR:"
ls -R $OUTPUT_DIR

# Notify that the build is complete
echo "Build complete. Files are ready for deployment."

# Exit the script
exit 0
