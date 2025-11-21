"""@Knorfixx"""
import random
chars = "@qwertyuiopasdfghjklzxcvbnm1234567890"

def passwd_gen():
	passwd_len = int(input("Length of password: "))
	char1 = tuple(chars)
	password = ""
	x = 0
	while x <= passwd_len:
		password += random.choice(char1)
		x+=1
	print(password)

passwd_gen()
input()
