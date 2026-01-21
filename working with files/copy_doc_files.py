"""
This program finds .docx (and .doc) files in the folder and its subfolders and then
copies them to another folder.
"""

import shutil, os
from pathlib import Path


def copy_docx():

    source_folder = Path(input("Provide the path from where files will be copied: "))
    destination_folder = Path(input("Provide the destination path: "))

    """ First I used os.walk() method but then I found a better solution."""
    # for folder_name, subfolder, filenames in os.walk(source_folder):
    #     for filename in filenames:
    #         if filename.lower().endswith(".docx") or filename.lower().endswith(".doc"):
    #             shutil.copy(Path(folder_name) / filename, destination_folder)
    #             print(Path(folder_name) / filename)

    # Searching the folder and its subfolders for docx files and copying them
    # to the destination folder.
    for file_path in source_folder.rglob("*.docx"):
        shutil.copy(file_path, destination_folder)


copy_docx()
