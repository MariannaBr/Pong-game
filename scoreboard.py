from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, player1, player2):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score1 = 0
        self.score2 = 0
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(str(self.score1) + " : " + str(self.score2), align="center", font=("Arial", 80, "normal"))

    def increase_score(self, player):
        if player == "player2 won":
            self.score2 += 1
        elif player == "player1 won":
            self.score1 += 1
        self.clear()
        self.update_scoreboard()