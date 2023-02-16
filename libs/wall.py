class Wall:
    def __init__(self, pos, length, frame):
        self.pos = pos
        self.length = length
        self.frame = frame
        self.border = 2
        self.color = "red"
        self.x = pos.x
        self.edge_r = self.x + self.border


    def draw(self, canvas):
        canvas.draw_line((self.x, 0),
                         (self.x, self.frame.y),
                         self.border * 2 + 1,
                         self.color)

    def hit(self, object):
        return object.offset_l() <= self.edge_r