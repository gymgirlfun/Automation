# • The ? matches zero or one of the preceding group.
# • The * matches zero or more of the preceding group.
# • The + matches one or more of the preceding group.
# • The {n} matches exactly n of the preceding group.
# • The {n,} matches n or more of the preceding group.
# • The {,m} matches 0 to m of the preceding group.
# • The {n,m} matches at least n and at most m of the preceding group.
# • {n,m}? or *? or +? performs a non-greedy match of the preceding group.
# • ^spam means the string must begin with spam.
# • spam$ means the string must end with spam.
# • The . matches any character, except newline characters.
# • \d, \w, and \s match a digit, word, or space character, respectively.
# • \D, \W, and \S match anything except a digit, word, or space character, respectively.
# • [abc] matches any character between the brackets (such as a, b, or c).
# • [^abc] matches any character that isn’t between the brackets.

#! python3
# phoneAndEmail.py - Exrtacts phones and emails from clipboard

'''
Contact Us

No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103 USA
Phone: 800.420.7240 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST)
Fax: +1 415.863.9950 ext. 12345

Reach Us by Email

General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Academic requests: academic@nostarch.com (Further information)
Conference and Events: conferences@nostarch.com
Help with your order: info@nostarch.com
'''

''' redacted message

Contact Us

No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103 USA
Phone:800******* or 415******* (9 a.m. to 5 p.m., M-F, PST)
Fax: 415*******

Reach Us by Email

General inquiries: ****.com
Media requests: ****.com
Academic requests: ****.com (Further information)
Conference and Events: ****.com
Help with your order: ****.com
'''

import re, pyperclip


phoneRegex = re.compile(r'''(
	(\+\d)?	# Country Code
	(\s*)?	# separator
	(\d{3}|\(\d{3}\))? # Area Code
	(\s*|-|\.)? # separator
	(\d{3})	# first 3 digits
	(\s*|-|\.)? # separator
	(\d{4})	# last 4 digits
	(\s*(ext(\.)?|x)\s*\d{2,5})? # extension
	)'''
, re.VERBOSE
)


# Create email regex.
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+	# username
	@	# @ symbol
	[a-zA-Z0-9.-]+	# domain name
    (\.[a-zA-Z]{2,4})	# dot-something
   )'''
, re.VERBOSE)

print("Original Message:".center(50, "="))
messages = str(pyperclip.paste())
print(messages)

matches = []
print("Phone:".center(50, "="))
phones = phoneRegex.findall(messages)
print(phones)
# Normilize phone format
for phone_group in phones:
	phone = "-".join([phone_group[3], phone_group[5], phone_group[7]])
	if (phone_group[8]):
		phone += " " + phone_group[8]
	# the + operator concatnating the elements (+ overload)
	# while append() append an array ref to the end of the original array
	# if use matches += phone.strip() will result in each digit will be an arr element
	matches.append(phone.strip())  

print("Email:".center(50, "="))
emails = emailRegex.findall(messages)
print(emails)
matches += [email[0] for  email in emails] # concatenating
matches = "\n".join(matches)

print("Extracted Message:".center(50, "="))
if (len(matches)>0):
	pyperclip.copy(matches)
	print(f"Copied phones and emails to clipboard:\n {matches}")
else:
	print("Found no matches")

print("Redacted Message:".center(50, "="))
redacted = phoneRegex.sub(r"\4*******", messages)
redacted = emailRegex.sub(r"****\2", redacted)
print(redacted)



