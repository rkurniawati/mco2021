#! python3
# phoneANDemail.py - Find phone numbers and email addresses in a specified file
# adapted from an example in "Automate the Boring Stuff with Python"

import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # main 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9.-_%+]+   # username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-z]{2,4})   # .country
    )''', re.VERBOSE)


# find matches in clipboard text.
filename = input("Enter filename: ")
f = open(filename.strip())
text = "\n".join([line.rstrip() for line in f])

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])   # group 0 matches entire expression

if len(matches) > 0:
    print('Result')
    print('\n'.join(matches))
else:
    print('Neither phone numbers nor email addresses were found.')






