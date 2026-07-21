"""A class to encapsulate the idea of animation on the screen. All forms of sprite animation should occur here."""

import turtle
import time
import collisionManager
import tapestry
import cactus


class AnimationManager:
    def __init__(self, dino):

        self.tapestryLength = 550
        tapestryObject = tapestry.Tapestry(nOfCacti = 2) #Cacti can be bunched up or not present for a while. 
        tapestryObject.generate(500, self.tapestryLength) 
        
        self.dino = dino
        self.tapestry = tapestryObject
        self.currentX = 0
        self.refreshPerSecond = 30

        self.spriteList = []
        self.spriteList.append(dino)

        # Variable to help generate cactus as the game runs. 
        self.cactusCount = 0 

        for Cactus in self.tapestry.listOfCacti:
            # How to delete Cactus as they're left behind? 
            self.cactusCount += 1 
            self.spriteList.append(Cactus)

        self.myCollisionManager = collisionManager.CollisionManager(self.spriteList)

        self.scoreTracker = turtle.Turtle()
        self.scoreTracker.ht()
        self.startTime = time.time()
        # Check how many seconds have passed since the program started running and store it in a variable
        
    def run(self):
        # move the screen over the tapestry using a turtle method and for loop
        self.currentX += 2

        for sprite in self.spriteList:
            if sprite.x <= self.currentX - 20:
                # Check the sprites' coordinates
                
                # if outside of the window, undraw the sprite and remove the sprite from spriteList 
                sprite.undraw()
                if isinstance(sprite, cactus.Cactus):
                    # A start to clearing the list of cacti
                    print(self.spriteList, self.tapestry.listOfCacti)
                    self.tapestry.listOfCacti.remove( sprite )
                    self.cactusCount -= 1
                self.spriteList.remove( sprite )
        
        if self.cactusCount < 3:
            # print(self.spriteList)
            print(self.cactusCount)
            self.cactusCount += 2
            # It's generating the cactus behind the dinosaur as opposed to in front of the dinosaur
            self.tapestry.generate(self.currentX + 500, self.currentX + self.tapestryLength)
            for Cactus in self.tapestry.listOfCacti:
                # If the cactus is already in the sprite list. 
                if Cactus in self.spriteList:
                    break
                # How to avoid adding in the same cacti for each run of this for loop? 
                self.spriteList.append(Cactus)


        turtle.setworldcoordinates(llx = self.currentX ,lly = -20, urx = 400 + self.currentX, ury = 350) 
        
        self.dino.undraw()
        self.scoreTracker.clear()

        self.scoreTracker.goto(350 + self.currentX,300)
        self.scoreTracker.write(arg = int((self.startTime - time.time()) * -10), font = ("Arial", 20, "normal"))

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
            print("Game over")
            # return 
        else:
            pass
        
        
        turtle.ontimer(self.run,100//self.refreshPerSecond) 