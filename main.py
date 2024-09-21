from turtle import Turtle, Screen
import time

class Paddle:
    def __init__(self):
        self.a = Turtle()
        self.a.penup()
        self.a.shape("square")
        self.a.shapesize(stretch_wid=5, stretch_len=1)
        self.a.color("white")
        self.a.goto(350, 0)

    def up(self):
        y = self.a.ycor() + 20
        self.a.goto(self.a.xcor(), y)

    def down(self):
        z = self.a.ycor() - 20
        self.a.goto(self.a.xcor(), z)

class PaddleE(Paddle):
    def __init__(self):
        super().__init__()
        self.a.goto(-350, 0)

class Ball(Turtle):
    def __init__(self):
        self.a = Turtle()
        self.a.shape("circle")
        self.a.penup()
        self.a.color("white")
        self.x = 10
        self.y = 10

    def move(self):
        x = self.a.xcor() + self.x
        y = self.a.ycor() + self.y
        self.a.goto(x, y)

    def collision(self):
        if self.a.ycor() > 280 or self.a.ycor() < -280:
            self.y *= -1

    def pad_col(self, paddle, paddle_e):
        if self.a.distance(paddle.a) < 50 and self.a.xcor() > 320 or self.a.distance(paddle_e.a) < 50 and self.a.xcor() < -320:
            self.x *= -1

    def reset(self):
        self.a.goto(0, 0)
        self.x = 10
        self.y = 10

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score1 = 0
        self.score2 = 0
        self.score_board = self.clone()
        self.score_board.goto(-350, 250)
        self.score_board.write(f"score:{self.score1}", move=False, align="center", font=("Arial", 15, "normal"))
        self.score_board.goto(350, 250)
        self.score_board.write(f"score:{self.score2}", move=False, align="center", font=("Arial", 15, "normal"))

    def increase1(self):
        self.score_board.clear()
        self.score1 += 1
        self.score_board.goto(-350, 250)
        self.score_board.write(f"score:{self.score1}", move=False, align="center", font=("Arial", 15, "normal"))
        self.score_board.goto(350, 250)
        self.score_board.write(f"score:{self.score2}", move=False, align="center", font=("Arial", 15, "normal"))

    def increase2(self):
        self.score_board.clear()
        self.score2 += 1
        self.score_board.goto(-350, 250)
        self.score_board.write(f"score:{self.score1}", move=False, align="center", font=("Arial", 15, "normal"))
        self.score_board.goto(350, 250)
        self.score_board.write(f"score:{self.score2}", move=False, align="center", font=("Arial", 15, "normal"))

b = Screen()
b.tracer(0)
pad = Paddle()
padd = PaddleE()
bal = Ball()
scor = Score()
b.update()
b.listen()
b.onkey(key="Up", fun=pad.up)
b.onkey(key="Down", fun=pad.down)
b.onkey(key="w", fun=padd.up)
b.onkey(key="s", fun=padd.down)
b.setup(width=800, height=600)
b.bgcolor("black")
b.title("Ping Pong")
end = False
while True:
    b.update()
    time.sleep(0.1)
    bal.move()
    bal.collision()
    bal.pad_col(pad, padd)
    if bal.a.xcor() > 400:
        scor.increase1()
        bal.reset()
    elif bal.a.xcor() < -400:
        scor.increase2()
        bal.reset()
b.exitonclick()