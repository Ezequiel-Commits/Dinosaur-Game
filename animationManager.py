"""A class to encapsulate the idea of a gamaManager"""

import turtle
import time

class AnimationManager:
    def __init__(self,refresh_persecond,length,dino,tapestry):
        self.refresh_persecond = refresh_persecond
        self.length = length
        self.dino = dino
        self.tapestry = tapestry
        self.currentx = 0
        
    def run(self):
        # move the screen over the tapestry using a turtle 
        # method and for loop
        self.currentx += 1
        turtle.setworldcoordinates(0+self.currentx,-20, \
        400+self.currentx,350) 
        
        # Render the dinosaur on the ground until the player
        # presses the "up" key
        self.dino.turt.clear()
        # print(self.dino.jumping)
        if self.dino.jumping == False:
            # Draw the dinosaur on the ground
            self.dino.draw(0+self.currentx)
        elif self.dino.jumping == True:
            # draw the dinosaur jumping
            self.dino.render_jump(0+self.currentx)
        else:
            print("error cactch: Jumping isn't set to a value")
        turtle.update()

        collision = self.tapestry.collision(self.dino)
        if collision == True:
            exit()
        turtle.update()
        
        
        turtle.ontimer(self.run,1000//self.refresh_persecond) # Two "//" for float division