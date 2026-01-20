"""
This program reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file.

Example: The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
"""

import re


# Read and save the string of the text we want to change.
with open("source_text.txt", "r", encoding="UTF-8") as input_file:
    source_text = input_file.read()


# Find matches in the text and save them in the list.
words_regex = re.compile(r"ADJECTIVE|NOUN|ADVERB|VERB")
matches = words_regex.findall(source_text)


# Loop through the matches and ask for user's corresponding words.
# Save user's words in another list in the same order as matches.
user_input = []

for word in matches:
    if word == "ADJECTIVE":
        user_input.append(input("Write an adjective: "))
    elif word == "NOUN":
        user_input.append(input("Write a noun: "))
    elif word == "ADVERB":
        user_input.append(input("Write an adverb: "))
    elif word == "VERB":
        user_input.append(input("Write a verb: "))


# Replace matches with the words given by user.
for i, word in enumerate(matches):
    source_text = source_text.replace(word, user_input[i], 1)


print("Output text: " + source_text)

# Write the result in the separate file.
with open("output_file.txt", "w", encoding="UTF-8") as output_file:
    output_file.write(source_text)
