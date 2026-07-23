#exp-1

import re

text = input("Enter the Text:")


match_result = re.match(r"My", text)

if match_result:
    print("Match found at the beginning:", match_result.group())
else:
    print("No match found at the beginning.")


email = re.search(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)

if email:
    print("Email found:", email.group())
else:
    print("Email not found.")


phone = re.search(r'\b\d{10}\b', text)

if phone:
    print("Phone number found:", phone.group())
else:
    print("Phone number not found.")
