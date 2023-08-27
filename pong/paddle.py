from turtle import Turtle

L_POSITION = (-350,0)
R_POSITION = (350,0)

class Paddle(Turtle):
 
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.shapesize(5, 1)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def reset(self,position):
        self.goto(position)
