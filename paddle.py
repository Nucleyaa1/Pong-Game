from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position, color, screen):
        super().__init__()
        self.screen = screen
        self.shape("square")
        self.color(color)  # Set paddle color (Red or Blue)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.moving_up = False
        self.moving_down = False

    def go_up(self):
        if self.moving_up:
            if self.ycor() < 250:
                self.goto(self.xcor(), self.ycor() + 20)
            self.screen.ontimer(self.go_up, 50)

    def go_down(self):
        if self.moving_down:
            if self.ycor() > -250:
                self.goto(self.xcor(), self.ycor() - 20)
            self.screen.ontimer(self.go_down, 50)

    def start_moving_up(self):
        self.moving_up = True
        self.go_up()

    def stop_moving_up(self):
        self.moving_up = False

    def start_moving_down(self):
        self.moving_down = True
        self.go_down()

    def stop_moving_down(self):
        self.moving_down = False
