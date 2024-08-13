################################
# Player Class:
################################


from Hand import Hand
class Player(object):
	def __init__(self, name, hand):
		self.name = name
		self.hand = Hand(hand)
		self.score = 0

	def increaseScore(self):
		self.score = self.score + 1