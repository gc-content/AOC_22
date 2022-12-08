
'''
#1 

with open("input.txt","r") as inp:
	spl = inp.read().split("\n\n")
mx = 0
for n in spl:
	sm = sum([int(k) for k in n.strip().split("\n")])
	if sm > mx: mx = sm
print(mx)


'''

#2

with open("input.txt","r") as inp:
	spl = inp.read().split("\n\n")
out = []
for n in spl:
	sm = sum([int(k) for k in n.strip().split("\n")])
	out.append(sm)
print(sum(sorted(out, reverse=True)[0:3]))

