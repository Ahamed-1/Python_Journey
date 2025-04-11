import time
from food import Food
from turtle import Screen
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height = 600, width = 600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

game_ison = True
while game_ison:

    screen.update()
    time.sleep(0.1) # Delays by 0.1 second
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    if not (-280 <= snake.head.xcor() <= 280) or not (-280 <= snake.head.ycor() <= 280):
        score_board.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()