from turtle import Turtle, Screen
from player import Player
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")

player1 = Player(-350, 0)
player2 = Player(350, 0)
ball = Ball()
scoreboard = Scoreboard(player1, player2)

screen.listen()
screen.onkey(player1.down, "s")
screen.onkey(player1.up, "w")
screen.onkey(player2.down, "Down")
screen.onkey(player2.up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    ball.move()
    ball.bounce_y()
    ball.bounce_x(player1)
    ball.bounce_x(player2)

    if ball.xcor() > 390.0:
        scoreboard.increase_score("player1 won")
        ball.reset()
        player1.reset(-350, 0)
        player2.reset(350, 0)
    elif ball.xcor() < -390.0:
        scoreboard.increase_score("player2 won")
        ball.reset()
        player1.reset(-350, 0)
        player2.reset(350, 0)



screen.exitonclick()

