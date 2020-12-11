from turtle import Turtle

class Player(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(x_pos, y_pos)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def reset(self, x_pos, y_pos):
        self.hideturtle()
        self.goto(x_pos, y_pos)
        self.showturtle()