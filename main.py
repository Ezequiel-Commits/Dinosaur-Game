# Class Diagram link: https://online.visual-paradigm.com/share.jsp?id=333835383138382d37
# Libraries for later use
import turtle 
import time
import dinosaur
import animationManager
import tapestry 
import cactus

""" ================== STUDENTS: ONLY EDIT WHERE INDICATED ================"""
window  = None
WINX, WINY = 400, 350

def main():
    """Main function"""
    # Do not edit
    def setupWin():
        global window
        # making turtle object
        window = turtle.Screen()
        # setup the screen size
        window.setup(WINX,WINY)
        # set the background color
        window.bgcolor("white")
    
    setupWin()
    """====================== STUDENTS: NAME YOUR TURTLES =========================="""

    # turn off tracer
    turtle.tracer(False)
    turtle.setworldcoordinates(0,0, 400, 350)
    """====================== STUDENT CODE BEGINS =========================="""
    
    dinosaurObject = dinosaur.Dinosour(0,0)
    dinosaurObject.draw()
    
    cactusObject = cactus.Cactus(100)
    cactusObject.draw()
    cactusObject.check_collision(dinosaurObject)
    
    tapestryObject = tapestry.Tapestry(nOfCacti = 200,tapestry_length = 20000)
    tapestryObject.generate()
    
    gameManagerObject = animationManager.AnimationManager(60,1000, \
    dinosaurObject, tapestryObject)
    gameManagerObject.run()
    
    # render the screen
    turtle.update()
    """====================== STUDENT CODE ENDS =========================="""
    
    # Do not edit
    window.mainloop()

main()