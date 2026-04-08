#!/usr/bin/env bash
# setup.sh – Install dependencies and generate a sample wallpaper
#
# Usage:
#   bash setup.sh                     # generate default wallpaper
#   bash setup.sh --text "My Design"  # generate with custom text

set -e

echo "Installing dependencies..."
pip install -r requirements.txt -q

echo "Running wallpaper generator..."
python3 wallpaper_generator.py --random "$@"
