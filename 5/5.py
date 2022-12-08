'''
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
'''


'''
[V]     [B]                     [F]
[N] [Q] [W]                 [R] [B]
[F] [D] [S]     [B]         [L] [P]
[S] [J] [C]     [F] [C]     [D] [G]
[M] [M] [H] [L] [P] [N]     [P] [V]
[P] [L] [D] [C] [T] [Q] [R] [S] [J]
[H] [R] [Q] [S] [V] [R] [V] [Z] [S]
[J] [S] [N] [R] [M] [T] [G] [C] [D]
 1   2   3   4   5   6   7   8   9 

move 1 from 8 to 4
move 1 from 7 to 8
'''


crates = []
with open("input_short.txt") as inp:
	for line in inp:
		if not line.startswith("move") and not line.startswith(" 1"):
			line = line.replace("    [","[.]-[")  ##
			line = line.replace("    ","-[.]")    ## quite ugly
			line = line.replace(" [", "-[")       ## but it works
			line = line.strip().split("-")        ## at least at my and test input
			for idx, n in enumerate(line):
					try:
						if n != "[.]":
							crates[idx].append(n)
						else:
							len(crates[idx]) ## to toggle try...
					except IndexError:
						if n =="[.]":
							crates.append([])
						else:
							crates.append([n])
			
		elif line.startswith("move"):
			line = line.strip().split(" ")
			quant = int(line[1])
			frm = int(line[3])-1
			to =  int(line[5])-1

			crates[to] = crates[frm][0:quant] + crates[to]  ## crates[frm][0:quant][::-1] # for part 1
			del crates[frm][0:quant]

print("".join(n[0][1] for n in crates))
