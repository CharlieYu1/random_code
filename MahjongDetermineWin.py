import collections
import itertools


def powerset(iterable):
	s = list(iterable)
	return itertools.chain.from_iterable(itertools.combinations(s,r) for r in range(len(s) + 1))

def hand_to_counter(hand):
	if type(hand) is str:
		return collections.Counter(map(int, hand))
	else:
		return hand
		
def check_sequences(hand):
	hand = hand_to_counter(hand)
	sequences = []
	if sum(hand.values()) % 3 != 0:
		return False
	while sum(hand.values()):
		m = min(hand)
		if m + 1 not in hand or m + 2 not in hand:
			return False
		hand -= collections.Counter((m, m + 1, m + 2))
		sequences.append(str(m) + str(m + 1) + str(m + 2))
	return sequences

def check_3k_hand(hand):
	hand = hand_to_counter(hand)
	if sum(hand.values()) % 3 != 0:
		return []
	complete_combos = []
	possible_triplets = [tile for tile in hand if hand[tile] >=3]
	for triplets in powerset(possible_triplets):
		remainding_hand = hand - collections.Counter(triplets + triplets + triplets)
		remainding_sequences = check_sequences(remainding_hand)
		if remainding_sequences is not False:
			complete_hand = [str(tile) * 3 for tile in triplets]
			complete_hand.extend(remainding_sequences)
			complete_combos.append(complete_hand)
	return complete_combos
	
def check_3k_2_hand(hand):
	hand = hand_to_counter(hand)
	if sum(hand.values()) % 3 != 2:
		return []
	complete_combos = []
	sum_value = sum(tile * hand[tile] for tile in hand)
	possible_pairs = {0:[3, 6, 9], 1:[2, 5, 8], 2:[1, 4, 7]}[sum_value % 3]
	for possible_pair in possible_pairs:
		if hand[possible_pair] >= 2:
			remaining_hand = hand - collections.Counter((possible_pair, possible_pair))
			if sum(remaining_hand.values()) == 0:
				complete_combos.append(str(possible_pair) * 2)  # corner case for only 2 tiles
			remaining_combos = check_3k_hand(remaining_hand)
			if remaining_combos:
				complete_combos.extend([[str(possible_pair) * 2] + remaining_combo for 														remaining_combo in remaining_combos])
	return complete_combos
