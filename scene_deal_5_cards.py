from scene import *
import sound
import random
import math
A = Action

class MyScene (Scene):
	def setup(self):
		self.background_color = '#342d59'
		self.card = []
		self.deck = Deck()
		for i in range(5):
			new_card = self.deck.deal_card()
			self.card.append(SpriteNode(new_card.img))
			self.card[i].card = new_card
			self.card[i].position = self.size.w / 2 + (i - 2) * 150, self.size.h * 0.5
			self.card[i].alpha = 0.0
			self.card[i].run_action(A.fade_to(1, 1))
			self.add_child(self.card[i])
		label_font = ('Futura', 40)
		self.label = LabelNode("scene with 5 cards", label_font, parent = self)
		self.label.position = self.size.w / 2, self.size.h / 2 + 200
		self.label.z_position = 1
		self.button = ShapeNode(Rect(self.size.w/2 - 100, self.size.h/2 - 200,200, 100))
	
	def did_change_size(self):
		pass
	
	def update(self):
		pass
	
	def touch_began(self, touch):
		touch_x, touch_y = touch.location
		self.check_touched_card(touch_x, touch_y)
		
		
	def check_touched_card(self, x, y):
		for card in self.card:
			if card.bbox.contains_point((x, y)):
				# replace the touched card
				new_card = self.deck.deal_card()
				card.card = new_card
				card.texture = Texture(new_card.img)
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass


class Deck:
	RANKS = '23456789TJQKA'
	SUITS = 'cdhs'
	SUITS_FULL = {'c': 'Clubs', 'd': 'Diamonds', 'h': 'Hearts', 's': 'Spades'}
	
	def __init__(self, **kwargs):
		self.deck = [Card(r+s) for r in self.RANKS for s in self.SUITS]
		if 'seed' in kwargs:
			random.seed(kwargs['seed'])
		random.shuffle(self.deck)
		self.num_remainding_cards = 52
		
	def __repr__(self):
		return "['{}']".format("', '".join(map(repr, self.deck)))
		
	def deal_card(self):
		self.num_remainding_cards -= 1
		return(self.deck.pop())
	
	def reset():
		self.__init__()
	
	
class Card:
	RANKS = '23456789TJQKA'
	SUITS = 'cdhs'
	SUITS_FULL = {'c': 'Clubs', 'd': 'Diamonds', 'h': 'Hearts', 's': 'Spades'}
	
	def __init__(self, *args):
		if len(args) == 1:  # rank and suit defined by two characters
			self.rank = args[0][0]
			self.suit = args[0][1]
			self.img = 'card:{}{}'.format(self.SUITS_FULL[self.suit], self.rank)
			if self.img[-1] == 'T':
				self.img = self.img[:-1] + '10'
		
	def __repr__(self):
		return self.rank + self.suit
		
if __name__ == '__main__':
	run(MyScene(), show_fps=False)
