import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from libs.vector import Vector
from libs.spritesheet import Spritesheet, get_path


class Wall:
    def __init__(self, pos: tuple[int, int], border: int, color: str, i=0) -> None:
        self.border = border
        self.color = color
        self.pos = Vector(pos[0], pos[1])
        self.length = 50
        self.safe_offset = 10
        if i:
            self.img = simplegui.load_image(get_path("wallAdrian.jpg"))
        else:
            self.img = simplegui.load_image(get_path("wall.png"))
        self.hitbox = (
            Vector(self.pos.x - self.length - self.safe_offset, self.pos.y - self.length - self.safe_offset),
            Vector(self.pos.x + self.length, self.pos.y + self.length + self.safe_offset))

        self.margin = 5

    def draw(self, canvas, camera):
        self.hitbox = (
            Vector(self.pos.x - self.length - self.safe_offset - camera.x,
                   self.pos.y - self.safe_offset - self.length - camera.y),
            Vector(self.pos.x + self.length + self.safe_offset - camera.x,
                   self.pos.y + self.length + self.safe_offset - camera.y))
        canvas.draw_image(self.img, (self.img.get_width() / 2, self.img.get_height() / 2),
                          (self.img.get_width(), self.img.get_height()),
                          (self.pos.x - camera.x, self.pos.y - camera.y),
                          (100, 100))

    # canvas.draw_polyline([(self.hitbox[0].x, self.hitbox[0].y), (self.hitbox[1].x, self.hitbox[0].y)], 12, 'Blue')
    # canvas.draw_polyline([(self.hitbox[1].x, self.hitbox[0].y), (self.hitbox[1].x, self.hitbox[1].y)], 12, 'Purple')
    # canvas.draw_polyline([(self.hitbox[1].x, self.hitbox[1].y), (self.hitbox[0].x, self.hitbox[1].y)], 12, 'Red')
    # canvas.draw_polyline([(self.hitbox[0].x, self.hitbox[1].y), (self.hitbox[0].x, self.hitbox[0].y)], 12, 'Green')

    def check_collision(self, player) -> None:
        push_power = 1
        if self.check1(player) and self.check2(player) and self.check3(player):
            player.vel.add(Vector(0, push_power))

        elif self.check3(player) and self.check4(player) and self.check1(player):
            player.vel.add(Vector(0, -push_power))

        elif self.check2(player) and self.check3(player) and self.check4(player):
            player.vel.add(Vector(-push_power, 0))

        elif self.check4(player) and self.check1(player) and self.check2(player):
            player.vel.add(Vector(push_power, 0))

    def check1(self, player):
        if self.hitbox[0].x - self.margin <= player.hitbox[0].x <= self.hitbox[1].x + self.margin:
            return True

    def check2(self, player):
        return self.hitbox[0].y - self.margin <= player.hitbox[0].y <= self.hitbox[1].y + self.margin

    def check3(self, player):
        return self.hitbox[0].x - self.margin <= player.hitbox[1].x <= self.hitbox[1].x + self.margin

    def check4(self, player):
        return self.hitbox[0].y - self.margin <= player.hitbox[1].y <= self.hitbox[1].y + self.margin
