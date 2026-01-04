import re

phoneNumberRegx = re.compile(r'\+\d\d\d-\d\d\d\d\d\d\d\d\d\d')
message = "Call me at +977-9842106109 or I've another phone number as +977-9842684025"


# mo = phoneNumberRegx.search(message)
print(phoneNumberRegx.findall(message))
# print(mo.group())