# Find a list of all of the names in the following string using regex.
import re

text = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

pattern = re.compile(r'[A-Z]([a-z]+|\.)')

matches = pattern.finditer(text)

for match in matches:
    print(match)

# print(r'\tTab')