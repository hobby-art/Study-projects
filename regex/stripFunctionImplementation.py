"""
This program implements str.strip() function. Removes whitespaces from both sides
if no arguments were passed, and removes characters given in the second argument
from the input_text if the argument was passed.
"""

import re


def strip_func(input_text: str, stripped_chars: str = "") -> str:
    # Checking if the second argument was given. If not, we look for whitespaces
    # at the ends of the input_text and remove them.
    if stripped_chars == "":
        whitespaces = re.compile(r"^\s*(.*?)\s*$")
        match = whitespaces.search(input_text)
        if match:
            return match.group(1)
        else:
            return "Invalid argument."
    # If the second argument was given, send its characters to the character class
    # in the regex, remove them from the ends of the input_text and return what is left.
    else:
        custom_chars = re.compile(f"^[{stripped_chars}]*(.*?)[{stripped_chars}]*$")
        match = custom_chars.search(input_text)
        if match:
            return match.group(1)
        else:
            return "Invalid argument."


text = "abc123abc"
print(strip_func(text, "abc"))
