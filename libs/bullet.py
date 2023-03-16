from libs.spritesheet import Spritesheet, get_path
from libs.vector import Vector
import math
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Settings import PATH

WIDTH: int = 1280
HEIGHT: int = 720


def rotate_point(x, y, angle, player_x, player_y):
    # Define the player's position as the origin
    x_origin, y_origin = player_x, player_y

    # Translate the point to be rotated so that the origin is at the center of rotation
    x -= x_origin
    y -= y_origin

    # Rotate the point by the desired angle
    x_rotated = x * math.cos(angle) - y * math.sin(angle)
    y_rotated = x * math.sin(angle) + y * math.cos(angle)

    # Translate the rotated point back to its original position
    x_rotated += x_origin
    y_rotated += y_origin

    return Vector(x_rotated, y_rotated)


class Bullet:
    def __init__(self, rot, gun_pos):
        self.rot = rot
        self.pos = gun_pos
        self.vel = Vector()
        self.speed_multi = 20
        self.hitbox = (Vector(self.pos.x - 1, self.pos.y - 1), Vector(self.pos.x + 1, self.pos.y + 1))
        self.type = "bullet"
        self.damage = 25

        self.img = simplegui.load_image(get_path("bullet.png"))
        self.source_centre = Vector(1024 / 2, 768 / 2)

    def draw(self, canvas):

        y = math.sin(self.rot)
        x = math.cos(self.rot)
        self.vel = Vector(x * self.speed_multi, y * self.speed_multi)
        self.pos.add(self.vel)
        canvas.draw_image(self.img, (self.source_centre.x, self.source_centre.y), (1024, 768),
                          (self.pos.x, self.pos.y), (20, 20), self.rot)

    def hit(self, enemies):
        for j in enemies:
            if j.hitbox[0].x <= self.hitbox[0].x <= j.hitbox[1].x and \
                    j.hitbox[0].y <= self.hitbox[0].y <= j.hitbox[1].y or \
                    j.hitbox[0].x <= self.hitbox[1].x <= j.hitbox[1].x and \
                    j.hitbox[0].y <= self.hitbox[1].y <= j.hitbox[1].y:
                j.health -= self.damage
                j.bleed()

    # TODO:still working on collision with wall
    def wall_collision(self, wall) -> bool:
        # print("it hit a wall omg no way ")
        return wall.check_collision(self)

    def off_screen(self) -> bool:
        return self.pos.x > WIDTH + 10 or self.pos.x < -10 or self.pos.y > HEIGHT + 10 or self.pos.y < -10

    def update(self) -> None:
        self.hitbox = (Vector(self.pos.x - 7.5, self.pos.y - 7.5), Vector(self.pos.x + 7.5, self.pos.y + 7.5))
        self.pos.add(self.vel)
