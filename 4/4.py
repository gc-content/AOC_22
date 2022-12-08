'''
##1

out = 0
with open("input.txt") as inp:
	for line in inp:
		line = line.strip().replace(",","-").split("-")
		line = [int(k) for k in line]
		if (line[0]<=line[2] and line[1]>=line[3]) or (line[2]<=line[0] and line[3]>=line[1]):
			out +=1
print(out)
'''



##2

out = 0
with open("input.txt") as inp:
	for line in inp:
		line = line.strip().replace(",","-").split("-")
		line = [int(k) for k in line]
		if (line[1]>=line[2] and line[1]<=line[3]) or (line[0]<=line[3] and line[1]>=line[3]):
			out +=1
print(out)

