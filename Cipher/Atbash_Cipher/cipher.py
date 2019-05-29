#!/usr/bin/python
from string import lowercase,uppercase
text = raw_input("text: ")
s =" "
for char in text.lower():
	if ord(char) in range(97,122):
		code = 25 - ord(char) +(2*ord('a'))
		char = chr(code)
	s = s+ char
print "cipher text: " + s