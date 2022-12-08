'''
### 1

out = 0

with open("input.txt") as inp:
	for line in inp:
		line=line.strip()
		c1 = line[0:int(len(line)/2)]
		c2 = line[int(len(line)/2):]
		buff = []
		for item in c1:
			for item2 in c2:
				if item==item2:
					no = ord(item)
					if no > 90:
						no -= 96
					else:
						no -= 64-26
					if no not in buff: buff.append(no)
		out += sum(buff)
print(out)
'''

###2

out = 0 

with open("input.txt") as inp:
	flag = 1
	for line in inp:
		if flag == 1:
			tab = line.strip()
			flag += 1
		else:
			tab2 = []
			for item in tab:
				for item2 in line.strip():
					if item==item2:
						if item not in tab2:
							tab2.append(item)
			tab = tab2
			flag += 1
		if flag == 4:
			for item in tab:
				no = ord(item)
				if no > 90:
					no -= 96
				else:
					no -= 64-26
				out += no
			flag = 1
print(out)



