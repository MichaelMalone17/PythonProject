from MasterGame import *

#Tomb Raider

print("Make your way to the Treasure room and grab the treasure.")

print("There is another Raider looking for the Treasure as well, stop him and take his belongings(You will need it to live)")

print("Once you have the Treasure, make your way out of Tomb")

print("To play, type 'go' followed by [north,south,east,west]")

print("When you encounter an item in the Tomb, type 'grab' followed by the name of the item.")

print("If you come across the other Raider in the Tomb, type 'fight' to start the Raider Battle!")

print("Good luck Raider!")

playerName = input("Enter your name Raider")#Get player's name

playerRaider = Raider(playerName)#Create a new Raider

comRaider = EvilRaider("Slade")#Creat the evil Raider

startGame = Game()#Start Game

startGame.gameStart(playerRaider,comRaider)





