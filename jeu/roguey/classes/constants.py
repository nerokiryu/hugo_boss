from os.path import abspath, dirname, join, sep

TREASURES = 10

TILE_SIZE = 48


EQUIPMENT_TYPES = ('hat', 'shirt', 'pants', 'shoes', 'back', 'neck', 'hands', 'weapon')
START_EQUIPMENT = {}
for treasure in EQUIPMENT_TYPES:
	START_EQUIPMENT[treasure] = None

TREASURE_TYPES = ('hat', 'shirt', 'pants', 'shoes', 'back', 'neck', 'hands', 'weapon', 'trash')


STATS = ('strength', 'attack', 'defense')
