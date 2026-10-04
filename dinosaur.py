import turtle
import time
import sprite

class Dinosaur(sprite.Sprite):
    # Use the sprite class constructor

    def __init__(self,x,y):
        sprite.Sprite.__init__(self, x) # Bottom left of the triangle is x
        self.y = y
        self.x = x
        self.hitboxList = []
        
        self.goUp = True # Debounce variable
        
        turtle.onkeypress(self.handleUp, "Up")
        self.jumping = False
        
        # Listen for key presses 
        turtle.listen()

    def drawSq(self,x,y):
        for side in range(2):
            self.turt.forward(x)
            self.turt.left(90)
            self.turt.forward(y)
            self.turt.left(90)
    
    def draw(self, x = 0):
        self.x = x
        # Go to the starting coords of the dinosaur
        self.turt.penup()
        self.turt.goto(self.x,self.y)
        self.turt.pendown()
        # draw a basic triangle stand-in for the dinosaur
        for i in range(3):
            self.turt.forward(40)
            self.turt.left(120)
        # Testing out different numbers until I like what I see
        # self.turt.penup()
        self.turt.goto(self.x + 7, self.y)
        self.hitBox1 = self.drawSq(27, 8)
        # Circumventing the nonetype error.
        self.leftx1 = self.x + 7
        self.rightx1 = self.leftx1 + 27 
        self.topy1 = self.y + 8
        self.bottomy1 = self.y
        self.turt.goto(self.x + 10, self.y + 8)
        self.hitBox2 = self.drawSq(18, 8)
        self.leftx2 = self.x + 10
        self.rightx2 = self.leftx1 + 18 
        self.topy2 = self.y + 16
        self.bottomy2 = self.y + 8
        self.turt.goto(self.x + 14, self.y + 16)
        self.hitBox3 = self.drawSq(14, 8)
        self.leftx3 = self.x + 14
        self.rightx3 = self.leftx3 + 14 
        self.topy3 = self.y + 24
        self.bottomy3 = self.y + 16
        self.turt.goto(self.x + 18, self.y + 24)
        self.hitBox4 = self.drawSq(3, 8)
        # The y overlap always seems to occur for this hitbox...
        self.leftx4 = self.x + 18
        self.rightx4 = self.leftx4 + 3 
        self.topy4 = self.y + 32
        self.bottomy4 = self.y + 24
    
    def renderJump(self,x=0): 
        # pass in an x so that the dinosaur moves along with 
        # the tapestry 
        self.x = x
        if self.goUp == True:
            # add 1 to the y-coord
            self.y += 1.5
            # if the y-coord is bigger than 120 set goUp to true
            if self.y >= 69:
                self.goUp =not self.goUp
                
        # if goUp is false
        if self.goUp == False:
            # subtract 1 from the y-coord
            self.y -= 1.5
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

    # def __repr__(self):
    #     return f"DINO: <{self.leftx}, {self.bottomy}>" #Not too sure what this f does 