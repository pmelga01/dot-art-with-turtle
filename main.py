from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")


# Draw a Square
# for i in range(4):
#      tim.forward(100)
#      tim.right(90)

# Draw a dashed line
# for _ in range(5):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

# Draw a shape given the number of sides
def drawShape(num_sides):
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(360/num_sides)

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
for i in range (3, 11):
    drawShape(i)





screen = Screen()
screen.exitonclick()