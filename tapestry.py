"""A tapestry class to that encapsulates the background of the game, including the ground and cacti"""
import random
import cactus
import turtle

class Tapestry:
    def __init__(self, nOfCacti, tapestryLength):
        self.nOfCacti = nOfCacti
        self.tapestryLength = tapestryLength
        
        # An instance variable to make checking for collisions easier
        self.listOfCacti=[]

    
    def generate(self):
        # Generate a tapestry with randomly spaced cacti that will 
        # appear on the screen as the dinosaur moves
        self.listOfCacti=[]
        
        # loops for amount of cacti to get location of the cacti's
        for Cactus in range(self.nOfCacti):
            #Add a random cactus between 0 and the length of the 
            # tapestry 
            random_X = random.randint(0,self.tapestryLength)
            # create a cactus object with a random x
            new_cactus=cactus.Cactus(random_X)
            self.listOfCacti.append(new_cactus )
            
        for cactusObject in self.listOfCacti:
            # Draw the cactus 
            cactusObject.draw()