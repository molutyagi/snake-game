from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self) -> None:
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.pu()
        new_turtle.goto(position)
        self.all_snakes.append(new_turtle)

    def extend(self):
        # add a new snake segment
        self.add_snake(self.all_snakes[-1].position())

    def move(self):
        for turtle_num in range(len(self.all_snakes) - 1, 0, -1):
            new_x = self.all_snakes[turtle_num - 1].xcor()
            new_y = self.all_snakes[turtle_num - 1].ycor()
            self.all_snakes[turtle_num].goto(new_x, new_y)
        self.head.fd(MOVE_DIST)

    def w(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def s(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def a(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def d(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        for snake in self.all_snakes:
            snake.goto(1000, 1000)
        self.all_snakes.clear()
        self.create_snake()
        self.head = self.all_snakes[0]
