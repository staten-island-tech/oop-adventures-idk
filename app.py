import random
items = [
    {
        "id": 1,
        "name": "Twig",
        "atk": 5,  
        "type": "weapon",
    },
    {
        "id": 2,
        "name": "Glock",
        "atk": 10,
        "type": "weapon",
    },
    {
        "id": 3,
        "name": "Textbook Troika",
        "atk": 20,
        "type": "weapon",
    },
    {
        "id": 4, 
        "name": "Helmet",
        "def": 10,
        "type": "armor",
    },
    {
        "id": 5, 
        "name": "Chestplate",
        "def": 20,
        "type": "armor",
    },
    {
        "id": 6, 
        "name": "Leggings",
        "def": 10,
        "type": "armor",
    },
    {
        "id": 7, 
        "name": "Excalibur",
        "atk": 1,
        "type": "weapon",
    },
    {
        "id": 8, 
        "name": "Impenetrable Armor",
        "def": 1,
        "type": "armor"
    },
    {
        "id": 9, 
        "name": "Pebble",
        "atk": 25,
        "type": "weapon",
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
        for name in items:
            if self.inventory == items[i]["name"]:
                if opponent.health <= 0:
                    opponent.health = 0
                    print(f"{opponent.name} is DEAD.")
                elif opponent.health > 0:
                    print(f"Attack successful, {opponent.name} lost {self.inventory["atk"]} health.")

pName = input("What do you want the player's name to be?\n*Stats will be randomized\n- ")
#               name,  health, strength,               defense                 hunger          inventory balance
player = Player(pName, 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), ['Glock'], 5)

player.checkStats()
john = Player("john", 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), ['Glock'], 5)
player.fight(john, ['glock'])