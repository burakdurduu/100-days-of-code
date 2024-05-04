import turtle as t
import random
import colorgram
# pip install colorgram.py

colors = colorgram.extract("hirst.jpg", 30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    rgb_colors.append(rgb)
print(rgb_colors)

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]
t.colormode(255)
tim = t.Turtle()
x = -250
tim.penup()
tim.hideturtle()


def position_turtle():
    global x
    tim.goto(-250, x)
    x += 50


def more_dots():  
    for i in range(9):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.forward(50)
        tim.color(random.choice(color_list))
        tim.dot(20)


for i in range(10):
    position_turtle()
    more_dots()


screen = t.Screen()
screen.exitonclick()
