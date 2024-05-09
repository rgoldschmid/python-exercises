from Classes.Pokemon import Pokemon
from Classes.Battle import Battle

"""
Pokemon Test
"""

pikachu = Pokemon('Pikachu', 'Electric', 100, {'Thunder Shock': 40, 'Tackle': 20})

damage = pikachu.perform_attack('Thunder Shock')
print(f'Pikachu deals {damage} points of damage with Thunder Shock.')

print(pikachu)
pikachu.receive_damage(30)
print(pikachu)

"""
Battle Time!
"""

charizard = Pokemon('Charizard', 'Fire', 150, {'Flamethrower': 60, 'Fire Spin': 40})
blastoise = Pokemon('Blastoise', 'Water', 160, {'Water Gun': 50, 'Hydro Pump': 70})

battle = Battle(charizard, blastoise)

print(battle)
result = battle.fight()
print(result)
