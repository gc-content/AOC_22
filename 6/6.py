with open("input.txt") as inp:
	string =  inp.read()

for i in range(len(string)):
	if len(set(string[i:i+14]))==14:
		print(i+14)
		break
