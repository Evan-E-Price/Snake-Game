from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("red")
        self.speed("fastest")
        self.new_loc()

    def new_loc(self):
        self.goto( random.randrange(-280, 280, 20), random.randrange(-280, 260, 20) )
