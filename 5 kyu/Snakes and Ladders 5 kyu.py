# https://www.codewars.com/kata/587136ba2eefcb92a9000027/train/python


class SnakesLadders():
	def __init__(self):
		self.p1 = 0
		self.p2 = 0
		self.holes = {2: 38, 7: 14, 8: 31, 15: 26, 16: 6, 21: 42, 
                      28: 84, 36: 44, 46: 25, 49: 11, 51: 67, 62: 19, 
                      64: 60, 71: 91, 74: 53, 78: 98, 87: 94, 89: 68, 
                      92: 88, 95: 75, 99: 80}
		self.turn = 0
	def play(self, d1, d2):
		if any(s == 100 for s in (self.p1, self.p2)):
			return "Game over!"
		p = self.turn % 2
		pos = (self.p1, self.p2)[p]
		total, con = d1 + d2, d1 != d2
		pos += total
		pos = pos if pos <= 100 else 100 - (pos - 100)
		pos = self.holes.get(pos, pos)
		if p == 0: self.p1 = pos
		else: self.p2 = pos
		self.turn += 1 * con
		if pos == 100:
			return "Player {} Wins!".format(p + 1)
		return "Player {} is on square {}".format(p + 1, pos)
