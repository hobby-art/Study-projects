"""
This program checks files numeration (file001, file002, etc.).
If there is a gap (file003, file005), it will rename the files
to fix the numeration.
"""

import re, shutil
from pathlib import Path


# Creating example files for the function.
for i in range(1, 21):
    if i not in (3, 11, 15):
        with open(f"spam/spam{str(i).zfill(3)}.txt", "w") as file:
            file.write(f"Hello {i}")


def files_numerator() -> None:

    # Asking user for:
    # 1. Folder path where to check the files.
    # 2. Files prefix.
    # 3. From which number numeration begins.
    source_folder = Path(input("Provide the folder address: "))
    prefix: str = input("What is the files prefix: ")
    title_counter: int = int(input("From which number to count: "))

    # Regex pattern for numbers at the end of the file name.
    suffix_numbers = re.compile(r"\d+$")

    # Getting all the files in the source_folder and sorting them out.
    all_files: list = sorted(list(source_folder.rglob(f"{prefix}*.*")))

    # Looking for files with given prefix.
    for filename in all_files:

        # Checking if there is a match and if there is, saving its lenght.
        suffix_match = suffix_numbers.search(filename.stem)
        if suffix_match:
            padding_length: int = len(suffix_match.group())
        else:
            print("No matches found. Try again.")
            break

        # If file's number doesn't match the counter,
        # we rename the file with the correct number.
        if suffix_match.group() != str(title_counter):
            shutil.move(
                filename,
                source_folder
                / (prefix + str(title_counter).zfill(padding_length) + filename.suffix),
            )

        title_counter += 1


files_numerator()
