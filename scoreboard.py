from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("file.txt")as file:
            self.high_score=int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_turtle_score()
    def update_turtle_score(self):
        self.clear()
        self.write(f"Score :{self.score}  High score :{self.high_score} ",align="center", font=("arial", 24, "normal"))
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("file.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.update_turtle_score()

    # def game_over(self):
      #  self.goto(0,0)
       # self.write(f"GAME OVER", align="center", font=("arial", 24, "normal"))

    def update_score(self):
        self.score+=1
        self.update_turtle_score()