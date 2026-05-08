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
        type=input("Would you like to use a weapon? yes/no").lower()
        if type=="yes":
            print("Weapons:")
            for i in self.inventory:
                print(f"{i.index(i)+1}. {i}")
        #opponent.health-=x
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} is DEAD.")
        elif opponent.health > 0:
            print(f"Attack successful, {opponent.name} lost {self.inventory["atk"]} health.")

pName = input("What do you want the player's name to be?\n*Stats will be randomized\n- ")
#               name,  health, strength,               defense                 hunger          inventory balance
player = Player(pName, 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), ['glock'], 5)

player.checkStats()
john = Player("john", 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), ['glock'], 5)
player.fight(john, ['glock'])