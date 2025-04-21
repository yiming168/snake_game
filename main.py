from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

segments = []

for i in range(3):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto((i*(-20),0))
    segments.append(new_segment)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x=segments[seg_num -1].xcor()
        new_y=segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)







screen.exitonclick()