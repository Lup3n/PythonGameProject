import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from libs.vector import Vector
from libs.spritesheet import get_path


class Wall:
    def __init__(self, pos: tuple[int, int], border: int, i=0) -> None:
        """
        Constructor to initalize a wall
        :param pos: position of the wall on the map
        :param border: thickness of teh border
        :param i:
        """
        self.border = border
        self.pos = Vector(pos[0], pos[1])
        self.length = 50
        self.safe_offset = 10
        if i == 1:
            self.img = simplegui.load_image(get_path("levelSprites/wallAdrian.jpg"))
        else:
            self.img = simplegui.load_image(get_path("levelSprites/wall.png"))
        self.hitbox = (
            Vector(self.pos.x - self.length - self.safe_offset, self.pos.y - self.length - self.safe_offset),
            Vector(self.pos.x + self.length, self.pos.y + self.length + self.safe_offset))

        self.margin = 5

    def draw(self, canvas, camera):
        # Update hitbox position
        self.hitbox = (
            Vector(self.pos.x - self.length - self.safe_offset - camera.x,
                   self.pos.y - self.safe_offset - self.length - camera.y),
            Vector(self.pos.x + self.length + self.safe_offset - camera.x,
                   self.pos.y + self.length + self.safe_offset - camera.y))

        # Draw sprite of wall
        canvas.draw_image(self.img, (self.img.get_width() / 2, self.img.get_height() / 2),
                          (self.img.get_width(), self.img.get_height()),
                          (self.pos.x - camera.x, self.pos.y - camera.y),
                          (100, 100))

    # canvas.draw_polyline([(self.hitbox[0].x, self.hitbox[0].y), (self.hitbox[1].x, self.hitbox[0].y)], 12, 'Blue')
    # canvas.draw_polyline([(self.hitbox[1].x, self.hitbox[0].y), (self.hitbox[1].x, self.hitbox[1].y)], 12, 'Purple')
    # canvas.draw_polyline([(self.hitbox[1].x, self.hitbox[1].y), (self.hitbox[0].x, self.hitbox[1].y)], 12, 'Red')
    # canvas.draw_polyline([(self.hitbox[0].x, self.hitbox[1].y), (self.hitbox[0].x, self.hitbox[0].y)], 12, 'Green')

    def check_collision(self, instance) -> None:
        """
        Checks whether the instance is colliding within the wall
        :param instance: player/zombie to check as example
        """
        push_power = 1
        if self.check1(instance) and self.check2(instance) and self.check3(instance):
            instance.vel.add(Vector(0, push_power))

        elif self.check3(instance) and self.check4(instance) and self.check1(instance):
            instance.vel.add(Vector(0, -push_power))

        elif self.check2(instance) and self.check3(instance) and self.check4(instance):
            instance.vel.add(Vector(-push_power, 0))

        elif self.check4(instance) and self.check1(instance) and self.check2(instance):
            instance.vel.add(Vector(push_power, 0))

    def check1(self, instance):
        #
        if self.hitbox[0].x - self.margin <= instance.hitbox[0].x <= self.hitbox[1].x + self.margin:
            return True

    def check2(self, instance):
        return self.hitbox[0].y - self.margin <= instance.hitbox[0].y <= self.hitbox[1].y + self.margin

    def check3(self, instance):
        return self.hitbox[0].x - self.margin <= instance.hitbox[1].x <= self.hitbox[1].x + self.margin

    def check4(self, instance):
        return self.hitbox[0].y - self.margin <= instance.hitbox[1].y <= self.hitbox[1].y + self.margin
