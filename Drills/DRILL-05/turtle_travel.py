import turtle

def move_up():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def move_down():
    turtle.stamp()
    turtle.setheading(-90)
    turtle.forward(50)

def move_left():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)

def move_right():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

def restart():
    turtle.reset()

turtle.shape("turtle")

turtle.onkey(move_right,'d')
turtle.onkey(move_left,'a')
turtle.onkey(move_up,'w')
turtle.onkey(move_down,'s')
turtle.onkey(restart, 'Escape')
turtle.listen()

