#!/bin/bash
# Copy JSON files without extension for content negotiation
# Repository: WCRP-constants

echo "Copying JSON files without .json extension..."

find . -type f -name "*.json" \
  ! -path "*/docs/*" \
  ! -path "*/summaries/*" \
  ! -path "*/.*" \
  -print0 | while IFS= read -r -d '' file; do
    dir=$(dirname "$file")
    base=$(basename "$file" .json)
    cp "$file" "$dir/$base"
    echo "  Copied: $file → $dir/$base"
done

echo "✓ JSON files copied"
