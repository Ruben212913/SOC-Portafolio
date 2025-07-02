# Bandit Report - Key Levels (0, 3, 5, 6)

## Level 0 → 1
**Commands Used**:
```bash
ls
cat readme

Learning:

Basic file reading

Identifying credentials in text files

##Level 3 → 4
Commands Used:

Bash

ls -a
cat ./.hidden
Learning:

Detecting hidden files


Understanding dot files in Linux

##Level 5 → 6
Commands Used:

Bash

find . -type f -size 1033c -not -executable
cd maybehere07
ls -al .file2
cat .file2

Learning:

Advanced find command usage (by size, type, and permissions)

Filtering for non-executable files

Navigating and verifying specific file properties

##Level 6 → 7
Commands Used:

Bash

find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
Learning:

Combining multiple find filters (user, group, size)

Searching the entire filesystem (/)

Suppressing error messages (2>/dev/null)

