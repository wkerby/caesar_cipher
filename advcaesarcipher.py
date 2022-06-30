#create a function for the advanced caesar cipher
#parameters are a single-line text string, and the number of alphabetical shifts used for transformation
#of each character in the string
def advcaesar(string,shift_num):
	if shift_num < 1 or shift_num > 25:
		return print("Please enter a valid shift number.")
	cipher = ""
	for char in string:
		if char == '\n':
			return print("The message must be comprised of one line.")
			break
		elif char.isspace():
			cipher += char
		elif char in ["z","Z"]:
			if char.isupper():
				charnum = ord("A") + (shift_num - 1)
			else:
				charnum = ord("a") + (shift_num - 1)
			cipher += chr(charnum)
		elif char.isdigit():
			cipher += char
		else:
			if char.isalpha():
				if char.isupper():
					if ord(char) + shift_num > ord("Z"):
						diff = ord("Z") - ord(char)
						charnum = ord("A") + (shift_num - diff - 1)
					else:
						charnum = ord(char) + shift_num
				elif char.islower():
					if ord(char) + shift_num > ord("z"):
						diff = ord("z") - ord(char)
						charnum = ord("a") + (shift_num - diff - 1)
					else:
						charnum = ord(char) + shift_num
			else:
				charnum = ord(char) + shift_num
			cipher += chr(charnum)
	return print(cipher)


advcaesar("My father believed that all good things, trout as well as eternal salvation, come by grace. And grace comes by art. and art does not come easy.", 3)