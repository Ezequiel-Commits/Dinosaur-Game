"""A class to encapsulate the checking of collisions between two objects. Will be better in the long run if I plan on 
implementing another type of obstacle(e.g. pterodactyl)"""
import math
import cactus
import dinosaur
import pterodactyl

class CollisionManager:
    def __init__(self, spriteList):
        self.spriteList = spriteList

    def checkCollisions(self):
        for sprite1 in self.spriteList:
            for sprite2 in self.spriteList: #Two "for loops" to compare a pair of sprites
                if sprite1 != sprite2: #Avoid comparing the same sprites to each other
                    distanceBetweenSprites = math.dist([sprite1.x, sprite1.y],[sprite2.x, sprite2.y])
                    if distanceBetweenSprites <= sprite1.size + sprite2.size: 
                        #Not sure I want to use size here, as it was for bounding circles. Comparing the 
                        # distanceBetweenSprites to hitboxes or reworking the system. 
                        
                        # Check the types of the sprites
                        if isinstance(sprite1, cactus.Cactus) and isinstance(sprite2, dinosaur.Dinosaur):
                            # Remove the sprite's drawing and the remove the sprite from the spriteList
                            # print("Orc + gatehouse: the game should end")
                            # sprite1.undraw()
                            # self.spriteList.remove( sprite1 )
                            return "endgame"

                        if isinstance(sprite1, pterodactyl.Pterodactyl) and isinstance(sprite2, dinosaur.Dinosaur):
                            # Remove the sprite's drawing and the remove the sprite from the spriteList
                            # print("Orc + gatehouse: the game should end")
                            # sprite1.undraw()
                            # self.spriteList.remove( sprite1 )
                            return "endgame"

def checkCollisions(self):
        for sprite1 in self.spriteList:
            for sprite2 in self.spriteList: #Two "for loops" to compare a pair of sprites
                if sprite1 != sprite2: #Avoid comparing the same sprites to each other
                    # Define sprite1' hitbox(es)
                    if sprite1 == dinosaur:
                        # there'll be multiple hitboxes 
                        left1 = sprite1.leftx
                        right1 = sprite1.rightx
                        top1 = sprite1.topy
                        bottom1 = sprite1.bottomy

                    # Define sprite2' hitbox(es)
                    left2 = sprite2.leftx
                    right2 = sprite2.rightx
                    top2 = sprite2.topy
                    bottom2 = sprite2.bottomy
                    # Variables to check if hitboxes from each sprite overlap
                    x_overlap = False
                    y_overlap = False
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