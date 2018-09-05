#!/usr/bin/env python
val = False
str1 = ['Hi','Hey','Hello']
str2 = ['How are you', 'How you doing']
str3 = "Bye"
str4 = "Fine"
str4 = "Same here"
message = "Hey there"
nextmsg = "I am fine , How are you ?"
while val == False:
	msg= raw_input()
	for data in str1:
		if msg == data:
			print(message)
	for nextdata in str2:
		if msg == nextdata:
			print(nextmsg)		
	if msg == str4:
		print("Okay cool")
			print(nextmsg)
	if msg == str4:
		print("Okay cool")			
	if msg == str3:
		val = True
		print("Bye see you again")
#		else:
#			 print("Plese enter")
#			 val = True
