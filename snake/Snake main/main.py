from turtle import Screen

from food import Food
from snake import Snake
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.w, key="w")
screen.onkey(snake.s, key="s")
screen.onkey(snake.d, key="d")
screen.onkey(snake.a, key="a")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect food-snake collision
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#   Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset_snake()

#   Detect collision with tail
    for tail in snake.all_snakes[1:]:
        if tail == snake.head:
            pass
        elif snake.head.distance(tail) < 10:
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()
