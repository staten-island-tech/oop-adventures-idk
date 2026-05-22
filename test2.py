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
        h=0
        while self.armorquip==0 and h==0:
            for i in self.inventory:
                if i=="Car":
                    Car=input("Would you like to equip 'Car'?").lower()
                    if Car=="yes":
                        self.hp=120
                        self.armorquip=1
                        print(f"You have {self.hp} health now!")
                        cc=1
                elif i=="Duck":
                    Duck=input("Would you like to equip 'Duck'").lower()
                    if Duck=="yes":
                        self.hp=110
                        self.armorquip=1
                        print(f"You have {self.hp} health now!")
                elif i=="Impenetrable Armor":
                    Impenarmor=input("Would you like to equip 'Impenetrable Armor'").lower()
                    if Impenarmor=="yes":
                        self.hp=101
                        self.armorquip=1
                        print(f"You have {self.hp} health now!")

                    
                        


pName = input("What do you want the player's name to be?\n*Stats will be randomized\n- ")
#               name,  health, strength,               defense                 hunger          inventory balance
player = Player(pName, 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), ['Glock', 'Duck', 'Car'], 5000, 0) 
john = Player("john", 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), ['Glock'], 5, 0)

player.armorequip()