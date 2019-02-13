from Raider import *

class Battle:#Battle Class determines the winner of the battle between player and computer

    def raiderBattle(self, goodRaider = Raider, badRaider = EvilRaider):

        #calculate results of the battle

        raider_A_Hlth = goodRaider.health#player health

        raider_B_Hlth = badRaider.health#Evil Raider health

        while(True):

            raider_A_Atk = goodRaider.attack()#player attack

            raider_B_Atk = badRaider.attack()#Evil Raider attack

            if raider_A_Atk > raider_B_Atk:#player Raider attacks first if it's attack points is greater than Evil Raider

                raider_B_Hlth = raider_B_Hlth - raider_A_Atk

                print(goodRaider.raiderName(), " attacked ", badRaider.raiderName(), " for ", raider_A_Atk, " points.")

                print(badRaider.raiderName(), " now has ", raider_B_Hlth, " health.")

            elif raider_B_Atk > raider_A_Atk:#Evil Raider attacks first if it's attack points is greater than player

                raider_A_Hlth = raider_A_Hlth - raider_B_Atk

                print(badRaider.raiderName(), " attacked ", goodRaider.raiderName(), " for ", raider_B_Atk, " points.")

                print("You now have ", raider_A_Hlth, " health.")

            if (raider_A_Hlth < 0):#If the player health reaches 0

                return print("You have died.")


            elif (raider_B_Hlth < 0):#If the player defeats the Evil Raider

                return print("You defeated the Raider")




