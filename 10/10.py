
outtab = [1]

with open("input.txt") as inp:
	for line in inp:
		spl = line.strip().split(" ")
		if spl[0] == "noop":
			outtab.append(outtab[-1])
		if spl[0] == "addx":
			outtab.append(outtab[-1])
			outtab.append(outtab[-1]+int(spl[1]))


#Part 1

signal = 0
for i in range(19,220,40): 
	signal += outtab[i]*(i+1)
print(signal)

# Part2


for ln in range(6):
	line = []
	for idx,sig in enumerate(outtab[0+ln*40:40+ln*40]):
		if  sig-1 <= idx <= sig+1: #add border case
			line.append("#")
		else: line.append(".")
	print("".join(line))




