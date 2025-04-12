from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_cor , y_cor):
        super().__init__('square')
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.color('white')
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.x_cor, self.y_cor)
        
    def up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(),new_y)
        

        




    
