"""A tapestry class to that encapsulates the background of the game, including the ground and cacti"""
import random
import cactus
import turtle
import pterodactyl

class Tapestry:
    def __init__(self, nOfCacti = 2, nOfPterodactyls = 1, tapestryLength = 450):
        self.nOfCacti = nOfCacti
        self.nOfPterodactyls = nOfPterodactyls
        # self.tapestryLength = tapestryLength
        
        # An instance variable to make checking for collisions easier
        self.listOfCacti = []
        self.listOfPterodactyls = []

    
    def generateCacti(self, startingx = 0, endingx = 400):
        # Generate a tapestry with cacti that will 
        # appear on the screen as the dinosaur moves
        
        # loops for amount of cacti to get location of the cacti
        # Around 4-5 are created instead of 3 to start
        for Cactus in range(self.nOfCacti):
            randomX = random.randint(startingx, endingx)
            # create a cactus object with a random x
            newCactus = cactus.Cactus(randomX)
            self.listOfCacti.append(newCactus)
            
        for cactusObject in self.listOfCacti:
            # Can't write for cactus... for some reason
            cactusObject.draw()

    def generatePterodactyls(self, startingx = 200, endingx = 250):
        # print(self.nOfPterodactyls) 2 are created at the start instead of 1
        for Pterodactyl in range(self.nOfPterodactyls):
            # Don't want the starting and ending x variable to be constant. 
            randomX = random.randint(startingx, endingx)
            randomY = random.choice([5,50])
            print(randomY)
            # create a pterodactyl object with a random x
            newPterodactyl = pterodactyl.Pterodactyl(randomX, randomY)
            self.listOfPterodactyls.append(newPterodactyl)
        
        for pterodactylObject in self.listOfPterodactyls:
            pterodactylObject.draw()