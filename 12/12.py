import sys 
from collections import deque

grid = []
S,E = [],[0,0]
with open("input.txt") as inp:
	ln = 0
	for line in inp:
		line = line.strip()
		linearr = []
		for idx, n in enumerate(line):
			#if n == "S": S = [ln, idx]; linearr.append("a") #part 1
			if n == "S" or n =="a": S.append([ln,idx]); linearr.append("a") #part2 
			elif n == "E": E = ln, idx; linearr.append("z")
			else: linearr.append(n)
		ln += 1
		grid.append(linearr)


def neighs(point,grid):
	y,x = point
	ncol = len(grid[0])
	nrow = len(grid)
	neighs = [[y-1,x],[y,x-1],[y,x+1],[y+1,x]]
	neighs = [m for m in neighs if nrow > m[0] >= 0 and ncol > m[1] >= 0  ]
	return neighs

dic = {}
for idl, line in enumerate(grid):
	for ids, s in enumerate(line):
		num1 = ord(s)
		for n in neighs((idl,ids),grid):
			num2 = ord(grid[n[0]][n[1]])
			if num2-1  <= num1:
				try:
					dic[tuple(n)].append((idl,ids))
				except KeyError:
					dic[tuple(n)] = [(idl,ids)]




### backtrace the dic 


### "inspired" by https://www.python.org/doc/essays/graphs/
def traverse(graph, S, E):
	dist = {S:[S]}
	q = deque([S])
	while len(q):
		at = q.popleft()
		for next in graph[at]:
			if next not in dist:
				dist[next] = [dist[at],next]
				q.append(next)
	return dist.get(E)


def unpack(lst, out):
	out.append(lst[-1])
	if len(lst) > 1:
		unpack(lst[0],out)
	return out

### Part 1:
'''
a = traverse(dic,tuple(E),tuple(S))

a = unpack(a)

print(len(a)-1)

'''

### Part2:

#ways = [unpack(traverse(dic, tuple(E), tuple(s))) for s in S]
ways = []
for s in S:
	a = traverse(dic,tuple(E), tuple(s))
	if a:
		out = []
		a = unpack(a, out)
		ways.append(a)


print(min([len(x)-1 for x in ways]))














