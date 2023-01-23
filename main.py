import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# Square
#for _ in range(4):
#    timmy_the_turtle.forward(100)
#    timmy_the_turtle.left(90)

# Dashed line -- chalalenge 2
#for _ in range(15):
#    tim.forward(10)
#    tim.penup()
#    tim.forward(10)
#    tim.pendown()

#colors = ["green yellow", "orange", "firebrick", "medium violet red", "magenta", "dark violet", "navajo white", "blue"]
#directions = [0, 90, 180, 270]
#tim.pensize(15)
#tim.speed(4)

# random shapes -- challenge 3

#def draw_shape(num_sides):
#    angle = 360 / num_sides
#    for _ in range(num_sides):
#        tim.forward(100)
#        tim.right(angle)

#for shape_side_n in range(3, 11):
#    tim.color(random.choice(colors))
#    draw_shape(shape_side_n)

# random walk -- challenge 4

#for _ in range(100):
#    tim.color(random_color())
#    tim.forward(25)
#    tim.setheading(random.choice(directions))

# random Spirograph -- challenge 5

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph((5))

screen = t.Screen()
screen.exitonclick()
