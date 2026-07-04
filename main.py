# Class Diagram link: https://online.visual-paradigm.com/share.jsp?id=333835383138382d37
# Libraries for later use
import turtle 
import time
import dinosaur
import animationManager
import tapestry 
import cactus

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
    
    # turn off tracer
    turtle.tracer(False)
    turtle.setworldcoordinates(0,0, 400, 350) # Deleting this made my game unplayable. 

    dinosaurObject = dinosaur.Dinosaur(0,0)
    dinosaurObject.draw()
    time1 = time.time()
    time.sleep(1)
    time2 = time.time()
    print(time1 - time2)
    
    tapestryObject = tapestry.Tapestry(nOfCacti = 200, tapestryLength = 20000) #Cacti can be bunched up or not present for a while. 
    tapestryObject.generate()
    
    animationManagerObject = animationManager.AnimationManager(dinosaurObject, tapestryObject)
    animationManagerObject.run()
    
    window.mainloop()

main()
 