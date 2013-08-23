typ = raw_input('1 - binary to decimal 2 - decimal to binary?\n')
num = raw_input('Enter your number:\n')
def converter(n):
	if typ == '1':
		print int(num, 2)
	elif typ == '2':
		print bin(int(num))[2:]

converter(num)