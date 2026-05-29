import random, json
with open('items.json', 'r', encoding='utf-8') as file:
    items = json.load(file)
with open('workstrings.json', 'r', encoding='utf-8') as file:
    workstrings = json.load(file)

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
        print(f"You have {self.balance} coins!")
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
                    print("You have no armor in your inventory!")
                    break
            break

                

                    
    def work(self):
        payment=self.balance+random.randint(1,20)
        self.balance=payment
        stringsel = random.randint(1, 10)
        print(workstrings[stringsel]['text'])
        print(f"You now have {payment}")
class Gambler:
    def Roulette(self):
        


pName = input("What do you want the player's name to be?\n*Stats will be randomized\n- ")
#               name,  health, strength,               defense                 hunger          inventory balance
player = Player(pName, 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), ['Glock', 'Twig'], 5)

run = True
while run:        
    john = Player("john", 100, random.randint(1, 10), random.randint(1, 10), random.randint(5, 10), ['Glock'], 5)
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
    