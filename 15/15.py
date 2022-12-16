from collections import deque

'''  # :.)
def sphare_squere(point, radius, outdict):  ## could stream directly to dic
	x,y = point
	for i in range(-radius,radius+1):
		for j in range(-abs(radius-abs(i)), abs(radius-abs(i))+1):
			try:
				outdict[i+y].add(j+x)
			except KeyError:
				outdict[i+y] = {j+x}
'''


def sphare_squere2(point, radius, outdict):  ## could stream directly to dic (does now)
	x,y = point
	for i in range(-radius,radius+1):
		j1,j2 = -abs(radius-abs(i)), abs(radius-abs(i)) ## reduntant
		try:
			outdict[i+y].add((j1+x, j2+x))  ## could use numpy array
		except KeyError:
			outdict[i+y] = {(j1+x, j2+x)}


		
def mann_dist(p,p2):
	return(abs(p[0]-p2[0])+abs(p[1]-p2[1]))


def expand_ranges(ranges):
	mn,mx = ranges[0][0], ranges[0][1]
	for x1,x2 in ranges:
		if x1<mn: mn=x1
		if x2>mx: mx=x2
	return((mn,mx))

def overlap(range1,range2):
	if (range1[1]>=range2[0] and range1[1]<=range2[1]) or (range2[1]>=range1[0] and range2[1]<=range1[1]) :
		return True
	else: return False



dic_cov = {}
dic_sens = {}
dic_beac = {}

with open("input.txt") as inp:
	for line in inp:
		line = line.strip().replace("="," ").split(" ")
		s = int(line[3][:-1]), int(line[5][:-1])
		b = int(line[11][:-1]), int(line[13])
		for n,k in [s]:
			try:
				dic_sens[k].add(n)
			except KeyError:
				dic_sens[k] = {n}
		for n,k in [b]:
			try:
				dic_beac[k].add(n)
			except KeyError:
				dic_beac[k] = {n}
		dist = mann_dist(s,b)

		sphare_squere2(s,dist,dic_cov)

for k in dic_cov:
	l = deque(dic_cov[k])
	l = sorted(l, key=lambda n:n[0])
	idx = 0 

	while idx<len(l)-1:
		if overlap(l[idx],l[idx+1]):
			er = expand_ranges((l[idx],l[idx+1]))
			for i in (l[idx],l[idx+1]): l.remove(i)
			l.insert(idx, er)
		else:
			idx += 1

	dic_cov[k] = set(l)


### PART 1

'''
test_y = 2000000


sumlen=0
for n in dic_cov[test_y]:
	rangelen = abs(n[0]-n[1])+1
	try:
		for k in dic_beac[test_y]:
			if overlap(n,(k,k)):
				rangelen -=1



	except KeyError:
		pass
	sumlen+=rangelen

print(sumlen)




'''
### Part2:

limits = 0, 4000000


def trim_range(r, limits):
	x1out,x2out = r
	if overlap(r, limits):
		if r[0] < limits[0]: x1out = limits[0]
		if r[1] > limits[1]: x2out = limits[1]
		return (x1out,x2out)
	else: return False



for n in range(limits[0],limits[1]+1):
	sumlen = 0
	try:
		for k in dic_cov[n]:
			trimmed_k = trim_range(k,limits)
			if not trimmed_k:
				continue
			rangelen = abs(trimmed_k[0]-trimmed_k[1])+1

			sumlen += rangelen
	except KeyError:
		continue
	if sumlen <= limits[1]-limits[0]:
		almost_there = sorted(dic_cov[n], key=lambda k: k[0])
		almost_there = almost_there[0][1]+1   ### not very robust xd
		almost_there = almost_there*4000000+n
		print(n, sumlen, dic_cov[n], almost_there)






