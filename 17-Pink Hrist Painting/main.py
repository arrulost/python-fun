# import colorgram
import random
import turtle as turtle_module

# rgb_colors = []
# colors = colorgram.extract('image4.jpg', 50)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)


tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed('fastest')
color_list = [(224, 63, 144), (250, 211, 227), (229, 118, 167), (192, 45, 126), (242, 157, 189), (219, 4, 114), (239, 219, 214), (228, 135, 127), (243, 243, 247), (240, 246, 243), (238, 164, 161), (120, 92, 87), (71, 41, 52), (255, 1, 124), (161, 108, 106), (66, 47, 42), (92, 51, 48), (203, 191, 179)]

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.fd(300)
tim.setheading(0)

num_of_dots = 101

for dot_counts in range(1, num_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.fd(50)
    
    if dot_counts % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()



