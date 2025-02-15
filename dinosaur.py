import turtle
import time

class Dinosour:
    
    def __init__(self,x,y):
        # Bottom left of the triangle
        self.x=x
        self.y=y
        # Define bounding variables of each cactus to check 
        # for collisions later
        self.leftx=x-(x/2)
        self.rightx=x+(x/2)
        self.topy=self.y+49
        self.bottomy=self.y
        
        self.turt=turtle.Turtle()
        self.turt.ht()
        self.turt.speed(0)
        
        self.goUp = True # Debounce variable
        
        turtle.onkeypress(self.handleUp, "Up")
        self.jumping = False
        
        # Listen for key presses 
        turtle.listen()

    
    def draw(self,x=0):
        self.x = x
        # Go to the starting coords of the dinosaur
        self.turt.penup()
        self.turt.goto(self.x,self.y)
        self.turt.pendown()
        # draw a basic triangle stand-in for the dinosaur
        for i in range(3):
            self.turt.forward(40)
            self.turt.left(120)
    
    def render_jump(self,x=0): 
        # pass in an x so that the dinosaur moves along with 
        # the tapestry 
        self.x = x
        if self.goUp == True:
            # add 1 to the y-coord
            self.y += 1
            # if the y-coord is bigger than 120 set goUp to true
            if self.y >=60:
                self.goUp =not self.goUp
                
        # if goUp is false
        if self.goUp == False:
            # subtract 1 from the y-coord
            self.y -= 1
            if self.y <=0:
                self.goUp=not self.goUp
                # Let the game manager know the jump has been completed
                self.jumping = False
                return print("ending jump function")
        self.turt.clear()
        self.draw(self.x)
    
    # A function to handle player input, allowing for
    # the player to jump 
    def handleUp(self):
        # Set an instance variable to some value to be checked
        # in the gameManager class
        self.jumping = True