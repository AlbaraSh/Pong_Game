from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.win_Score = 10
        self.update()

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align = 'center', font = ("Courier", 80 , "normal"))
        self.goto(100,200)
        self.write(self.r_score, align = 'center', font = ("Courier", 80 , "normal"))

    def game_over(self):
        winner = ''
        if self.l_score == self.win_Score:
            winner = 'Left' 
        else:
            winner = 'Right'
        self.goto(0,0)
        self.write(f"GAME OVER, The winner of this game is {winner}", False, "center", ('Arial',24,'normal'))