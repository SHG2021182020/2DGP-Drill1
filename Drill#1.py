import turtle

turtle.shape("turtle")

def Wmove():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def Amove():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
    
def Smove():
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()
    
def Dmove():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()
    
def resetgame():
    turtle.reset()
    
turtle.onkey(Wmove, 'w')
turtle.onkey(Amove, 'a')
turtle.onkey(Smove, 's')
turtle.onkey(Dmove, 'd')
turtle.onkey(resetgame, 'Escape')
turtle.listen()
