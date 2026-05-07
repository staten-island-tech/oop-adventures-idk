import random
items = [
    {
        "id": 1,
        "name": "twig",
        "atk": 5,
        "type": "weapon",
    },
    {
        "id": 2,
        "name": "glock",
        "atk": 10,
        "type": "weapon",
    }
]

class Player:
    def __init__(self, name, health, strength, defense, hunger, inventory, balance):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.hunger = hunger
        self.inventory = inventory
        self.balance = balance
    def checkStats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Defense: {self.defense}")
        print(f"Hunger: {self.hunger}")
        print(f"Inventory: {self.inventory}")
    def fight(self, opponent,item):
        type=input("Would you like to use your weapon? yes/no").lower()
        if type=="yes":
            for i in range(self.inventory):
                print(self.inventory[i]["name"])
        opponent.health-=x
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} is DEAD.")
        elif opponent.health > 0:
            print(f"Attack successful, {opponent.name} lost {self.inventory["atk"]} health.")

pName = input("What do you want the player's name to be?\n*Stats will be randomized\n- ")

player = Player(pName, 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), 5, ['glock'] )

player.checkStats()