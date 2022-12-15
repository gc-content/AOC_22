import ast 
from collections import deque


def compare(a,b):
	if type(a) == int and type(b) == int:
		if a > b:
			return 0 
		elif a  < b:
			return 1
	elif type(a) == list and type(b) == int:
		return compare(a, [b])
	elif type(a) == int and type(b) == list:
		return compare([a], b)
	elif type(a) == list and type(b) == list:
		if len(a) == 0 and len(b) != 0 :
			return 1
		elif len(b) == 0 and len(a)!=0:
			return 0
		n = min(len(a),len(b))
		lst = []
		for idx in range(n):
			lst.append(compare(a[idx], b[idx]))
		lst = [k for k in lst if k!=None]
		if len(lst) == 0:
			if len(a) < len(b):
				return 1
			elif len(a) > len(b): 
				return 0
		else:
			return lst[0]

### PART1 :

pairs = [[]] 
count = 0
with open("input.txt") as inp:
	for line in inp:
		if line.startswith("\n"):
			count +=1 
			pairs.append([])
		else:
			pairs[count].append(ast.literal_eval(line.strip())) ##danger


aa = []
for idx, pair in enumerate(pairs):
	a = compare(pair[0],pair[1])
	aa.append(a)
print(aa)

print(sum([(idx + 1) for idx, a in enumerate(aa) if a == 1]))



### PART2 : 

with open("input.txt") as inp:
	dividers = [[[2]],[[6]]]
	pairs = deque(dividers)
	b = pairs[0]
	

	for line in inp:
		if line.startswith("\n"):
			continue
		a = ast.literal_eval(line.strip())
		idx = 0
		for idx,n in enumerate(pairs):
			if compare(a,pairs[idx]) == 1:
				pairs.insert(idx,a)
				break
			elif idx==len(pairs)-1:
				pairs.append(a)
				break



final = 1
for idx,n in enumerate(pairs):
	if n in dividers: final *= idx+1    ## could be done on the fly
print(final)

