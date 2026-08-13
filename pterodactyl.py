import sprite

class Pterodactyl(sprite.Sprite):
    def __init__(self, x, y = 5):
        super().__init__(x)

        self.x = x
        self.y = y

    def draw(self):
        self.turt.penup()
        self.turt.goto(self.x, self.y)
        self.turt.pendown()
        self.turt.setheading(0)
        # Go to the coordinates defined by the tapestry class 
        for i in range(2):
            # Draw a basic cactus
            self.turt.forward(30)
            self.turt.left(90)
            self.turt.forward(10)
            self.turt.left(90)