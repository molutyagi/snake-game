from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 13, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("../data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.pu()
        self.color("white")
        self.goto(0, 282)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write((f"Score: {self.score} | High Score: {self.high_score} "), False,
                   ALIGN, FONT)

    def reset(self) -> None:
        if self.high_score < self.score:
            self.high_score = self.score
            with open("snake/data.txt", mode="w") as data:
                int(data.write(f"{self.high_score}"))

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write((f"GAME OVER!"), False,
    #                ALIGN, FONT)

    # def score_pos(self):

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
