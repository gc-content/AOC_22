import numpy as np

tab = []

with open("input.txt") as inp:
	for line in inp:
		tab.append([int(k) for k in line.strip()])

tab = np.array(tab)


def spotter_l(intab):
	indices = []
	indices_out = []
	mx = max(intab)
	for idx, n in enumerate(intab):
		if n == mx:
			indices.append(idx)
	indices_out.append(min(indices))
	sub_tab = intab[0:min(indices)]
	#print(f"imhere2:{sub_tab}")
	if len(sub_tab) >= 1:
		splice = spotter_l(sub_tab)
		indices_out.extend(splice)
	return indices_out


print(tab)


non_trans = []
for idx, n in enumerate(tab):
	a = spotter_l(n)
	b = [len(n)-x-1 for x in spotter_l(np.flip(n))]
	non_trans.extend([(idx, k) for k in sorted(set(a+b))])
#print(f"NT:\n{non_trans}")

trans_tab = np.transpose(tab)

trans = []
for idx, n in enumerate(trans_tab):
	a = spotter_l(n)
	b = [len(n)-x-1 for x in spotter_l(np.flip(n))]
	trans.extend([(k, idx) for k in sorted(set(a+b))]) # transform_coordinates



high_trees = set(non_trans+trans)
print(len(high_trees))




#### part2:

score_tab = []

nrow, ncol = np.shape(tab)

for tree in high_trees:
	l,r,u,d = 0,0,0,0
	y,x = tree[0], tree[1]
	if y == 0 or y == ncol-1 or x==0 or x == nrow-1:
		continue
# left:
	for i in reversed(range(x)):
		#print(f"i:{i}")
		l+=1
		if tab[y,x] <= tab[y,i]:
			break
# right 	
	for i in range(x+1,nrow):
		r+=1
		if tab[y,x] <= tab[y,i]:
			break
# up
	for i in reversed(range(y)):
		u+=1
		if tab[y,x] <= tab[i,x]:
			break
# down
	for i in range(y+1,ncol):
		d+=1
		if tab[y,x] <= tab[i,x]:
			break	
	
	score_tab.append(r*l*u*d)

print(max(score_tab))


