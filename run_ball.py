import random
import turtle
import ball

class BouncingSimulate:
    def __init__(self, num_balls):
        self.num_balls = num_balls
        self.ball_list = []
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        canvas_width = turtle.screensize()[0]
        canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * canvas_width

        for i in range(self.num_balls):
            x = random.randint(-1*canvas_width + self.ball_radius, canvas_width - self.ball_radius)
            y = random.randint(-1*canvas_height + self.ball_radius, canvas_height - self.ball_radius)
            vx = random.randint(1, 0.01*canvas_width)
            vy = random.randint(1, 0.01*canvas_height)
            ball_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self.ball_list.append(ball.Ball(self.ball_radius, x, y, vx, vy, ball_color))

    def run(self):
        while True:
            turtle.clear()
            for i in range(self.num_balls):
                self.ball_list[i].draw_circle()
                self.ball_list[i].move_circle()
            turtle.update()
        turtle.done()

num_balls = int(input("Number of balls to simulate: "))
my_simulator = BouncingSimulate(num_balls)
my_simulator.run()
