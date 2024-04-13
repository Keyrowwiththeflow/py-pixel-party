import random as rnd

chest = ['Loot1', 'Loot2']
magic_chest = [{'name':'Stone', 'power':5, 'rarity': 'common'}, {'name':'Stick', 'power':3, 'rarity': 'common'},                {'name':'Sword', 'power':20, 'rarity': 'rare'}]

randomPlace = rnd.randint(0,len(magic_chest)-1)
loot = magic_chest[randomPlace]
print(f"You found a {loot['rarity']} {loot['name']} with a power rating of {loot['power']}!")