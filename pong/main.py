from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.title('Pong Game')
screen.setup(width = 800, height = 600)
screen.tracer(0)

L_pad = Paddle((-350,0))
R_pad = Paddle((350,0))
ball = Ball()
score = Scoreboard()


screen.listen()

screen.onkey(L_pad.go_up, 'w')
screen.onkey(L_pad.go_down, 's')
screen.onkey(R_pad.go_up, 'Up')
screen.onkey(R_pad.go_down, 'Down')

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(0.005)

    #detect collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(R_pad) < 50 and ball.xcor() > 320 or ball.distance(L_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #detect ball going out from right side
    if ball.xcor() > 380:
        ball.reset()
        L_pad.reset((-350,0))
        R_pad.reset((350,0))
        score.l_score += 1
        score.update()
        screen.update()
        time.sleep(0.2)
    
    #detect ball going our from left side
    if ball.xcor() < -380:
        ball.reset()
        L_pad.reset((-350,0))
        R_pad.reset((350,0))
        score.r_score += 1
        score.update()
        screen.update()
        time.sleep(0.2)

    if score.l_score == score.win_Score or score.r_score == score.win_Score:
        game_on == False
        screen.clear()
        screen.bgcolor("black")
        score.game_over()
        screen.update()
        screen.exitonclick()