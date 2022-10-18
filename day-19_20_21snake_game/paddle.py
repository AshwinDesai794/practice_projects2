from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        # self.x_cor = x_cor
        # self.y_cor = y_cor
        self.goto(x_cor, y_cor)

    # paddle = Turtle()
    # paddle.color("white")
    # paddle.shape("square")
    # paddle.penup()
    # paddle.goto(350, 0)
    # paddle.shapesize(stretch_wid=5, stretch_len=1, outline=None)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

