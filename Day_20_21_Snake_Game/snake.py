from turtle import Turtle,Screen
POSITIONS = [(0,0),(-20,0),(-40,0)]
Move_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake():

    def __init__(self) :
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]


    def create_snake(self):
        for  position in POSITIONS:
            self.add_segment(position)
    
    def add_segment(self,position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segment_list.append(new_segment)

    def extend(self):
        self.add_segment(self.segment_list[-1].position())

    def move(self):
        for seg_num in range(len(self.segment_list) - 1, 0, -1):
            x = self.segment_list[seg_num - 1].xcor()
            y = self.segment_list[seg_num - 1].ycor()
            self.segment_list[seg_num].goto(x, y)
        self.segment_list[0].speed('fastest')
        self.segment_list[0].forward(Move_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)

    
    def right(self):
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)

    
    def left(self):
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)
    
    def down(self):
        if self.head.heading() != UP :
            self.head.setheading(DOWN)

        