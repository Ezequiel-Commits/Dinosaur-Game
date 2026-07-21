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
                    if distanceBetweenSprites <= sprite1.size + sprite2.size: #Not sure I want to use size here. 
                        
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