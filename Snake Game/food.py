import random
from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('purple')
        self.speed('fast')
        self.shapesize(stretch_len=0.7,stretch_wid=0.7)
        self.refresh()

    def refresh(self):
        random_x = randint(-280,280)
        random_y = randint(-280,280)
        self.goto(random_x,random_y)
