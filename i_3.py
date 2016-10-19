import argparse

def check_password(passwd):
	"""
	Check the password to see if it conforms to the rules
	1. length >= MIN_LENGTH
	2. must contain at least one upper case character
	3. must contain at least one lower case character
	4. must contain at least one digit
	5. must contain at least one non-alpganumeric character

	args: passwd: candidate password string
	returns: True iff all criteria have been met; False otherwise
	"""
	MIN_LENGTH = 6
	has_upper = False
	has_lower = False
	has_digit = False
	has_other = False
	if len(passwd) < MIN_LENGTH:
		return False
	for ch in passwd:
		if ch.isalnum():				
			if ch.isdigit():
				has_digit = True
			elif ch.isupper():
				has_upper = True
			else:
				has_lower = True
		else:
			has_other = True
	return has_upper and has_lower and has_digit and has_other

def main():
	parser = argparse.ArgumentParser(description="Check password for validity")
	parser.add_argument("Password", type=str, help="Proposed password (a string)")	
	args = parser.parse_args()
	passwd = args.Password
	if check_password(passwd):
		print(passwd, "is a legal password")
	else:
		print(passwd, "is an illegal password")

if __name__=="__main__":
	main()

#ask about how to copy file destination and pathway to the next lines