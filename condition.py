#!/usr/bin/env python
username = raw_input("Enter username")
if 10 >= len(username) >=6:
    print("Username is valid")
else:
    print("NOt valid")

print("Your name is %s" % username)
