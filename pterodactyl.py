import sprite

class Pterodactyl(sprite.Sprite):
    def __init__(self, x):
        super().__init__(x)

        self.x = x
        self.y = 5

    def draw(self):
        # Go to the coordinates defined by the tapestry class 
        self.turt.goto(self.x,0)
        for i in range(2):
            # Draw a basic cactus
            self.turt.forward(30)
            self.turt.left(90)
            self.turt.forward(10)
            self.turt.left(90)