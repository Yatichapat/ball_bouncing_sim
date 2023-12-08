import turtle
import random

class Ball:
    def __init__(self, color, size, x, y, vx, vy):
        self.size = size
        self.color = color
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def draw_circle(self, color, size, x, y):
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()

    def move_circle(self):
        self.x += self.vx
        self.y += self.vy

        canvas_width = turtle.screensize()[0]
        canvas_height = turtle.screensize()[1]

        if abs(self.x + self.vx) > (canvas_width - self.size):
            self.vx = -self.vx

        if abs(self.y + self.vy) > (canvas_height - self.size):
            self.vy = -self.vy

