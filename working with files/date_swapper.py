"""
This program searches files that have dates in their names
and swaps days with months. In case we need to change
american date format to a normal one. Or the other way around.
"""

import re, shutil
from pathlib import Path

# Ask user to give a directory with files.
working_directory = Path(input("Provide directory path: "))

# A regex pattern for dates: MM-DD-YYYY
mm_dd_yyyy_regex = re.compile(r"(.*)?(\d{2})-(\d{2})-(\d{4})(.*)?")


# Searching the files in the provided directory and changing the name if
# found a match.
for file_path in working_directory.rglob("*.*"):

    date_match = mm_dd_yyyy_regex.search(file_path.name)
    if date_match:
        prefix, month, day, year, suffix = date_match.groups()
        new_name = f"{prefix}{day}-{month}-{year}{suffix}"
        shutil.move(file_path, working_directory / new_name)
