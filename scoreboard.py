from turtle import Turtle

FONT=('Courier',24,'bold')
ALIGNMENT="center"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color('white')
        self.ht()
        self.penup()
        self.goto(0,270)
        self.pendown()
        self.score=0
        file=open("data.txt")
        contents=file.read()
        self.high_score=int(contents)
        file.close()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",False,ALIGNMENT,font=FONT)

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt","w") as filer:
                filer.write(f"{self.high_score}")


        self.score=0
        self.write_score()


    #def gameover(self):
       # self.goto(0,15)
       # self.clear()
       # self.write("GAME OVER!!!", False, ALIGNMENT, font=FONT)
       # self.goto(0,-15)
       # self.write("Your Score was: " + str(self.score), False, ALIGNMENT, font=FONT)



    #def clearing(self):
        #self.clear()