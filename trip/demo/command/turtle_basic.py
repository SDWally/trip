import turtle

turtle.color("blue", "red")
turtle.begin_fill()

for _ in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.end_fill()
turtle.done()