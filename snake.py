from turtle import Turtle

MOVE_DISTANCE = 20
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0


class Snake:
    def __init__(self):
        self.segments = []
        for i in range(3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto((i * (-MOVE_DISTANCE), 0))
            self.segments.append(new_segment)
        self.head = self.segments[0]

    def move(self):
        for segment in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment-1].xcor()
            new_y = self.segments[segment-1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != SOUTH:
            self.segments[0].setheading(NORTH)

    def down(self):
        if self.segments[0].heading() != NORTH:
            self.segments[0].setheading(SOUTH)


    def left(self):
        if self.segments[0].heading() != EAST:
           self.segments[0].setheading(WEST)

    def right(self):
        if self.segments[0].heading() != EAST:
            self.segments[0].setheading(EAST)

    def extend(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        new_segment.goto(new_x, new_y)
        self.segments.append(new_segment)
