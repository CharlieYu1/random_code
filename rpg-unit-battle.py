import enum

class Unit (object):
	
	class unit_types(enum.Enum):
		Knight = 1
		Soldier = 2
		Archer = 3
		
	def __init__(self, unit_type, level, **kwargs):
		self.unit_type = unit_type
		self.level = level
		self.attack = level * 10
		self.HP = level * 100
		
	@staticmethod
	def attack_bonus(self_type, other_type):
		return [[1, 2, 0.5], [2, 1, 0.5], [0.5, 2, 1]][self_type.value - 1][other_type.value - 1]
		
A = Unit(Unit.unit_types.Knight, 15)
B = Unit(Unit.unit_types.Soldier, 11)
