import turtle as t
import random
tim = t.Turtle()
# for i in range(15):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
# c = 0
# for i in range(3,11):
#     draw_shape(i)
#     colours = ["red", "yellow", "blue", "orange"]
#     tim.pencolor(colours[c])
#     i += 1
#     if c + 1 == 4:
#         c = 0
#     else:
#         c += 1


t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# tim.pensize(1)
tim.speed(0)

# for i in range(100):
#     direction =[0, 90, 180, 270]
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

# Circle

for i in range(72):
    tim.circle(175)
    tim.left(5)
    tim.color(random_color())

screen = t.Screen()
screen.exitonclick()
