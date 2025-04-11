from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')


class ScoreBoard(Turtle):

    def __init__(self,):
        super().__init__()
        self.score = 0
        with open("./day_20,21,24/data.txt") as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.print_score()
        self.hideturtle()

    def print_score(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}",align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.print_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./day_20,21,24/data.txt", mode= 'w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.print_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align = ALIGNMENT, font = FONT)