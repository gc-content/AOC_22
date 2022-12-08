""" 
### 1

wins = {"A Y":8,"B Z":9,"C X":7}
draws = {"A X":4,"B Y":5,"C Z":6}
points = {"X":1,"Y":2,"Z":3}

score = 0

with open("input.txt") as inp:
	for line in inp:
		line = line.strip()
		try:
			score += wins[line]
		except KeyError:
			try:
				score += draws[line]
			except KeyError:
				score += points[line.split(" ")[1]]
print(score)

"""

### 2

dic = {
		"X":{"A":3, "B": 1, "C":2},
		"Y":{"A":4, "B": 5, "C": 6},
		"Z":{"A":8, "B": 9, "C": 7}

}

score = 0

with open("input.txt") as inp:
	for line in inp:
		line = line.strip().split(" ")
		score += dic[line[1]][line[0]]
print(score)