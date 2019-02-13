from Map import *

class Game:

    def gameStart(self, playerRaider = Raider, comRaider = EvilRaider):

        mapLocation = Map()

        currentLocation = mapLocation.beginningLocation

        while True:

            #Player Status

            print("--------------------------------------------------------------")
            print("You're current location is. ", currentLocation)
            print("Current items in backpack ")
            playerRaider.viewItems()#show current item in backpack

            if 'specialItem' in mapLocation.location[currentLocation]:
                print("You located a " + mapLocation.location[currentLocation]['specialItem'])

            elif 'badRaider' in mapLocation.location[currentLocation]:
                print("Uh Oh! You just ran into the other Raider! " + mapLocation.location[currentLocation]['badRaider'])

            if currentLocation == 'Treasure Room' and 'orb' not in playerRaider.myBackpack:#Check if player has the orb in the backpack
                print("Hmmm it seems this door requires some kind of ORB to get inside.")

                print("A mystrious force takes you back to the Tomb Entrance...")

                currentLocation = mapLocation.beginningLocation

            elif currentLocation == 'Treasure Room' and 'orb' in playerRaider.myBackpack:#Check play has the orb

                print("You opened the door! Good job Raider!")

                print("Now grab the Treasure and get out of here!")

            if currentLocation == 'Tomb Entrance' and 'ruby' in playerRaider.myBackpack:#Check if player has the ruby at the Treasure Entrance

                print("You made it out sucessfully with the Treasure! Good Work Raider!")

                break
            print("----------------------------------------------------------------")
            #End of Player Status

            action = input("What will you do next raider?")#Get the player's action

            action = action.lower().split()#Break action into a list

            if action[0] == 'go':#If index 0 is go, the player will move around the map

                if action[1] in mapLocation.location[currentLocation]:

                    currentLocation = mapLocation.location[currentLocation][action[1]]

                else:

                    print("You can't go that way!")

            if action[0] == 'grab':#If index 0 is grab, the player action will grab an item

                if 'specialItem' in mapLocation.location[currentLocation] and action[1] in mapLocation.location[currentLocation]['specialItem']:

                    playerRaider.pickUpItems(mapLocation.location[currentLocation]['specialItem'])

                    print("You picked up the " + mapLocation.location[currentLocation]['specialItem'])

            if action[0] == 'fight':#If index 0 is fight, the player will fight the other Raider

                if 'badRaider' in mapLocation.location[currentLocation]:

                    print("Defeat him quickly, he might have something valueable!")

                    readyToFight = input("Are you ready to fight?")

                    readyToFight = readyToFight.lower()

                    if readyToFight == 'yes':

                        raiderFight = Battle()

                        #Add player and computer into the Battle class
                        #The player wins if the raiderBattle function returns "You defeated the Raider"

                        if raiderFight.raiderBattle(playerRaider,comRaider) == "You defeated the Raider":

                            playerRaider.pickUpItems(comRaider.backPack)
                            break
                        else:
                            print("Better luck next time Raider!")
                            break


