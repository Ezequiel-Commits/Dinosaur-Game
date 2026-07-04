"""A class to encapsulate the idea of animation on the screen. All forms of sprite animation should occur here."""

import turtle
import time
import collisionManager

class AnimationManager:
    def __init__(self, dino, tapestry): 
        
        self.dino = dino
        self.tapestry = tapestry
        self.currentX = 0
        self.refreshPerSecond = 30

        self.spriteList = []
        self.spriteList.append(dino)
        for Cactus in tapestry.listOfCacti:
            self.spriteList.append(Cactus)

        self.myCollisionManager = collisionManager.CollisionManager(self.spriteList)

        scoreTracker = turtle.Turtle()
        startTime = time.time()
        scoreTracker.
        if startTime - time.time()
        
    def run(self):
        # move the screen over the tapestry using a turtle method and for loop
        self.currentX += 1
        turtle.setworldcoordinates(llx = self.currentX ,lly = -20, urx = 400 + self.currentX, ury = 350) 
        
        self.dino.undraw()

        # Render the dinosaur on the ground until the player presses the "up" key
        if self.dino.jumping == False:
            # Draw the dinosaur on the ground
            self.dino.draw(0 + self.currentX)
        elif self.dino.jumping == True:
            # draw the dinosaur jumping
            self.dino.renderJump(0 + self.currentX)
        else:
            print("error cactch: Jumping isn't set to a value")
        
        turtle.update()

        collision = self.myCollisionManager.checkCollisions()
        if collision == "endgame":
            print("working")
        else:
            pass
        
        
        turtle.ontimer(self.run,1000//self.refreshPerSecond) 