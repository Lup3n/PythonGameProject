import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from libs.vector import Vector


class Spritesheet:
    def __init__(self, imgurl: str, pos: Vector, columns: int, rows: int, frame_duration: int, rot: int = 0) -> None:
        self.img = simplegui.load_image(imgurl)

        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.columns = columns
        self.rows = rows
        self.dest_centre = pos
        self.rot = rot

        self.frame_width = self.width / columns
        self.frame_height = self.height / rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2
        self.frame_index = [0, 0]
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
