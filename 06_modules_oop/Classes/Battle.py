import random


class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def fight(self):
        attacker = self.pokemon1
        defender = self.pokemon2

        while self.pokemon1.hp > 0 and self.pokemon2.hp > 0:
            attack_name = random.choice(list(attacker.attacks.keys()))
            damage = attacker.perform_attack(attack_name)
            defender.receive_damage(damage)

            print(f"{attacker.name} uses {attack_name}! {defender.name} receives {damage} damage.")

            if defender.hp <= 0:
                print(f"{defender.name} has fainted!")
                return f"{attacker.name} wins!"

            attacker, defender = defender, attacker

        return "It's a draw!"

    def __str__(self):
        return f"{self.pokemon1}\nvs.\n{self.pokemon2}"
