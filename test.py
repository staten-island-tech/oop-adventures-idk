import random
class Player:
    def __init__(self, name, health, strength, hunger, inventory, balance):
        self.name = name
        self.health = health
        self.strength = strength
        self.hunger = hunger
        self.inventory = inventory
        self.balance = balance
player = Player("pName", 1, random.randint(1, 10), random.randint(50, 100), ['Glock', 'Twig'], 5)
print(player.health())