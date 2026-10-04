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
                            # Define sprite1' hitbox(es)
                            if isinstance(sprite1, dinosaur.Dinosaur):
                                # there'll be multiple hitboxes, so define multiple hitboxes
                                # These variables aren't being accessed past the if statement...
                                left1 = sprite1.leftx1
                                right1 = sprite1.rightx1
                                top1 = sprite1.topy1
                                bottom1 = sprite1.bottomy1
                                # Jump over left2 in this situation
                                left3 = sprite1.leftx2
                                right3 = sprite1.rightx2
                                top3 = sprite1.topy2
                                bottom3 = sprite1.bottomy2
                                # left4 = sprite1.leftx3
                                # right4 = sprite1.rightx3
                                # top4 = sprite1.topy3
                                # bottom4 = sprite1.bottomy3
                                left5 = sprite1.leftx4
                                right5 = sprite1.rightx4
                                top5 = sprite1.topy4
                                bottom5 = sprite1.bottomy4
                                # Define sprite2' hitbox(es)
                                left2 = sprite2.leftx
                                right2 = sprite2.rightx
                                top2 = sprite2.topy
                                bottom2 = sprite2.bottomy
                                # Variables to check if hitboxes from each sprite overlap
                                x_overlap = False
                                y_overlap = False
                                # Check if there is no collision and then reverse it; Do I have to do this with
                                # all the dino hitboxes?
                                # The top most hitbox isn't working right now...
                                if left2 > right1 or right2 < left1:
                                    x_overlap = False
                                elif left2 > right3 or right2 < left3:
                                    x_overlap = False
                                elif left2 > right5 or right2 < left5:
                                    x_overlap = False
                                else:
                                    x_overlap = True
                                if bottom2 > top1 or top2 < bottom1:
                                    # the cactus and dinosaur don't have overlapping
                                    # y's
                                    # print("no overlap y")
                                    y_overlap = False
                                elif  bottom2 > top3 or top2 < bottom3:
                                    y_overlap = False
                                elif bottom2 > top5 or top2 < bottom5: #How come the parallel 
                                # if statements for the fourth hitbox seem fine here?
                                # Disabling these if statements biases the collisions for 1's 
                                    y_overlap = False
                                else:
                                    y_overlap = True
                                
                                if x_overlap == True and y_overlap == True:
                                    # the player has touched an obstacle
                                    print("you lose - 1")
                                    # exit()
                            elif isinstance(sprite2, dinosaur.Dinosaur):
                                # First sprite
                                left1 = sprite1.leftx
                                right1 = sprite1.rightx
                                top1 = sprite1.topy
                                bottom1 = sprite1.bottomy
                                # Dinosaur Sprite
                                left2 = sprite2.leftx1
                                right2 = sprite2.rightx1
                                top2 = sprite2.topy1
                                bottom2 = sprite2.bottomy1
                                left3 = sprite2.leftx2
                                right3 = sprite2.rightx2
                                top3 = sprite2.topy2
                                bottom3 = sprite2.bottomy2
                                left5 = sprite2.leftx4
                                right5 = sprite2.rightx4
                                top5 = sprite2.topy4
                                bottom5 = sprite2.bottomy4
                                # Variables to check if hitboxes from each sprite overlap
                                x_overlap2 = False
                                y_overlap2 = False
                                # Check if there is no collision and then reverse it; seems as though I have to do this
                                # with all four of the dinosaur hitboxes.
                                if left1 > right2 or right1 < left2:
                                    # the cactus and dinosaur don't have overlapping
                                    # x's
                                    # print("no overlap x")
                                    x_overlap2 = False
                                elif left1 > right3 or right1 < left3:
                                    x_overlap2 = False
                                elif left1 > right5 or right1 < left5: #seems like this if statement is fine.
                                    x_overlap2 = False
                                    # Disabling the fourth hitbox statements here mens a lot more printed 2's than 1's.
                                else:
                                    x_overlap2 = True
                                
                                if bottom1 > top2 or top1 < bottom2:
                                    # the cactus and dinosaur don't have overlapping
                                    # y's
                                    # print("no overlap y")
                                    y_overlap2 = False
                                elif bottom1 > top3 or top1 < bottom3:
                                    y_overlap2 = False
                                elif bottom1 > top5 or top1 < bottom5: 
                                    # Why would this interfere with the bottom two hitboxes? 
                                    y_overlap2 = False
                                else:
                                    y_overlap2 = True
                                
                                if x_overlap2 == True and y_overlap2 == True:
                                    # the player has touched an obstacle
                                    print("you lose - 2")
                                    # exit()
                            else:
                                # No need to check for collisions between cacti and pterodactyls
                                pass

'''def checkCollisions(self):
        for sprite1 in self.spriteList:
            for sprite2 in self.spriteList: #Two "for loops" to compare a pair of sprites
                if sprite1 != sprite2: #Avoid comparing the same sprites to each other
                    # Define sprite1' hitbox(es)
                    if isinstance(sprite1, dinosaur.Dinosaur):
                        # there'll be multiple hitboxes, so define multiple hitboxes
                        # These variables aren't being accessed past the if statement...
                        left1 = sprite1.leftx1
                        right1 = sprite1.rightx1
                        top1 = sprite1.topy1
                        bottom1 = sprite1.bottomy1
                        # Jump over left2 in this situation
                        left3 = sprite1.leftx2
                        right3 = sprite1.rightx2
                        top3 = sprite1.topy2
                        bottom3 = sprite1.bottomy2
                        # left4 = sprite1.leftx
                        # right4 = sprite1.rightx
                        # top4 = sprite1.topy
                        # bottom4 = sprite1.bottomy
                        # left5 = sprite1.leftx
                        # right5 = sprite1.rightx
                        # top5 = sprite1.topy
                        # bottom5 = sprite1.bottomy
                        # Define sprite2' hitbox(es)
                        left2 = sprite2.leftx
                        right2 = sprite2.rightx
                        top2 = sprite2.topy
                        bottom2 = sprite2.bottomy
                        # Variables to check if hitboxes from each sprite overlap
                        x_overlap = False
                        y_overlap = False
                        # Check if there is no collision and then reverse it; seems as though I have to do this
                        # with all four of the dinosaur hitboxes.
                        if left2 > right1 or right2 < left1 or left2 > right3 or right3 < left2:
                            # the cactus and dinosaur don't have overlapping
                            # x's
                            # print("no overlap x")
                            x_overlap = False
                        else:
                            x_overlap = True
                        
                        if bottom2 > top1 or top2 < bottom1 or bottom2 > top3 or top3 < bottom2:
                            # the cactus and dinosaur don't have overlapping
                            # y's
                            # print("no overlap y")
                            y_overlap = False
                        else:
                            y_overlap = True
                        
                        if x_overlap == True and y_overlap == True:
                            # the player has touched a cactus
                            print("you lose")
                            # exit()
                    elif isinstance(sprite1, dinosaur.Dinosaur):
                        left2 = sprite1.leftx1
                        right2 = sprite1.rightx1
                        top2 = sprite1.topy1
                        bottom2 = sprite1.bottomy1
                        # First sprite
                        left1 = sprite2.leftx
                        right1 = sprite2.rightx
                        top1 = sprite2.topy
                        bottom1 = sprite2.bottomy
                        # Variables to check if hitboxes from each sprite overlap
                        x_overlap = False
                        y_overlap = False
                        # Check if there is no collision and then reverse it; Do I have to do this with
                        # all the dino hitboxes?
                        if left2 > right1 or right2 < left1:
                            # the cactus and dinosaur don't have overlapping
                            # x's
                            # print("no overlap x")
                            x_overlap = False
                        else:
                            x_overlap = True
                        
                        if bottom2 > top1 or top2 < bottom1:
                            # the cactus and dinosaur don't have overlapping
                            # y's
                            # print("no overlap y")
                            y_overlap = False
                        else:
                            y_overlap = True
                        
                        if x_overlap == True and y_overlap == True:
                            # the player has touched a cactus
                            print("you lose")
                            # exit()
                    else:
                        # No need to check for collisions between cacti and pterodactyls
                        pass'''