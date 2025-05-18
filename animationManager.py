"""A class to encapsulate the idea of animation on the screen. All forms of sprite animation should occur here."""

import turtle
import time
import collisionManager

class AnimationManager:
    def __init__(self, dino, tapestry): 
        
        self.dino = dino
        self.tapestry = tapestry
        self.currentX = 0

        self.myCollisionManager = collisionManager.CollisionManager(spriteList = [dino, tapestry.listOfCacti])

        turtle.tracer(False)
        turtle.setworldcoordinates(0,0, 400, 350)
        
    def run(self):
        # move the screen over the tapestry using a turtle method and for loop
        self.currentX += 1
        turtle.setworldcoordinates(llx = self.currentX ,lly = -20, urx = 400 + self.currentX, ury = 350) 
        
        self.dino.undraw()

        # Render the dinosaur on the ground until the player presses the "up" key
        if self.dino.jumping == False:
            # Draw the dinosaur on the ground
            self.dino.draw(self.currentX)
        elif self.dino.jumping == True:
            # draw the dinosaur jumping
            self.dino.renderJump(self.currentX)
        else:
            print("error cactch: Jumping isn't set to a value")
        
        turtle.update()
        
        
        turtle.ontimer(self.run,1000//60) 