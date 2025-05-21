import turtle
from datetime import datetime
from watch import Watch

class DigitalWatch(Watch):
    def __init__(self, x=0, y=0, is_24_hour_format=True):
        super().__init__(x, y)
        self.writer = turtle.Turtle()
        self.writer.speed(0)
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.goto(self.x, self.y)
        self.is_24_hour_format = is_24_hour_format

    def toggle_format(self):
        """Перемикає формат часу (12/24 години)."""
        self.is_24_hour_format = not self.is_24_hour_format
        self.update_time()

    def update_time(self):
        """Оновлює відображення цифрового часу."""
        now = datetime.now()
        if self.is_24_hour_format:
            time_string = now.strftime("%H:%M:%S")
        else:
            time_string = now.strftime("%I:%M:%S %p")

        self.writer.clear()
        self.writer.write(time_string, align="center", font=("Arial", 24, "normal"))
        self.screen.update() 