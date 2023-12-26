from turtle import Turtle, Screen
from colorthief import ColorThief
import turtle as t
import random

tim = Turtle()
tim.shape("turtle")

ct = ColorThief("bee_puppycat_image1.jpeg")
colors = ct.get_palette(color_count=30)
t.colormode(255)
directions = [0, 90, 180, 270]

color_list = [(47, 54, 78), (238, 199, 165), (158, 78, 100), (199, 119, 119), (243, 233, 220), (148, 165, 145), (195, 110, 82), (89, 167, 164), (235, 152, 104)]


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

# name: drawShape
# description: draw a shape with num_sides (int)
# parameter: num_sides
# return: None
def drawShape(num_sides, steps=100):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.color(randomColor())
        tim.forward(steps)
        tim.right(angle)

# name: randomColor
# description: return a random color
# parameter: None
# return: color (tuple of rgb)
def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0,255)
    return (r, g, b)

# name: randomWalk
# description: draw a random walk
# parameter: pensize (int - default 15)
# return: None
def randomWalk(pensize=15):
    tim.pensize(pensize)
    tim.speed("fastest")
    for _ in range(300):
        tim.color(randomColor())
        tim.forward(25)
        tim.setheading(random.choice(directions))


# name: drawSpirograph
# description: draw a circle with radius
# parameter: radius (int - default 100)
# return: None
def drawSpirograph(radius=100, steps=50):
    for i in range(steps):
        tim.color(randomColor())
        tim.circle(radius)
        tim.setheading(i * (360 / steps))



# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# for i in range (3, 11):
#     drawShape(i)
        

tim.speed("fastest")
# drawSpirograph()

def drawHirstPainting(steps=10):
    tim.penup()
    tim.hideturtle()
    tim.speed("fastest")
    for i in range(steps):
        tim.goto(-300, -300 + i * (650 / steps))
        for j in range(steps):
            tim.color(random.choice(color_list))
            tim.dot(20)
            tim.forward(650 / steps)

drawHirstPainting(10)





screen = Screen()
screen.exitonclick()