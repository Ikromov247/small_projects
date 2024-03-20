from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0

        high_score = self.read_from_file()
        if high_score.isnumeric() and eval(high_score) > 0:
            self.high_score = eval(high_score)
        self.color("white")
        self.hideturtle()
        self.up()
        self.goto(-10, 270)
        self.update_score()

    def write_to_file(self, new_text):
        with open("high_score.txt", "r+") as f:
            f.write(f"{new_text}")

    def read_from_file(self):
        with open("high_score.txt", "r+") as f:
            file_content = f.read()
            return file_content

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
