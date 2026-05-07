import random

class Player:
    def __init__(self, name, health, strength, defense, hunger, inventory):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.hunger = hunger
        self.inventory = inventory
    def checkStats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Defense: {self.defense}")
        print(f"Hunger: {self.hunger}")
        print(f"Inventory: {self.inventory}")
pName = input("What do you want the player's name to be?\n*Stats will be randomized\n- ")

player = Player(pName, 100, random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), ['empty'] )

player.checkStats()