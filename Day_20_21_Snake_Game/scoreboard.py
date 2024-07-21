from turtle import Turtle


class Score(Turtle) :
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        
        self.shape(None)
        self.goto(x=0,y=270)
        self.update_core()

    def game_over(self) :
        self.goto(0,0)
        self.write(f'Game Over', True, align="center")
       

    def update_core(self) :
        self.clear()
        self.write(f'Score : {self.score}', True, align="center")
        self.score += 1
        