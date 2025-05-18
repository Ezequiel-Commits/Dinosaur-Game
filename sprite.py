"""A superclass for each sprite in this game."""
import turtle 

class Sprite:
    def __init__(self, x):
        self.x = x
        self.turt = turtle.Turtle()
        self.turt.ht()
        self.turt.speed(0)
    
    def draw(self):
        # Not much in common between draw methods. 
        pass

    def undraw(self):
        self.turt.clear()
        pass