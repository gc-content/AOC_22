rounds = 20 # 20 for part 1

### part 1
import math

class Monkey:
	def __init__(self, ID, items, operation, test_n, if_t, if_f, inspects):
		self.ID = ID
		self.items = items
		self.operation = operation
		self.test_n = test_n
		self.if_t = if_t
		self.if_f = if_f
		self.inspects = inspects
	def __str__(self):
		return f"{self.ID}\n{self.items}\n{self.operation}"
	
	def inspect(self, item):
		func = self.operation.split(" ")
		self.inspects += 1
		if func[1] == "*":   ## could use eval (maybe with regex for safaty)
			if func[2] == "old":
				return(item*item)
			else:
				return(item * int(func[2]))
		elif func[1] == "+":
			return(item + int(func[2]))
		

	def throw(self, item, monkeys):
		if item%self.test_n == 0:
			monkeys[self.if_t].items.append(item)
			self.items = self.items[:-1]
		else : 
			monkeys[self.if_f].items.append(item)
			self.items = self.items[:-1]



monkeys = []

with open("input.txt") as inp:
	l_count = 0

	for line in inp:
		if line.startswith("Monkey"):
			ID = int(line.strip().split(" ")[1].replace(":",""))
			l_count += 1
		elif l_count == 1:
			items = [int(n) for n in line.strip().split(": ")[1].split(", ")]
			l_count += 1
		elif l_count == 2:
			operation = line.strip().split("= ")[1]
			l_count += 1
		elif l_count == 3:
			test_n = int(line.strip().split("by ")[1])
			l_count += 1
		elif l_count == 4:
			if_t = int(line.strip().split("monkey ")[1])
			l_count += 1
		elif l_count == 5:
			if_f = int(line.strip().split("monkey ")[1])
			monkeys.append(Monkey(ID,items,operation,test_n,if_t,if_f,0))
			l_count = 0 
	

for r in range(rounds):
	for monkey in monkeys:
		for item in monkey.items:
			item = monkey.inspect(item)
			item = math.floor(item/3) # part 1
			monkey.throw(item, monkeys)


top2 = sorted([monkey.inspects for monkey in monkeys])[-2:]
print(top2[0]*top2[1])




