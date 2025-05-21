import turtle
from datetime import datetime

class Watch:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.screen = turtle.Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("white")
        self.screen.tracer(0) # Вимкнути автоматичне оновлення екрану

    def update_time(self):
        """Оновлює відображення часу."""
        raise NotImplementedError("Підклас має реалізувати цей метод") 