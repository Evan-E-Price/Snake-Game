from Snake import Snake
from turtle import Screen
from Food import Food
from Scoreboard import Scoreboard
import time



screen = Screen()
screen.title("Snake")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

game_is_running = True

while game_is_running:
    snake.move()
    screen.update()
    time.sleep(0.1)


    # Eat food
    if snake.head.distance(food) < 15:
        food.new_loc()
        snake.add_food()
        scoreboard.increase_score()

    # Wall collision
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        game_is_running = False
        scoreboard.game_over()

    # Tail collision
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_running = False
            scoreboard.game_over()

screen.exitonclick()
