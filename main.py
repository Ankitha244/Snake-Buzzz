from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("snake buzz")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def play_game():
    global game_is_on
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # when snake collides with foood
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.update_score()

        # collision on food
        if snake.head.xcor() > 284 or snake.head.xcor() < -284 or snake.head.ycor() > 284 or snake.head.ycor() < -284:
            snake.reset()
            game_is_on = False  # Exit the loop

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                snake.reset()
                screen.update()
                screen.clear()
                game_is_on = False
    if not game_is_on:
        pen = Turtle()
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 0)
        if scoreboard.score > scoreboard.high_score:
            pen.write(f"Congratulations!\nNew High Score: {scoreboard.score}", align="center",
                    font=("Arial", 24, "normal"))
        else:
            pen.write(f"Game Over\nYour Score: {scoreboard.score}", align="center", font=("Arial", 24, "normal"))
        time.sleep(2)
        pen.clear()
    scoreboard.reset()

while True:
    game_is_on = True
    screen.listen()
    play_game()
    replay = screen.textinput("Replay", "Do you want to play again? (yes/no)").lower()
    if replay != "yes":
        break
screen.exitonclick()
