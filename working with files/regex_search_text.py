"""
This program opens all .txt files in a folder and searches for any text that
matches a user-supplied regular expression, then prints the results to the screen.
"""

from pathlib import Path
import re, sys

# Ask user for the folder path where to search matches.
# Also checking if the path leads to a folder.
while True:
    search_dir = Path(input("Provide folder path: "))
    if not search_dir.is_dir():
        print("This is not a folder. Try another address.")
        continue
    else:
        break

# Ask user for a regex that will be used for searching.
# Also checking if user provides an invalid regex.
while True:
    try:
        user_regex = re.compile(input(r"Provide regular expression: "))
        break
    except re.error as e:
        print(f"Invalid regex: {e.msg}\nTry another.")
        continue

# Getting all the .txt files in the provided folder.
text_files = list(search_dir.glob("*.txt"))

# Searching matches in the files and saving them in the dictionary.
file_matches = {}
for file in text_files:
    with open(file, "r", encoding="UTF-8") as file_obj:
        content = file_obj.read()
        matches = user_regex.findall(content)
        file_matches[file.name] = matches

# Checking if there are no matches.
if not any(file_matches.values()):
    print("No matches found.")
    sys.exit()

# Printing found matches.
for file_name in file_matches:
    if file_matches[file_name] == []:
        continue
    print(f"Found in file '{file_name}':")
    for match in file_matches[file_name]:
        print(match)
    print()
