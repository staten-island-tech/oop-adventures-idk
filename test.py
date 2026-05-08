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
    def fight(self):
        type=input("Would you like to use your weapon? yes/no").lower()
        if type=="yes":
            whatweapon=input("What weapon would you like to use?")
            for i in range(self.inventory):
                if self.inventory[i]["type"]=="weapon":
                    print(self.inventory[i]["name"])
                    if whatweapon==self.inventory[i]["name"]:
                        x=self.inventory[i]["atk"]
                        print(x)

pName = input("What do you want the player's name to be?\n*Stats will be randomized\n- ")

player = Player(pName, 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), ['glock'], 5 )

player.checkStats()
player.fight()