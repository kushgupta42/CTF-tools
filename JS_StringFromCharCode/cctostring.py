#!/usr/bin/python
import os
def clear():
	if os.name =='nt':
		_ = os.system('cls')
	else:
		_ = os.system('clear')

def charCodeToString():
	#print "        input:"
	s =""
	print "        char codes: "
	while True:
		i = raw_input("        ")
		if not i:
			break
		if "," in i:
			numbers = map(int, i.split(","))
		else:
			numbers = map(int, i.split(" "))
		for i in numbers:
			s = s + chr(i)
	print "        "+s
	raw_input()

def stringToCharCode():
	inputStr = raw_input("        String: ")
	charCode = []
	for char in inputStr:
		charCode.append(ord(char))
	print "        "+str(charCode)
	raw_input()

while True:
	clear()
	print """
	  ____   _         ____            ____    ___        _   _____
	 / ___| | |__     / __ \   _ __   / ___|  / _ \    __| | |___ /   _ __ 
	| |     | '_ \   / / _` | | '__| | |     | | | |  / _` |   |_ \  | '__|
	| |___  | | | | | | (_| | | |    | |___  | |_| | | (_| |  ___) | | |   
	 \____| |_| |_|  \ \__,_| |_|     \____|  \___/   \__,_| |____/  |_|   
	                   \____/
	"""
	print"""
	1) String to CharCode
	2) CharCode to String
	3) Exit"""
	choice = int(input("	"))
	if choice == 1:
		stringToCharCode()
	elif choice == 2:
		charCodeToString()
	elif choice == 3:
		clear()
		exit()


	