import random, json
with open('items.json', 'r', encoding='utf-8') as file:
    items = json.load(file)
with open('workstrings.json', 'r', encoding='utf-8') as file:
    workstrings = json.load(file)

class Player:
    def __init__(self, name, health, strength, hunger, inventory, balance, rebirth, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.hunger = hunger
        self.inventory = inventory
        self.balance = balance
        self.rebirth= rebirth
        self.defense=defense
    def checkStats(self):
        print(" -- PLAYER STATS -- ")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Hunger: {self.hunger}")
        print(f"Inventory: {self.inventory}")
        print(f"Balance: {self.balance}")
        print(f"Defense: {self.defense}")
        print(f"Rebirths: {self.rebirth}")
    def fight(self, opponent):
        print("What weapon would you like to use?(type weapon name):")
        for i, name in enumerate(self.inventory):
            print(f"{i+1}. {name}")
        typee=input("- ").lower()

        while opponent.health>0 and self.health>0:
            for name in items:
                for i in range(len(self.inventory)):
                    if name["name"] == self.inventory[i] and self.inventory[i] == typee.capitalize():
                        opponent.health = opponent.health - name['atk']*self.strength
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
                            print(f"{self.name} is DEAD.")
                        elif opponent.health > 0:
                            print(f"- Attack successful, {opponent.name} lost {name["atk"]*self.strength} health.")
                            self.health=round(self.health-(opponent.damage*self.defense))
                            print(f"Your opponent attacks and you took {round(opponent.damage*self.defense)} damage! You have {self.health} health left!")
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
                    Car=input("Would you like to equip 'Car'? If you want other options type no\n- ").lower()
                    if Car=="yes":
                        self.defense=items[4]["def"]*self.defense
                        print(f"You take 3% less damage now!")
                        self.inventory.remove("Car")
                elif i=="Duck":
                    Duck=input("Would you like to equip 'Duck' If you want other options type no\n- ").lower()
                    if Duck=="yes":
                        self.defense=items[3]["def"]*self.defense
                        print(f"You take 2% less damage now!")
                        self.inventory.remove("Duck")
                elif i=="Impenetrable Armor":
                    Impenarmor=input("Would you like to equip 'Impenetrable Armor'?\n- ").lower()
                    if Impenarmor=="yes":
                        self.defense=items[6]["def"]*self.defense
                        print(f"You take 10% less damage now!")
                        self.inventory.remove("Impenetrable Armor")
                elif "Impenetrable Armor" not in self.inventory and "Duck" not in self.inventory and "Car" not in self.inventory:
                    print("You have no armor in your inventory!")
                    break
            break
    def hunt(self):
        if "Hunting Knife" not in self.inventory:
            print("You enter a forest not knowing you didn't have a hunting knife! Go get a hunting knife!")
        else: 
                huntingchance=random.randint(1,4)
                if huntingchance==1:
                    print("You encountered a rabbit!")
                    while rabbit.health>=0 or self.health>=0:
                        attack=input("Would you like to attack?\n- ").lower()
                        if attack!="no":
                            rabbit.takedamage(5*self.strength)
                            finaldmg=round(rabbit.damage*self.defense)
                            self.takedamage(finaldmg)
                        else: 
                            print("ok")
                            break
                        if rabbit.health<=0:
                                print("You have successfully skewered the rabbit and got rabbeat!")
                                self.inventory.append(rabbit.drop)
                                rabbit.health=100
                                break
                        elif self.health<=0:
                            print("Your character died")
                            

                elif huntingchance==2:
                    print("You encountered a buffalo!")
                    while buffalo.health>=0 or self.health>=0:
                            attack=input("Would you like to attack?\n- ").lower()
                            if attack!="no":
                                buffalo.takedamage(5*self.strength)
                                finaldmg=round(buffalo.damage*self.defense)
                                self.takedamage(finaldmg)
                            else: 
                                print("ok")
                                break
                            if buffalo.health<=0:
                                    print("it died. You got beef.")
                                    self.inventory.append(buffalo.drop)
                                    buffalo.health=200
                                    break
                            elif self.health<=0:
                                print("Your character died")
                            
                elif huntingchance==3:
                    print("You enounter a frog!")
                    while frog.health>=0 or self.health>=0:
                            attack=input("Would you like to attack?\n- ").lower()
                            if attack!="no":
                                frog.takedamage(5*self.strength)
                                finaldmg=round(frog.damage*self.defense)
                                self.takedamage(finaldmg)
                            else: 
                                print("ok")
                                break
                            if frog.health<=0:
                                    print("Congrats! You murdered the frog! Meat has been added to your inventory")
                                    self.inventory.append(frog.drop)
                                    frog.health=150
                                    break
                            elif self.health<=0:
                                    print("Your character died!")
                elif huntingchance==4:
                    print("You found nothing!")
    def takedamage(self, amount):
        self.health-=amount
        print(f"Your player has {self.health} health left")           
    def work(self):
        payment=self.balance+random.randint(1,20)
        self.balance=payment
        stringsel = random.randint(0, 5)*self.rebirth
        print(workstrings[stringsel]['text'])
        print(f"You now have a balance of {payment} ")
        self.hunger=self.hunger-random.randint(8,10)
    def eat(self, food):
        while self.hunger<100:
            for i in self.inventory:
                if food=="rabbeat":
                    self.inventory.remove("rabbeat")
                    self.hunger= self.hunger+15
                    break
                elif food=="beef":
                    self.inventory.remove("beef")
                    self.hunger= self.hunger+35
                    break
                elif food=="meat":
                    self.inventory.remove("raw meat")
                    self.hunger=self.hunger+22
                    break
            else: 
                print("You have max hunger!")
                break
    def losehunger(self):
        losehunger=random.randint(1,5)
        self.hunger=self.hunger-losehunger
    def eat(self):
        hungercap=self.rebirth*100
        while self.hunger<hungercap:
                if askfood not in self.inventory:
                    print("You have no food!")
                    return
                if askfood=="rabbeat":
                    self.inventory.remove("rabbeat")
                    self.hunger=self.hunger+15
                    self.health=self.health+50
                    if self.health>100*self.rebirth:
                        self.health=100*self.rebirth
                    print(f"You have {self.hunger} hunger now and {self.health} health now!")
                    break
                elif askfood=="beef":
                    self.inventory.remove("beef")
                    self.hunger=self.hunger+30
                    self.health=self.health+100
                    if self.health>100*self.rebirth:
                        self.health=100*self.rebirth
                    print(f"You have {self.hunger} hunger now and {self.health} health now!")
                    break
                elif askfood=="meat":
                    self.inventory.remove("meat")
                    self.hunger=self.hunger+20
                    self.health=self.health+75
                    if self.health>100*self.rebirth:
                        self.health=100*self.rebirth
                    print(f"You have {self.hunger} hunger now and {self.health} health now!")
                    break
                print("You don't have any food")
    def reborn(self):
        rebirthamount=1.5*200*self.rebirth
        askrebirth=input(f"Would you like the rebirth for {rebirthamount} coins? You will gain more strength, health, defense and money gain.\n- ").lower()
        if askrebirth=="yes":
            if self.balance-rebirthamount>=0:
                self.rebirth=self.rebirth+1
                self.balance=self.balance-rebirthamount
                self.health=self.health*self.rebirth
                self.strength=self.strength*self.rebirth
                self.defense=self.defense-(self.rebirth/10)
            elif self.balance-rebirthamount<0:
                print("You need more coins in your balance!")
 
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
            self.health=700
        elif self.name=="Hut":
            self.health=5000
        elif self.name=="john":
            self.health=1000
#heree


        


pName = input("What do you want the player's name to be?\n*Stats will be randomized\n- ")
#               name,  health, strength,                                hunger          inventory balance
player = Player(pName, 100, random.randint(1,10), random.randint(50, 100), ['Twig'], 10000000, 1, random.uniform(.95, 1))
run = True
while run:
    if player.health<=0:
        break
    if player.hunger<=0:
        print("You died from hunger loss!")
        break
    if player.hunger<=25:
        print(f"You have {player.hunger} hunger left! Make sure it doesn't reach 0! (Hunt for food)")
    john = NPC("john", 1000, 4)
    Hut= NPC("Hut", 5000, 2)
    Rud= NPC("Rud", 700, 15)
    rabbit= Animal(100, 1, "rabbeat")
    buffalo=Animal(200, 2, "beef")
    frog=Animal(150, 1, "meat")
    print(" - What would you like to do?(type a number):")
    print("[1] - Check Stats")
    print("[2] - Fight")
    print("[3] - Quit")
    print("[4] - Shop")
    print("[5] - Armory")
    print("[6] - Work")
    print("[7] - Hunt")
    print("[8] - Eat")
    print("[9] - Rebirth")
    option = input("- ")
    if option.lower() == "check stats" or int(option) == 1:
        player.checkStats()
    elif int(option) == 2:
        player.losehunger()    
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
        player.losehunger()
    elif int(option)== 7:
        player.hunt()
        player.losehunger()
    elif int(option)== 8:
        askfood=input("What food do you want to eat? (rabbeat, meat, or beef)\n- ").lower()
        player.eat()
    elif int(option)==9:
        player.reborn()
    elif int(option) == 3:
        run = False

    