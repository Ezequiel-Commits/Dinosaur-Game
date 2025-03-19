"""A superclass for each sprite in this game."""
import turtle 

class Sprite:
    def __init__(self, x):
        self.x = x
        self.turt = turtle.Turtle()
        self.turt.ht()
        self.turt.speed(0)
    
    def draw(self):
        pass

    def undraw(self):
        pass