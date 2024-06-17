import turtle as t


tim = t.Turtle()

# ########### Challenge 2 - Draw a Dashed Line ########
# tim.forward(100)

# screen = t.Screen()
# screen.exitonclick()

for i in range(8):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    

screen = t.Screen()
screen.exitonclick()
