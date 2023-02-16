import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from libs.vector import Vector

class Spritesheet:
    def __init__(self, imgurl, dims, pos,columns, rows, frame_duration, rot=0):
        self.img = simplegui.load_image(imgurl)

        self.width = dims.x
        self.height = dims.y
        self.columns = columns
        self.rows = rows
        self.dest_centre = pos
        self.rot = rot

        self.frame_width = dims.x / columns
        self.frame_height = dims.y / rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2
        self.frame_index = [0,0]
        self.frame_duration = frame_duration
        self.frame_clock = 0
        self.frame_reverse = False

    def update_index(self):
        self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
        if self.frame_index[0] == 0:
            self.frame_index[1] = (self.frame_index[1] + 1) % self.rows

    def draw(self, canvas):
        self.frame_clock += 1
        if (self.frame_clock % self.frame_duration == 0):
                self.update_index()

        source_centre = (
            self.frame_width * self.frame_index[0] + self.frame_centre_x,
            self.frame_height * self.frame_index[1] + self.frame_centre_y
        )
        source_size = (self.frame_width, self.frame_height)

        dest_size = (100, 100)

        canvas.draw_image(
            self.img,
            source_centre, source_size,
            (self.dest_centre.x, self.dest_centre.y), dest_size, self.rot
        )