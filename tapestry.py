"""A tapestry class to that encapsulates the background of the game, including the ground and cacti"""
import random
import cactus
import turtle

class Tapestry:
    def __init__(self, nOfCacti, tapestryLength = 450):
        self.nOfCacti = nOfCacti
        # self.tapestryLength = tapestryLength
        
        # An instance variable to make checking for collisions easier
        self.listOfCacti=[]

    
    def generate(self, startingx = 0, endingx = 400):
        # Generate a tapestry with randomly spaced cacti that will 
        # appear on the screen as the dinosaur moves
        
        # loops for amount of cacti to get location of the cacti's
        for Cactus in range(self.nOfCacti):
            random_X = random.randint(startingx, endingx)
            # create a cactus object with a random x
            new_cactus = cactus.Cactus(random_X)
            self.listOfCacti.append(new_cactus )
            
        for cactusObject in self.listOfCacti:
            # Draw the cactus 
            cactusObject.draw()