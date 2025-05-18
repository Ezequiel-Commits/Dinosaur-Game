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
    """====================== Initiating my classes =========================="""
    
    dinosaurObject = dinosaur.Dinosour(0,0)
    dinosaurObject.draw()
    
    tapestryObject = tapestry.Tapestry(nOfCacti = 200, tapestryLength = 20000)
    tapestryObject.generate()
    
    animationManagerObject = animationManager.AnimationManager(dinosaurObject, tapestryObject)
    animationManagerObject.run()
    """====================== STUDENT CODE ENDS =========================="""
    
    # Do not edit
    window.mainloop()

main()