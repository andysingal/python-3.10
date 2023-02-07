from turtle import Turtle,Screen

timmy = Turtle()
timmy.shape("turtle")
timmy. color("red")

#goto a certain co-ordinate
timmy.penup()
timmy.goto(50,75)
timmy.pendown()

timmy.forward(100)
timmy.left(90)
timmy.forward(200)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(200)
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)
screen = Screen()
screen.exitonclick()

