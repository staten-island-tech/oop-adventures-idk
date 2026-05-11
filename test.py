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
        "name": "Duck",
        "def": 10,
        "type": "armor",
    },
    {
        "id": 5, 
        "name": "Car",
        "def": 20,
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
    def work(self):
        for i in range(5):
            print(f"Items in the shop:{items[random.randint(0,7)]["name"]}")
        askbuy=input("Would you like to buy anything from the shop?\n*type the name of the item you want\n-")
pName = input("What do you want the player's name to be?\n*Stats will be randomized\n- ")
player = Player(pName, 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), ['Glock'], 5)
john = Player("john", 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), ['Glock'], 5)
player.work()