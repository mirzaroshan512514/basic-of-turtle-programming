import turtle
import colorsys

# Create screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.width(2)

# Color settings
num_colors = 36
hue = 0

# Draw spiral with changing colors
for i in range(360):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.color(color)
    t.forward(i)
    t.left(59)
    hue += 1/num_colors

# Finish
turtle.done()