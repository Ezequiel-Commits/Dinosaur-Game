"""Create a class to encapsulate the cactusus drawn on the screen"""
import dinosaur
import turtle
import time

class Cactus:
    def __init__(self,x):
        # middle x
        self.x = x
        # Define bounding variables of each cactus to check 
        # for collisions later
        self.leftx = x-5
        self.rightx = x+5
        self.topy = 30
        self.bottomy = 0
        self.turt = turtle.Turtle()
        self.turt.ht()
    
    
    def draw(self):
        # Go to the coordinates defined by the tapestry class
        self.turt.goto(self.x,0)
        for i in range(2):
            # Draw a basic cactus
            self.turt.forward(10)
            self.turt.left(90)
            self.turt.forward(30)
            self.turt.left(90)
    
    def __repr_(self):
        pass
    
    def check_collision(self,dino):
        # a method to check if a cactus has collided with the
        # dinosaur
        
        # Define the bounding coordinates of the dino
        left1 = dino.leftx
        right1 = dino.rightx
        top1 = dino.topy
        bottom1 = dino.bottomy
        
        # print("top1:" + str(top1),"bottom1:" + str(bottom1))
        
        # Define the bounding coordinates of the cactus
        left2 = self.leftx
        right2 = self.rightx
        top2 = self.topy
        bottom2 = self.bottomy
        
        # Variables to check if the dinosaur and cactus overlap
        x_overlap = False
        y_overlap = False
        
        # print("top2:" + str(top2),"bottom2:" + str(bottom2))
        
        # Check if there is no collision and then reverse it
        if left2 > right1 or right2 < left1:
            # the cactus and dinosaur don't have overlapping
            # x's
            print("no overlap x")
            x_overlap = False
        else:
            x_overlap = True
        
        if bottom2 > top1 or top2 < bottom1:
            # the cactus and dinosaur don't have overlapping
            # y's
            print("no overlap y")
            y_overlap = False
        else:
            y_overlap = True
        
        if x_overlap == True and y_overlap == True:
            # the player has touched a cactus
            print("you lose")
            exit()