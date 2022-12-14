import ast 

pairs = [[]] 
count = 0
with open("input.txt") as inp:
	for line in inp:
		if line.startswith("\n"):
			count +=1 
			pairs.append([])
		else:
			pairs[count].append(ast.literal_eval(line.strip())) ##danger


#print(pairs)

def compare(a,b):
	print(f"TYPES: {type(a), type(b)}")
	print(f"PAIR A:{a}")
	print(f"PAIR B:{b}")
	if type(a) == int and type(b) == int:
		print("AAAA")
		print(a, b)
		if a > b:  print("1return 0"); return 0 
		elif a  < b:  print("1return 1"); return 1
	elif type(a) == list and type(b) == int:
		print("BBBB")
		return compare(a, [b])
	elif type(a) == int and type(b) == list:
		print("CCCCC")
		return compare([a], b)
	elif type(a) == list and type(b) == list:
		print("DDDDD")
		if len(a) == 0 and len(b) != 0 : print("2return 1"); return 1
		elif len(b) == 0 and len(a)!=0: print("2return 0"); return 0
		n = min(len(a),len(b))
		print(f"N: {n}")
		lst = []
		for idx in range(n):
			print(f"IDX:{idx}")
			lst.append(compare(a[idx], b[idx]))
		print(f"LST0:{lst}")
		lst = [k for k in lst if k!=None]
		print(f"LST: {lst}")
		if len(lst) == 0:
			print("ZERO")
			if len(a) < len(b):
				print("3return 0")
				return 1
			elif len(a) > len(b): print("3return 1"); return 0
		else:
			print(f"LST2: {lst}, {lst[0]}")
			return lst[0]



#print(type(pairs[0][1]))
aa = []
for idx, pair in enumerate(pairs):
	print(f"PAIR {idx}")
#	for idx2, p in enumerate(pair[1][0]):
#		print(f"P1:{pair[0][0][idx2]}")
#		print(f"P1:{pair[1][0][idx2]}")
	a = compare(pair[0],pair[1])
	print("aaaaaaaaaaaaaaaaaa")
	print(a)
	aa.append(a)
print(aa)

print(sum([(idx + 1) for idx, a in enumerate(aa) if a == 1]))







