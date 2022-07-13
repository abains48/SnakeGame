from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()

screen.setup(width=600,height=600)

screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake= Snake()
food=Food()
score=Scoreboard()
screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")

game=True

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_tail()
        score.score+=1
        score.write_score()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.reset()
        snake.reset()
        #game=False
        #score.gameover()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()
            #score.gameover()
            #game=False





screen.exitonclick()
