import random

class Raider:

    def __init__(self,name):

        self.name = name#player Name

        self.health = 100#player Health

        self.agility = 100#player Agility

        self.strength = 25#player strength

        self.myBackpack = []#player backpack

    def raiderName(self):

        return self.name

    def health(self):

        print(self.health)

    def agilityIncrease(self):#If the player defeats the Evil Raider and obtain special Item
                                #the player gets an agility increase.
        self.agility += 100

    def attack(self):#Random number between 0-25 determins the players attack points

        return random.randrange(0,self.strength)

    def pickUpItems(self, item):#Pick up items around the tomb and from Evil Raider

        self.myBackpack.append(item)

    def viewItems(self):

        print(self.myBackpack)

class EvilRaider(Raider):#Evil Raider Class

    def __init__(self,name):

        self.name = name#Evil Raider Name

        self.backPack = ['pistol', '8 hour energy drink']#Special Items Evil Raider carries

        self.strength = 25#Evil Raider strength

        self.health = 100#Evil Raider Health

    def raiderName(self):

        return self.name

    def health(self):

        print(self.health)

    def viewItems(self):

        print(self.backPack)

    def attack(self):#Random number between 0-25 determins the players attack points

        return random.randrange(0,self.strength)



















