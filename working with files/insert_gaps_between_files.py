"""
This program checks files numeration (file001, file002, etc.)
and puts a gap in it (file003, file005) by renaming the files
after the gap.
"""

import re, shutil, logging, sys
from pathlib import Path

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)

# Example files for the function.
for i in range(1, 51):
    with open(f"spam/spam{str(i).zfill(3)}.txt", "w") as file:
        file.write(f"Hello {i}")


def files_numerator() -> None:

    # Asking user for:
    # 1. Folder path where to check the files.
    # 2. Files prefix.
    # 3. From which number numeration begins.
    source_folder = Path(input("Provide the folder address: "))
    prefix: str = input("What is the files prefix: ")
    gap_location: str = input("After which number make a gap: ")

    # Getting all the files in the source_folder and sorting them out.
    all_files = sorted(list(source_folder.rglob(f"{prefix}*.*")))

    # Regex pattern for numbers at the end of the file name.
    suffix_numbers = re.compile(r"\d+$")

    # Looking for files with given prefix in reversed order.
    # We will move UP the files numbers by one and go down
    # until we reach the limit.
    for filename in reversed(all_files):

        # Checking if there is a match and if there is, saving its lenght.
        suffix_match = suffix_numbers.search(filename.stem)
        if not suffix_match:
            continue

        padding_length: int = len(suffix_match.group())
        # Saving current value of the file's number in a variable.
        current_val: int = int(suffix_match.group())
        limit: int = int(gap_location)

        # Proceed if the file's number is bigger than the limit.
        # If it is, increase the number by one. Repeat until
        # you reach the limit, where the gap will be made.
        if current_val > limit:
            new_val = current_val + 1
            new_name = f"{prefix}{str(new_val).zfill(padding_length)}{filename.suffix}"
            shutil.move(filename, source_folder / new_name)
            logging.debug(f"Shifted {filename} UP to {new_name}")
        else:
            logging.debug(f"Reached the gap: {filename.name}.")


files_numerator()
