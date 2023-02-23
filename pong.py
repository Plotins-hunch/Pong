from turtle import Turtle, Screen
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('Pong')

def create_line():
    line = Turtle()
    line.color('white')
    line.hideturtle()
    line.pu()
    line.goto(0, -250)
    for i in range((550 // 20)):
        line.setheading(90)
        line.pendown()
        line.forward(10)
        line.penup()
        line.forward(10)


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.pu()
        self.x = 10
        self.y = 10
        self.ballspeed = 0.1

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce(self):
        self.y *= -1

    def hit(self):
        self.x *= -1
        self.ballspeed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.ballspeed = 0.1
        self.hit()

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.pu()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align='center', font=('Courir', 70, 'normal'))
        self.goto(100, 200)
        self.write(self.rscore, align='center', font=('Courir', 70, 'normal'))

    def lpoint(self):
        self.lscore += 1
        self.update_score()

    def rpoint(self):
        self.rscore += 1
        self.update_score()


r_player = Player((350, 0))
l_player = Player((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

create_line()
screen.listen()
screen.onkey(r_player.up, "Up")
screen.onkey(r_player.down, "Down")
screen.onkey(l_player.up, "w")
screen.onkey(l_player.down, "s")


game_on = True
while game_on:
    time.sleep(ball.ballspeed)
    screen.update()
    ball.move()

    if ball.ycor() >= 290 or ball.ycor() <= -280:
        ball.bounce()


    if ball.xcor() > 380:
        ball.reset()
        scoreboard.lpoint()
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.rpoint()
    #detect collision with right paddle
    if ball.distance(r_player) < 50 and ball.xcor() > 320 or ball.distance(l_player) < 50 and ball.xcor() < -320:
        ball.hit()

screen.exitonclick()