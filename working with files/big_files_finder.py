"""
This program searches for files bigger than 100 MB in the folder
provided by user.
"""

from pathlib import Path


def biggies_finder() -> None:

    # Asking user for a folder path where to search.
    source_folder = Path(input("Provide folder address where to search: "))

    # The counter increases by 1 if a file bigger than 100 MB was found.
    big_files_counter: int = 0

    # Searching the provided folder and its subfolders.
    for filename in source_folder.rglob("*"):

        if filename.stat().st_size / (1024**2) > 100:
            print(filename)
            big_files_counter += 1

    if big_files_counter == 0:
        print("No files bigger than 100 MB found.")
    else:
        print(f"Overall big files found: {big_files_counter}")


biggies_finder()
