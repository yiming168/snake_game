from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

segments = []

for i in range(3):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto((i*(-20),0))
    segments.append(new_segment)








screen.exitonclick()