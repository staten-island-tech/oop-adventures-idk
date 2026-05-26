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
        "hp": 20,
        "type": "armor",
        "cost": 15,
    },
    {
        "id": 6, 
        "name": "Excalibur",
        "atk": 1,
        "type": "weapon",
        "cost": 1000,
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
        print(" -- PLAYER STATS -- ")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Defense: {self.defense}")
        print(f"Hunger: {self.hunger}")
        print(f"Inventory: {self.inventory}")
        print(f"Balance: {self.balance}")
    def fight(self, opponent):
        print("What weapon would you like to use?:")
        for i, name in enumerate(self.inventory):
            print(f"{i+1}. {name}")
        typee=input("- ").lower()
        for name in items:
            for i in range(len(self.inventory)):
                if name["name"] == self.inventory[i] and self.inventory[i] == typee.capitalize():
                    opponent.health = opponent.health - name['atk']
                    if opponent.health <= 0:
                        opponent.health = 0
                        print(f"{opponent.name} is DEAD.")
                    elif opponent.health > 0:
                        print(f"- Attack successful, {opponent.name} lost {name["atk"]} health.")
                        print(f"{self.name}'s HP: {self.health}")
                        print(f"{opponent.name}'s HP: {opponent.health}")
    def shop(self):
        print(f"What would you like to buy?\nMenu: ")
        for i in range(len(items)):
            print(f" *{items[i]["name"]}")
        ask = input("- ")
        for i in range(len(items)):
            if ask==items[i]["name"]:
                Result=self.balance-items[i]["cost"]
                if Result>0:
                    self.balance=Result
                    self.inventory.append(items[i]["name"])
                    print(self.inventory)
                    print(f"You have successfully bought the item! You have {self.balance} coins left!")
                elif Result<0:
                    print("Insufficient funds!")
                
    def armorequip(self):
        while 1:
            for i in self.inventory:
                if i=="Car":
                    Car=input("Would you like to equip 'Car'?").lower()
                    if Car=="yes":
                        self.health=120
                        print(f"You have {self.health} health now!")
                        break
                elif i=="Duck":
                    Duck=input("Would you like to equip 'Duck'").lower()
                    if Duck=="yes":
                        self.health=110
                        print(f"You have {self.health} health now!")
                        break
                elif i=="Impenetrable Armor":
                    Impenarmor=input("Would you like to equip 'Impenetrable Armor'").lower()
                    if Impenarmor=="yes":
                        self.health=101
                        print(f"You have {self.health} health now!")
                        break
                elif "Impenetrable Armor" not in self.inventory and "Car" not in self.inventory and "Duck" not in self.inventory:
                    print("not in")
                    break
            break

                
    def work(self):
        jon=self.balance+random.randint(1,10)
        self.balance=jon
        if jon%10==0:
            print("You hijack a plane by accident and got paid by the local terrorist organization")
        elif jon%9==0:
            print("You pretend to be injured after a car nearly hit you and take the driver the court.")
        elif jon%8==0:
            print("You accidentally join a cult and reported them to the police, who give you an reward")
        elif jon%7==0:
            print("You robbed a single mother with a family of 6")
        elif jon%6==0:
            print("You fake your death and collect your insurance money!")
        elif jon%5==0:
            print("You have a 25 hour shift working at the local McDonalds")
        elif jon%4==0:
            print("You open open up a can of beans and you find money inside")
        elif jon%3==0:
            print("You fake being a cancer survivor for pity money")
        elif jon%2==0:
            print("You hijack someones device and transfer their money into your bank account")
        elif jon%1==0:
            print("You work very very very very very very very very very very very very hardddddddddddddddddddd")
        


pName = input("What do you want the player's name to be?\n*Stats will be randomized\n- ")
#               name,  health, strength,               defense                 hunger          inventory balance
player = Player(pName, 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), ['Glock', 'Twig'], 5, 0)

run = True
while run:        
    john = Player("john", 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), ['Glock'], 5, 0)
    print(" - What would you like to do?:")
    print("[1] - Check Stats")
    print("[2] - Fight")
    print("[3] - Quit")
    print("[4] - Shop")
    print("[5] - Armory")
    print("[6] - Work")
    option = input("- ")
    if option.lower() == "check stats" or int(option) == 1:
        player.checkStats()
    elif option.lower() == "fight" or int(option) == 2:    
        player.fight(john)
    elif option.lower() == "shop" or int(option) == 4:
        player.shop()
    elif option.lower() == "armory" or int(option) == 5:
        player.armorequip()
    elif option.lower() == "work" or int(option) == 6:
        player.work()
    elif option.lower() == "quit" or int(option) == 3:
        run = False
    