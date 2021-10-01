import turtle 

#creating a window
win=turtle.Screen()
win.bgcolor("white")
win.setup(700,650,370,0)
win.title("Finget Spinner")
win.bgpic("C:\\Users\\abhiram\\Desktop\\relax.png")

#text turtle
text=turtle.Turtle()
text.color("#000000")
text.hideturtle()

#spinner turtle
s=turtle.Turtle()
s.color("black")
s.hideturtle()
s.width(20)

#function to turn finget spinner
state = {'turn': 0}
def spinner():
    s.clear()
    angle = state['turn']/10
    s.right(angle)
    s.forward(100)
    s.dot(120, 'red')
    s.dot(30,'white')
    s.back(100)
    s.right(120)
    s.forward(100)
    s.dot(120, 'green')
    s.dot(30,'white')
    s.back(100)
    s.right(120)
    s.forward(100)
    s.dot(120, 'blue')
    s.dot(30,'white')
    s.back(100)
    s.right(120)
    win.update()

#function to perform animation
def animate():
    if state['turn']>0:
        state['turn']-=1
    spinner()
    win.ontimer(animate, 20)
    
#function to increment speed 
def flick():
    state['turn']+=10
    
#adding instructions to start the spinner
text.penup()
text.goto(10,-170)
text.pendown()
text.write("PRESS SPACEBAR TO PLAY",font="Roman 20 bold",align="center")

s.penup()
s.goto(0,120)
s.pendown()

win.tracer(False)
win.onkey(flick, 'space')
win.listen()
animate()
turtle.done()
