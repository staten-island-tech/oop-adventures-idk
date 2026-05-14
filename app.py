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
        "hp": 10,
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
        "hp": 1,
        "type": "armor",
        "cost": 100,
    },
    {
        "id": 8, 
        "name": "Pebble",
        "atk": 25,
        "type": "weapon",
        "cost": 20,
    },
]

class Player:
    def __init__(self, name, health, strength, defense, hunger, inventory, balance, armorquip):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.hunger = hunger
        self.inventory = inventory
        self.balance = balance
        self.armorquip=armorquip
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
    def shop(self):
        ask=input(f"What would you like to buy{items}")
        for i in range(len(items)):
            if ask==items[i]["name"]:
                Result=self.balance-items[i]["cost"]
                if Result>0:
                    self.balance=Result
                    self.inventory.append(items[i])
                    print(self.inventory)
                    print(f"You have {self.balance} coins left!")
                elif Result<0:
                    print("insufficient funds!")
    def armorequip(self):
        if self.armorquip==0:
            for i in self.inventory:
                armorr=input(self.inventory[i]["type"]["armor"]["name"])
                if armorr==self.inventory[i]["type"]["armor"]["name"]:
                    print("Armor successfully equipped!")
                    ovl=self.hp+self.inventory[i]["type"]["armor"]["hp"]
                    self.hp=ovl
                    self.armorquip=self.inventory[i]["type"]["armor"]["hp"]
            else:
                print("You have no armor!")
        elif self.armorquip==1:
            input("You have ")

pName = input("What do you want the player's name to be?\n*Stats will be randomized\n- ")
#               name,  health, strength,               defense                 hunger          inventory balance
player = Player(pName, 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), ['Glock'], 5, 0)

player.checkStats()
john = Player("john", 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), ['Glock'], 5, 0)
player.fight(john, ['glock'])