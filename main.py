from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0), "blue", screen)  # Right paddle is BLUE
l_paddle = Paddle((-350, 0), "red", screen)  # Left paddle is RED

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.listen()

# Right Paddle Controls
screen.onkeypress(r_paddle.start_moving_up, "Up")
screen.onkeyrelease(r_paddle.stop_moving_up, "Up")
screen.onkeypress(r_paddle.start_moving_down, "Down")
screen.onkeyrelease(r_paddle.stop_moving_down, "Down")

# Left Paddle Controls
screen.onkeypress(l_paddle.start_moving_up, "w")
screen.onkeyrelease(l_paddle.stop_moving_up, "w")
screen.onkeypress(l_paddle.start_moving_down, "s")
screen.onkeyrelease(l_paddle.stop_moving_down, "s")



WINNING_SCORE = 5

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

# Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# Collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.x_move > 0:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 and ball.x_move < 0:
        ball.bounce_x()

# Miss with right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

# Miss with left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Dynamic color changes
    if scoreboard.l_score == WINNING_SCORE or scoreboard.r_score == WINNING_SCORE:
        game_is_on = False

        # Determine winner and set colors dynamically
        if scoreboard.l_score == WINNING_SCORE:
            winner_text = "Red Player Wins!"
            winner_color = "red"
        else:
            winner_text = "Blue Player Wins!"
            winner_color = "blue"

        # GAME OVER uses the winner's color
        scoreboard.goto(0, 0)
        scoreboard.color(winner_color)
        scoreboard.write("GAME OVER", align="center", font=("Courier", 36, "bold"))

        # Winner message appears below, in the same color
        scoreboard.goto(0, -50)
        scoreboard.write(winner_text, align="center", font=("Courier", 24, "bold"))





screen.exitonclick()