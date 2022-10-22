import turtle

turtle.showturtle()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def move_clockwise():
    turtle.right(10)
    turtle.heading()
    turtle.forward(10)


def move_anticlockwise():
    turtle.left(10)
    turtle.heading()
    turtle.forward(10)


def clear_screen():
    turtle.reset()


turtle.listen()
turtle.onkey(key = "w", fun=move_forward)
turtle.onkey(key="s", fun=move_backward)
turtle.onkey(key="a", fun=move_clockwise)
turtle.onkey(key="d", fun=move_anticlockwise)
turtle.onkey(key="c", fun=clear_screen)
turtle.exitonclick()