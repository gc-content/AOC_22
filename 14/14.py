rocks = []
bottom = 0
with open("input.txt") as inp:
	for line in inp:
		line = line.strip().split(" -> ")
		for i in range(1,len(line)):

			rock =([int(k) for k in line[i-1].split(",")], [int(k) for k in line[i].split(",")])
			if min(rock[0][1], rock[1][1]) > bottom: bottom = min(rock[0][1], rock[1][1])
			if rock[0][0] == rock[1][0]:
				rocks.extend([(rock[0][0],n) for n in range(min(rock[0][1],rock[1][1]),max(rock[0][1],rock[1][1])+1)])
			elif rock[0][1] == rock[1][1]:
				rocks.extend([(n,rock[0][1]) for n in range(min(rock[0][0],rock[1][0]),max(rock[0][0],rock[1][0])+1)])

rocks = set(rocks)


#PART1 
'''
y=0
count = 0
while y <= bottom:
	count +=1
	x=500
	y=0
	while True:
		point = (x,y)
		if y > bottom: break
		if point in rocks:
			if (x-1,y) not in rocks:			
				x -= 1
				continue
			elif (x+1,y) not in rocks:
				x += 1
				continue
			elif (x, y-1) not in rocks:
				rocks.add((x, y-1))
				break
			

		else:
			y += 1
		
	
print(count-1)
'''


# PART2

bottom += 2 


y=0
count = 0
flow =1
while y <= bottom and flow ==1:
	count +=1
	x=500
	y=0
	while True:
		point = (x,y)
		if y > bottom: break
		if point in rocks or point[1]==bottom:
			if (x-1,y) not in rocks and y!=bottom:		
				x -= 1
				continue
			elif (x+1,y) not in rocks and y!=bottom:
				x += 1
				continue
			elif (x, y-1) not in rocks:
				rocks.add((x, y-1))
				if (x, y-1) == (500,0): flow=0
				break
			

		else:
			y += 1
		
	
print(count)



