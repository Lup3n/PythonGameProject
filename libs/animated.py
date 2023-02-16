import random
from libs.vector import Vector

class Back:
    def __init__(self, frame):
        self.frame = frame
        self.colours = ["#212121", "#353535"]
        self.x = 0
        self.bars = []
        self.done = False


    def draw(self, canvas):
        if len(self.bars) != 40:
            for i in range((self.frame.x // 40)+1):
                self.bars.append(canvas.draw_line([self.x-40*i, 0], [self.x-40*i, self.frame.y], 40, self.colours[i%2]))
        for i in range(len(self.bars)):
            self.bars[i]


    def update(self):
        if self.done == False:
            self.x += 16
            if self.x == self.frame.x:
                self.done = True
