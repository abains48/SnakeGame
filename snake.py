import turtle
from turtle import Turtle
STARTING = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
LEFT=180
UP=90
RIGHT=0
DOWN=270
turtle.colormode(255)
class Snake:

    def __init__(self):
        self.segments = []
        self.create()
        self.head=self.segments[0]

    def create(self):
        for position in STARTING:
            self.adder(position)

    def adder(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        # new_segment.color(57,93,56)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)

        self.segments.clear()
        self.create()
        self.head=self.segments[0]

    def extend_tail(self):
        self.adder(self.segments[-1].position())


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
