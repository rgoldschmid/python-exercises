class Pokemon:
    def __init__(self, name: str, element: str, hp: int, attack: dict):
        self.name = name
        self.element = element
        self.hp = hp
        self.attacks = attack

    def perform_attack(self, attack_name: str) -> int:
        if attack_name in self.attacks:
            return self.attacks[attack_name]
        else:
            return 0  # No damage if the attack is not found

    def receive_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0  # Ensure HP does not go negative

    def __str__(self):
        return f"{self.name} ({self.element}) - HP: {self.hp}"
