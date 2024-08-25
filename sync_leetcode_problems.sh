#!/bin/bash

# Define source and destination directories
source_dir="/Users/niranjanabalaji/leetcode/problems"
dest_dir="/Users/niranjanabalaji/leetcode/"

# Navigate to the destination directory
cd "$dest_dir"

# Add, commit, and push changes to GitHub
git add .
git commit -m "Automated sync $(date +"%Y-%m-%d %H:%M:%S")"
git push origin main
