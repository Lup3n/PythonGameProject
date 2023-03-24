import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from libs.vector import Vector
import os


def get_path(file: str) -> str:
    """
    Function that gets a file name and looks for the absolute path inside the ``assets`` directory,
    removing the need to change the path from user to user
    :param file: filename that the user needs to find
    :return: A string representing the absolute path to the given file
    """
    cur_path = os.path.dirname(__file__)
    s = '..\\assets\\' + file
    p = os.path.join(cur_path, s)
    return p


class Spritesheet:
    """
    Class that handles the animations of object such as: Player and Enemy.
    Mostly modifiable, it allows editing the frame rate, rotation, and position of the animation occuring.
    """
    def __init__(self, image: str, pos: Vector, columns: int, rows: int, frame_duration: int, rot: int | float = 0, size:
    tuple[int, int] = (100, 100)) -> None:
        """
        Constructor to initialise the sprite-sheet for an animation
        :param image: String name of the image.
        :param pos: Position where to draw the animation.
        :param columns: Amount of columns in the image.
        :param rows: Amount of rows in the image.
        :param frame_duration: How long should a frame stay on the screen before going to the next one.
        :param rot: Rotation of the image
        :param size: Size of the image
        """
        self.img = simplegui.load_image(get_path(image))

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

        #Starting frame position
        self.frame_index = [0, 0]
        self.frame_duration = frame_duration
        self.frame_clock = 0
        self.frame_reverse = False
        self.size = size

    def update_index(self):
        """
        Update the frame position
        """
        self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
        if self.frame_index[0] == 0:
            self.frame_index[1] = (self.frame_index[1] + 1) % self.rows

    def draw(self, canvas):
        """
        Draws the correct frame on screen
        :param canvas: Canvas on which to draw the sprites
        """
        self.frame_clock += 1
        if self.frame_clock % self.frame_duration == 0:
            self.update_index()

        source_centre = (
            self.frame_width * self.frame_index[0] + self.frame_centre_x,
            self.frame_height * self.frame_index[1] + self.frame_centre_y
        )
        source_size = (self.frame_width, self.frame_height)

        canvas.draw_image(
            self.img,
            source_centre, source_size,
            (self.dest_centre.x, self.dest_centre.y), self.size, self.rot
        )
