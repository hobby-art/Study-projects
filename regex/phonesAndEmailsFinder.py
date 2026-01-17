"""
This program scans text in a clipboard for ukrainian phone numbers and emails.
"""

import pyperclip, re

# Regex for phone numbers patterns in different formats.
phone_regex = re.compile(
    r"""
                         
                (?:\+?38)?     # Optional country code +38
                [\s\-]?        # Optional space or hyphen
                \(?0[\s\-]?\(?\d{2}\)?  # Operator code with optional parentheses around and an optional space or hyphen after zero
                [\s\-]?        # Optional space or hyphen
                \d{3}          # Three numbers
                [\s\-]?        # Optional space or hyphen
                \d{2}          # Two numbers
                [\s\-]?        # Optional space or hyphen
                \d{2}          # Last two numbers

                """,
    re.VERBOSE,
)

# Regex for emails.
email_regex = re.compile(r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(?:\.[a-zA-Z]+))")

# Get text from the clipboard.
text = str(pyperclip.paste())

# Save matched phone numbers into a list.
phone_matches = []
for phone in phone_regex.findall(text):
    phone_matches.append(phone)

# Format matched phone numbers, so it's just numbers with a country code: "+380 (44) 123-45-67" -> "380441234567".
# Save them in a new list.
phone_format = re.compile(r"\D+")
formatted_phones = []
for number in phone_matches:
    formatted_number = phone_format.sub("", number)
    if formatted_number[0] == "0":
        number_with_code = "38" + formatted_number
        formatted_phones.append(number_with_code)
    else:
        formatted_phones.append(formatted_number)

# Save matched emails in a list.
email_matches = []
for email in email_regex.findall(text):
    email_matches.append(email)

# Combine phone numbers with emails.
all_matches = formatted_phones + email_matches

# Copy all matches to the clipboard and make each match on a new line.
pyperclip.copy("\n".join(all_matches))
print("\n".join(all_matches))
