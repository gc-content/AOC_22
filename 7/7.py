import re

dic = {}


with open("input.txt") as inp:
	name = ""
	levels = []
	for line in inp:
		if re.match("\$ cd ", line) and not re.match("\$ cd \.\.", line):
			parent = name
			name = name+"_"+line.strip().split(" ")[2]
			levels.append(name)
			if name not in dic:
				dic[name] = {"parent":parent, "children":[], "size":0}
		if re.match("^[0-9]", line):
			for level in levels:
				dic[level]["size"] += int(line.strip().split(" ")[0])
		if re.match("^dir", line):
			dic[name]["children"].append(line.strip().split(" ")[1])
		if re.match("\$ cd \.\.", line):
			levels.pop(len(levels)-1)
			name = levels[-1]


### Part 1

outsum = 0
for n in dic:
	if dic[n]["size"] <= 100000:
		outsum += dic[n]["size"]			

print(outsum)



#### Part 2
unused = 70000000 - dic["_/"]["size"]
limit = 30000000
missing = limit - unused

lenlist = []
for n in dic:
	if dic[n]["size"] >= missing:
		lenlist.append(dic[n]["size"])
print(min(lenlist))
