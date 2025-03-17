"""A tapestry class to render the game"""
import random
import cactus
import dinosaur
import turtle

class Tapestry:
    # Create a tapestry that will serve as a background
    def __init__(self, nOfCacti,tapestry_length):
        self.nOfCacti = nOfCacti
        self.tapestry_length = tapestry_length
        
        # An instance variable to make checking for collisions
        # easier
        self.list_of_cacti=[]
        
        self.turt=turtle.Turtle()
    
    def generate(self):
        # Generate a tapestry with randomly spaced cacti that will 
        # appear on the screen as the dinosaur moves
        self.list_of_cacti=[]
        
        # loops for amount of cacti to get location of the cacti's
        for Cactus in range(self.nOfCacti):
            #Add a random cactus between 0 and the length of the 
            # tapestry 
            random_X = random.randint(0,self.tapestry_length)
            # create a cactus object with a random x
            new_cactus=cactus.Cactus(random_X)
            self.list_of_cacti.append(new_cactus )
            
        for cactusObject in self.list_of_cacti:
            # Draw the cactus 
            cactusObject.draw()
    
    def collision(self, dino):
        collision = False
        for cactus in self.list_of_cacti:
            #print(dino)
            if cactus.check_collision(dino)==True:
                collision=True
                print ("collision")
        return collision