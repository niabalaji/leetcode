#!/bin/bash
# script to upload solutions to github

# Navigate to the directory containing your LeetCode solutions
cd /Users/niranjanabalaji/leetcode/problems

# Add all changes to the staging area
git add .

# Commit changes with a message containing the current date and time
git commit -m "Auto-update LeetCode solutions: $(date +'%Y-%m-%d %H:%M:%S')"

# Push changes to the remote repository
git push origin main
