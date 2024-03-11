import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

star = turtle.Turtle()
star.speed(0)
star.color("white")
star.hideturtle()

def draw_star(size):
    for _ in range(5):
        star.forward(size)
        star.right(144)

for _ in range(100): //total bintang
    x = random.randint(-screen.window_width()//2, screen.window_width()//2)
    y = random.randint(-screen.window_height()//2, screen.window_height()//2)
    size = random.randint(5, 20)
    
    star.penup()
    star.goto(x, y)
    star.pendown()
    
    draw_star(size)

turtle.done()
