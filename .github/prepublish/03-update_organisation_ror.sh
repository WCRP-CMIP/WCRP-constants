#!/bin/bash
# Update organisation files from ROR (Research Organization Registry)
# Repository: WCRP-constants
# This script updates institution files with latest ROR data

echo "Updating organisation files from ROR..."

if [ ! -d "organisation" ]; then
  echo "No organisation directory found, skipping..."
  exit 0
fi

# Check if upgrade_ror command is available
if command -v upgrade_ror &> /dev/null; then
  upgrade_ror --repo-path ./organisation/
  echo "✓ Organisation files updated from ROR"
else
  echo "⚠ upgrade_ror not available, skipping ROR update"
fi
