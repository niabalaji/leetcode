@echo off

REM Navigate to the directory containing your LeetCode solutions
cd /d /Users/niranjanabalaji/leetcode/problems


REM Add all changes to the staging area
git add .

REM Commit changes with a message containing the current date and time
git commit -m "Auto-update LeetCode solutions: %date% %time%"

REM Push changes to the remote repository
git push origin main
