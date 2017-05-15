#!/usr/bin/env python
import re

_author_ = "rifatul.islam"

phone_num_regex = re.compile(r'''((\d{3})?\d{3}-*\d{3}-*\d{4})''')

# Search will extract the first occurrence.
extracted_phone = phone_num_regex.search("My Phone number USA cell is: 4155554242 and BD phone is: 8801926234890 ")
extracted_all_phone = (phone_num_regex.
                       findall("My Phone number 01800225544 cell is: 4155554242 and BD phone is: 8801926234890 "))
print(extracted_phone.group())
print(extracted_all_phone)

# Regex symbol

bat_string = "Batman Batmobile Batcopter Batbat"

bat_regex = re.compile(r'Bat(wo)?man')
print(bat_regex.search(bat_string).group())

# Replacing the matched regex
namesRegex = re.compile(r'Agent')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# Hiding  the sensitive name information
namesRegex = re.compile(r"Agent (\w)\w*")
print(namesRegex.sub(r"\1****", 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent'))
