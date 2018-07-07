#!/usr/bin/env python
import urllib
find_members = []
for member in dir(urllib):
    if "open" in member:
        find_members.append(member)

print(sorted(find_members))
