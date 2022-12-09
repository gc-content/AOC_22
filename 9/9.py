import time


def is_adj(point1,point2):
	y,x = [point1[0],point2[0]], [point1[1],point2[1]]
	if abs(min(y)-max(y)) > 1 or abs(min(x)-max(x)) > 1 : return False
	else: return True



def follow(head,tail):
	if head[0] == tail[0]:
		if head[1] > tail[1]:
			return ([head[0],head[1]-1])
		else:
			return ([head[0], head[1]+1])
	elif head[1] == tail[1]:
		if head[0] > tail[0]:
			return ([head[0]-1,head[1]])
		else:
			return ([head[0]+1, head[1]])

	elif head[0] > tail[0]:
		if head[1] > tail[1]:
			return([tail[0]+1,tail[1]+1])
		elif head[1]<tail[1]:
			return([tail[0]+1,tail[1]-1])

	elif head[0] < tail[0]:
		if head[1] > tail[1]:
			return([tail[0]-1,tail[1]+1])
		elif head[1]<tail[1]:
			return([tail[0]-1,tail[1]-1])





with open("input.txt") as inp:
	lnn = 0 # for animation
	n_seg = 10 # 2 for part 1
	coords = [[0,0] for k in range(n_seg)]
	dirs = {"R":(0,1),"L":(0,-1),"U":(1,0),"D":(-1,0)}
	ways = [[tuple(coords[n])] for n in range(n_seg)]
	onscreen = True
	for line in inp:
		line = line.strip().split(" ")
		steps = int(line[1])
		d = line[0]

		for step in range(steps):
			lnn +=1  # for animation
			coords[0][0] += dirs[d][0]
			coords[0][1] += dirs[d][1]

			for s in range(1,len(coords)):
				if not is_adj(coords[s-1],coords[s]):
					coords[s]= follow(coords[s-1],coords[s])

			for k in range(n_seg): ways[k].append(tuple(coords[k])) 

### Debuging animation:
			
			if onscreen:
				grid_size = (50,25)
				grid = [["." for n in range(grid_size[0])] for k in range(grid_size[1])]
		    
				for idx, k in enumerate(ways):
					try:
						grid[int(grid_size[1]/2)-k[lnn][0]][int(grid_size[0]/2)+k[lnn][1]] = str(idx)
					except IndexError: 
						onscreen = False
						print("Snake escaped")
						break	
				time.sleep(0.001)
				#input() #for step-by-step
				print("--------------")
				for n in grid:
					print("".join(n))



print(len(set(ways[n_seg-1])))


