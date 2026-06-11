import random, json
with open('items.json', 'r', encoding='utf-8') as file:
    items = json.load(file)
with open('workstrings.json', 'r', encoding='utf-8') as file:
    workstrings = json.load(file)

class Player:
    def __init__(self, name, health, strength, hunger, inventory, balance):
        self.name = name
        self.health = health
        self.strength = strength
        self.hunger = hunger
        self.inventory = inventory
        self.balance = balance
    def checkStats(self):
        print(" -- PLAYER STATS -- ")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Hunger: {self.hunger}")
        print(f"Inventory: {self.inventory}")
        print(f"Balance: {self.balance}")
    def fight(self, opponent):
        print("What weapon would you like to use?(type weapon name):")
        for i, name in enumerate(self.inventory):
            print(f"{i+1}. {name}")
        typee=input("- ").lower()
        while opponent.health>0 and self.health>0:
            for name in items:
                for i in range(len(self.inventory)):
                    if name["name"] == self.inventory[i] and self.inventory[i] == typee.capitalize():
                        opponent.health = opponent.health - name['atk']
                        self.health -= opponent.damage
                        hungerloss=random.randint(1, 5)
                        self.hunger -= hungerloss   
                        if opponent.health <= 0:
                            opponent.health = 0
                            print(f"{opponent.name} is DEAD.")
                            dropdecider=random.randint(1,4)
                            itemdecider= random.randint(0,8)
                            itemdecided=items[itemdecider]
                            if dropdecider==1:
                                print(f"You got a drop from defeating {opponent.name}")
                                self.inventory.append(itemdecided)
                        elif self.health <= 0:
                            self.health = 0
                            print(f"{opponent.name} is DEAD.")
                        elif opponent.health > 0:
                            print(f"- Attack successful, {opponent.name} lost {name["atk"]} health.")
                            print(f"You took {opponent.damage} damage! You have {self.health} health left!")
                            print(f"{self.name}'s HP: {self.health}")
                            print(f"{opponent.name}'s HP: {opponent.health}")
                            fightr=input("Would you like to attack again?").lower()
                            if fightr=="no": 
                                break
                            
    def shop(self):
        print(f"What would you like to buy?\nMenu: ")
        print(f"You have {self.balance} coins!")
        for i in range(len(items)):
            print(f" *{items[i]["name"]} --- {items[i]["cost"]} coins")
        ask = input("- ")
        for i in range(len(items)):
            if ask==items[i]["name"]:
                Result=self.balance-items[i]["cost"]
                if Result>0:
                    self.balance=Result
                    self.inventory.append(items[i]['name'])
                    print(self.inventory)
                    print(f"You have successfully bought the item! You have {self.balance} coins left!")
                elif Result<0:
                    print("Insufficient funds!")
    def armorequip(self):
        while True:
            for i in self.inventory:
                if i=="Car":
                    Car=input("Would you like to equip 'Car'?").lower()
                    if Car=="yes":
                        self.health=120
                        print(f"You have {self.health} health now!")
                elif i=="Duck":
                    Duck=input("Would you like to equip 'Duck'").lower()
                    if Duck=="yes":
                        self.health=110
                        print(f"You have {self.health} health now!")
                elif i=="Impenetrable Armor":
                    Impenarmor=input("Would you like to equip 'Impenetrable Armor'").lower()
                    if Impenarmor=="yes":
                        self.health=101
                        print(f"You have {self.health} health now!")
                elif "Impenetrable Armor" not in self.inventory and "Car" not in self.inventory and "Duck" not in self.inventory:
                    print("You have no armor in your inventory!")
                    break
            break
    def hunt(self):
        if "Hunting Knife" not in self.inventory:
            print("Go get a hunting knife!")
        else: 
                huntingchance=random.randint(1,4)
                if huntingchance==1:
                    print("You encountered a rabbit!")
                    while rabbit.health!=0 or self.health<=0:
                        attack=input("Would you like to attack?").lower()
                        if attack=="yes":
                            rabbit.takedamage(5)
                            self.takedamage(rabbit.damage)
                        else: 
                            print("ok")
                            break
                        if rabbit.health==0:
                            print("You have successfully skewered the rabbit")
                            self.inventory.append(rabbit.drop)
                            rabbit.health=10
                        elif self.health<=0:
                            print("Your character died")
                            run=False

                elif huntingchance==2:
                    print("You encountered a buffalo!")
                    while buffalo.health!=0 or self.health<=0:
                            attack=input("Would you like to attack?").lower()
                            if attack=="yes":
                                buffalo.takedamage(5)
                                self.takedamage(buffalo.damage)
                            else: 
                                print("ok")
                                break
                    if buffalo.health==0:
                            print("it died.")
                            self.inventory.append(buffalo.drop)
                            buffalo.health=20
                    elif self.health<=0:
                            print("Your character died")
                            run=False
                elif huntingchance==3:
                    print("You enounter a frog!")
                    while frog.health!=0 or self.health<=0:
                            attack=input("Would you like to attack?").lower()
                            if attack=="yes":
                                frog.takedamage(5)
                                self.takedamage(frog.damage)
                            else: 
                                print("ok")
                                break
                    if frog.health==0:
                            print("Congrats! You murdered the frog!")
                            self.inventory.append(frog.drop)
                            frog.health=15
                    elif self.health<=0:
                            print("Your character died!")
                            run=False
                elif huntingchance==4:
                    print("You found nothing!")
    def takedamage(self, amount):
        self.health-=amount
        print(f"Your player has {self.health} health left")           
    def work(self):
        payment=self.balance+random.randint(1,20)
        self.balance=payment
        stringsel = random.randint(0, 9)
        print(workstrings[stringsel]['text'])
        print(f"You now have {payment}")

class Animal:
    def __init__(self, health, damage, drop):
        self.health=health
        self.damage=damage
        self.drop=drop
    def takedamage(self, amount):
        self.health-=amount
        print(f"The animal has {self.health} health left")
            
class NPC:
    def __init__(self, name, health, damage):
        self.health=health
        self.name=name
        self.damage=damage
    def fixhealth(self):
        if self.name=="Rud":
            self.health=10
        elif self.name=="Hut":
            self.health=50
        elif self.name=="john":
            self.health=100
#heree


        


pName = input("What do you want the player's name to be?\n*Stats will be randomized\n- ")
#               name,  health, strength,                                hunger          inventory balance
player = Player(pName, 1, random.randint(1, 10), random.randint(50, 100), ['Glock', 'Twig'], 5)
run = True
while run:        
    john = NPC("john", 100, 4)
    Hut= NPC("Hut", 50, 2)
    Rud= NPC("Rud", 10, 15)
    rabbit= Animal(10, 1, "rabbit")
    buffalo=Animal(20, 2, "beef")
    frog=Animal(15, 1, "raw meat")
    print(" - What would you like to do?:")
    print("[1] - Check Stats")
    print("[2] - Fight")
    print("[3] - Quit")
    print("[4] - Shop")
    print("[5] - Armory")
    print("[6] - Work")
    print("[7] - Hunt")
    option = input("- ")
    if option.lower() == "check stats" or int(option) == 1:
        player.checkStats()
    elif int(option) == 2:    
        fii=input("Who would you like to fight: John, Hut, or Rud").lower()
        if fii=="john":
            john.fixhealth()
            player.fight(john)
        elif fii=="hut":
            Hut.fixhealth
            player.fight(Hut)
        elif fii=="rud":
            Rud.fixhealth
            player.fight(Rud)
    elif int(option) == 4:
        player.shop()
    elif int(option) == 5:
        player.armorequip()
    elif int(option) == 6:
        player.work()
    elif int(option)== 7:
        player.hunt()
    elif int(option) == 3:
        run = False
    