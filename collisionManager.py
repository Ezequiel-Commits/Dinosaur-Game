"""A class to encapsulate the checking of collisions between two objects"""
import math

class CollisionManager:
    def __init__(self, spriteList):
        self.spriteList = spriteList

    def checkCollisions(self):
        for sprite1 in self.spriteList:
            for sprite2 in self.spriteList: #Two for loops to compare a pair of sprites
                if sprite1 != sprite2: #Avoid comparing the same sprites to each other
                    distanceBetweenSprites = math.dist([sprite1.x, sprite1.y],[sprite2.x, sprite2.y])
                    if distanceBetweenSprites <= sprite1.size + sprite2.size:
                        # If the distance between two sprites is less than the combined radii of their
                        # bounding circles, an overlap is present
                        
                        # Check the types of the sprites
                        if isinstance(sprite1, orc.Orc) and isinstance(sprite2, gatehouse.Gatehouse):
                            # Remove the sprite's drawing and the remove the sprite from the spriteList
                            print("Orc + gatehouse: the game should end")
                            sprite1.undraw()
                            self.spriteList.remove( sprite1 )
                            # Add an instance variable to tower that checks how many times it's been hit? 
                        elif isinstance(sprite1, bullet.Bullet) and isinstance(sprite2, orc.Orc) or isinstance(sprite2, bullet.Bullet) and isinstance(sprite1, orc.Orc):
                            print("Orc + bullet: Both should dissapear")
        