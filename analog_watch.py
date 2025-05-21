import turtle
import math
from datetime import datetime
from watch import Watch

class Digit:
    def __init__(self, value, position):
        self.value = value
        self.position = position

    def draw(self, writer):
        writer.penup()
        writer.goto(self.position)
        writer.pendown()
        writer.write(str(self.value), align="center", font=("Arial", 12, "normal"))

class Dial:
    def __init__(self, radius=200):
        self.radius = radius
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.digits = []
        self._create_digits()

    def _create_digits(self):
        center_x, center_y = 0, 0
        for i in range(1, 13):
            angle = 90 - (i * 30)
            rad_angle = math.radians(angle)
            digit_radius = self.radius * 0.85
            x = center_x + digit_radius * math.cos(rad_angle)
            y = center_y + digit_radius * math.sin(rad_angle)
            self.digits.append(Digit(i, (x, y)))

    def draw(self):
        self.turtle.penup()
        self.turtle.goto(0, -self.radius)
        self.turtle.pendown()
        self.turtle.circle(self.radius)

        writer = turtle.Turtle()
        writer.speed(0)
        writer.hideturtle()
        writer.penup()
        for digit in self.digits:
            digit.draw(writer)
        writer.goto(0, 0)

    def clear(self):
        pass

class Hand:
    def __init__(self, length, color, width):
        self.length = length
        self.color = color
        self.width = width
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.color(color)
        self.turtle.shape("classic")
        self.turtle.shapesize(stretch_wid=width/10, stretch_len=length/20)
        self.turtle.penup()
        self.turtle.goto(0, 0)
        self.turtle.pendown()
        self.turtle.setheading(90)

    def set_angle(self, angle):
        self.turtle.setheading(angle)

    def hide(self):
        self.turtle.hideturtle()

    def show(self):
        self.turtle.showturtle()

    def clear(self):
        self.hide()
        self.turtle.goto(0,0)

class AnalogWatch(Watch):
    def __init__(self, x=0, y=0, radius=200):
        super().__init__(x, y)
        self.radius = radius
        self.dial = Dial(self.radius)
        self.hour_hand = Hand(length=radius*0.5, color="black", width=6)
        self.minute_hand = Hand(length=radius*0.7, color="black", width=4)
        self.second_hand = Hand(length=radius*0.8, color="red", width=2)
        self.dial.draw()

    def update_time(self):
        now = datetime.now()
        hour = now.hour % 12
        minute = now.minute
        second = now.second

        hour_angle = 90 - (hour + minute/60) * 30
        minute_angle = 90 - (minute) * 6
        second_angle = 90 - (second) * 6

        self.hour_hand.clear()
        self.minute_hand.clear()
        self.second_hand.clear()

        self.hour_hand.set_angle(hour_angle)
        self.hour_hand.show()

        self.minute_hand.set_angle(minute_angle)
        self.minute_hand.show()

        self.second_hand.set_angle(second_angle)
        self.second_hand.show()

        self.screen.update() 