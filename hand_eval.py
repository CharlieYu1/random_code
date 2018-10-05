import enum
import itertools

# a shelve to map from rank5 objects to hand description for fast lookup
rank5_map = dict()

class HandType(enum.IntEnum):
	# poker hand rankings by type
	HIGH_CARD, PAIR, TWOPAIRS, TRIPS, STRAIGHT, FLUSH, FULL_HOUSE, QUADS, STRAIGHT_FLUSH, ROYAL_FLUSH = range(10)

class Rank(enum.IntEnum):
	TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE = range(13)


def nCr(n, r):
	result = 1
	for i in range(n, n-r, -1):
		result *= i
	for i in range(1, r+1):
		result //= i
	return result

def nHr (n, r):
	return nCr(n+r-1, r)
	
def rank5_code(rank5):
	'''take a rank5 object and return a unique code in range(6188)'''
	'''where there are a total of 6188 unique hands including'''
	'''5 of a kind'''
	if len(rank5) != 5: #only allow 5 card hands
		raise NotImplementedError
	_rank5 = sorted(rank5[:], key=lambda x:x.value)
	return sum(nHr(rank.value, i+1) for i, rank in enumerate(_rank5))
	
# add hands for rank5_map

# add quads
rank5_map.update({rank5_code((r, r, r, r, s)): (HandType.QUADS, r, s) \
									for r in Rank for s in Rank if r!=s})
									
# add full_houses
rank5_map.update({rank5_code((r, r, r, s, s)): (HandType.FULL_HOUSE, \
									r, s) for r in Rank for s in Rank if r!=s})


# add trips, rank trips kickers by reverse order
rank5_map.update({rank5_code((r, r, r, s, t)): (HandType.TRIPS, \
									r, t, s) for r in Rank for s, t in itertools.combinations(Rank, 2) if r not in (s, t)})
									
# add two pairs
rank5_map.update({rank5_code((r, r, s, s, t)): (HandType.TWOPAIRS, \
									s, r, t) for r, s in itertools.combinations(Rank, 2) for t in Rank if t not in (r, s)})
									
# add one pair
rank5_map.update({rank5_code((r, r, s, t, u)): (HandType.PAIR, \
									r, u, t, s) for s, t, u in itertools.combinations(Rank, 3) for r in Rank if r not in (s, t, u)})
									
# add high card
rank5_map.update({rank5_code((r, s, t, u, v)): (HandType.HIGH_CARD, \
									v, u, t, s, r) for r, s, t, u, v in itertools.combinations(Rank, 5)})
									
# add straight, rank by highest card
for i in range(9):
	# temp hand variable for a 5 card straight
	_hand = *(Rank(i+j) for j in range(5)),
	rank5_map[rank5_code(_hand)] = (HandType.STRAIGHT, Rank(i+4))
#A2345
_hand = *(Rank(j) for j in range(4)), Rank(12)
rank5_map[_hand] = (HandType.STRAIGHT, Rank(3))

