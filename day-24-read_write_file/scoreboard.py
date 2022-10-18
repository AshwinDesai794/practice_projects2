from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')



class Scoreboard(Turtle):

    def __init__(self):
        file = open("data.txt")
        super().__init__()
        self.score_num = 0
        self.color("white")
        self.penup()
        self.high_score = int(file.read())
        self.goto(0, 275)
        self.hideturtle()
        self.update_scoreboard()
        file.close()

    def update_scoreboard(self):
        self.clear()  # clear previous score
        self.write(f"score : {self.score_num} High Score : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        # file = open("data.txt", mode="w")
        if self.score_num > self.high_score:
            self.high_score = self.score_num
            with open("data.txt", mode= "w") as data :
                data.write(f"{self.high_score}")
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game OVER! Your Score is: {self.score_num}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score_num += 1
        self.update_scoreboard()


