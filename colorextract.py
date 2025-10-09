import random

import colorgram
import turtle as t

# Extract 6 colors from an image.
rgb_color=[]
colors = colorgram.extract('image.jpg', 6)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_color.append(new_color)

print(rgb_color)
t.colormode(255)
color_list= [(248, 248, 245), (242, 249, 245), (242, 245, 250), (250, 245, 248), (238, 221, 116), (19, 112, 190)]
tim = t.Turtle()
#tim.speed("fastest")
tim.shape("turtle")

for _ in range(10):
    for _ in range(10):
        tim.dot(20 , random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()

    tim.setheading(90)
    tim.penup()
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    tim.pendown()

screen= t.Screen()
screen.exitonclick()