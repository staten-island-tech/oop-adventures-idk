import random
items = [
    {
        "id": 1,
        "name": "Twig",
        "atk": 5,  
        "type": "weapon",
        "cost": 6,
    },
    {
        "id": 2,
        "name": "Glock",
        "atk": 10,
        "type": "weapon",
        "cost": 10,
    },
    {
        "id": 3,
        "name": "Textbook Troika",
        "atk": 20,
        "type": "weapon",
        "cost": 20,
    },
    {
        "id": 4, 
        "name": "Duck",
        "def": 10,
        "type": "armor",
        "cost": 10,

    },
    {
        "id": 5, 
        "name": "Car",
        "def": 20,
        "type": "armor",
        "cost": 15,
    },
    {
        "id": 6, 
        "name": "Excalibur",
        "atk": 1,
        "type": "weapon",
        "cost": 100,
    },
    {
        "id": 7, 
        "name": "Impenetrable Armor",
        "def": 1,
        "type": "armor"
        "cost": 100,
    },
    {
        "id": 8, 
        "name": "Pebble",
        "atk": 25,
        "type": "weapon",
<<<<<<< HEAD
        "cost": 20,
=======
>>>>>>> 21a7bc32630b432e4a13ec26ee330a0b882008f1
    },
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
        type=input("Would you like to use a weapon? [yes/no]\n- ").lower()
        if type=="yes":
            print("Weapons:")
            for i in self.inventory:
                print(f"{i.index(i)+1}. {i}")
        #opponent.health-=x
<<<<<<< HEAD
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} is DEAD.")
        elif opponent.health > 0:
            print(f"Attack successful, {opponent.name} lost {self.inventory["atk"]} health.")
    def marketbuy(self, items):
        for i in range(len(items)):
            print(items[i]["name"])

=======
        for self.inventory in items:
            if self.inventory == items[i]["name"]:
                if opponent.health <= 0:
                    opponent.health = 0
                    print(f"{opponent.name} is DEAD.")
                elif opponent.health > 0:
                    print(f"Attack successful, {opponent.name} lost {self.inventory["atk"]} health.")
>>>>>>> 21a7bc32630b432e4a13ec26ee330a0b882008f1

pName = input("What do you want the player's name to be?\n*Stats will be randomized\n- ")
#               name,  health, strength,               defense                 hunger          inventory balance
player = Player(pName, 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), ['Glock'], 5)

player.checkStats()
john = Player("john", 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), ['Glock'], 5)
player.fight(john, ['glock'])