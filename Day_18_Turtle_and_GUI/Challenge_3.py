import turtle as t

tim = t.Turtle()
colors = ['red','orange','yellow','green','blue','indigo','violet','purple']
########### Challenge 3 - Draw Shapes ########


    
for i in range(3,11):
    for j in range(i):
        steps = 100
        angle = 360/i
        tim.pencolor(colors[i-3])
        tim.right(angle)
        tim.fd(steps)
screen = t.Screen()
screen.exitonclick()