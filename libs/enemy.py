from libs.spritesheet import Spritesheet, get_path
from libs.vector import Vector
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

from libs.clock import Clock
from libs.camera import Camera
from libs.player import Player


class Enemy:
    def __init__(self, pos, player: Player, gui):
        """

        :param pos: starting position of the Enemy
        :param player: Player instance to follow
        :param gui: GUI where it will handle blood drawing and damage input
        """
        self.pos = pos
        self.health = 100
        self.rot = 0
        self.vel = Vector()
        self.gui = gui
        self.player = player
        self.hitbox = (
            Vector(self.pos.x - 50, self.pos.y - 50),
            Vector(self.pos.x + 50, self.pos.y + 50))
        self.counter = 0
        self.sheet = "sheets\\zombie.png"
        self.sprite = Spritesheet(self.sheet, self.pos, 17, 1, 4, self.rot)
        self.temp_animation = Spritesheet("newSprites\\sequence2.png", self.pos, 12, 1, 10, self.rot,
                                          (50, 50))  # new seques
        self.bleeding = False
        self.alive = True

        self.timer = Clock(0)
        self.blood = simplegui.load_image(get_path("blood.png"))
        self.blood_source_size = Vector(self.blood.get_width(), self.blood.get_height())
        self.blood_source_centre = Vector(self.blood_source_size.x / 2, self.blood_source_size.y / 2)
        self.blood_pos = Vector(self.pos.x, self.pos.y)

    def draw(self, canvas):
        """
        Function that draws the enemy instance and the animation.
        It may draw the blood on the instance if ``self.bleeding`` is true.
        :param canvas:
        :return:
        """
        if self.bleeding:
            canvas.draw_image(self.blood,
                              (self.blood_source_centre.x, self.blood_source_centre.y),
                              (self.blood_source_size.x, self.blood_source_size.y),
                              self.pos.get_p(),  # (self.blood_pos.x, self.blood_pos.y),
                              (100, 100))

        self.sprite.draw(canvas)

    def lookat(self):
        """
        Set the enemy rotation to point at the player.
        """
        self.rot = math.atan2(self.pos.y - self.player.pos.y,
                              self.pos.x - self.player.pos.x) - math.pi  # Some reason their backs look at you so i just do a 180

    def follow(self):
        """
        Method that add to the zombie the direction of the player, so the zombie follows the player.
        """
        self.vel.add((Vector(self.player.pos.x - self.pos.x, self.player.pos.y - self.pos.y)).normalize())

    def bleed(self):
        """
        Method to start a countdown and display blood on the enemy.
        """
        self.timer.time = 0
        self.bleeding = True

    def update(self, camera: Camera):
        """

        :param camera: Camera instance to add the offset to the enemy
        """
        # self.hitbox = (Vector(self.pos.x - 50, self.pos.y - 50), Vector(self.pos.x + 50, self.pos.y + 50))
        if self.alive:
            self.lookat()
            self.follow()

        self.timer.tick()
        self.pos.add(-self.player.vel)
        self.hitbox = (Vector(self.pos.x - 20, self.pos.y - 20),
                       Vector(self.pos.x + 20, self.pos.y + 20))

        if self.health <= 0:
            self.alive = False
            self.player.kills += 1
        if self.counter % 30 == 0:
            if self.hitbox[0].x <= self.player.hitbox[0].x <= self.hitbox[1].x and \
                    self.hitbox[0].y <= self.player.hitbox[0].y <= self.hitbox[1].y or \
                    self.hitbox[0].x <= self.player.hitbox[1].x <= self.hitbox[1].x and \
                    self.hitbox[0].y <= self.player.hitbox[1].y <= self.hitbox[1].y:
                self.player.health -= 5
                self.player.gui.damaged_effect = True

        self.pos.add(self.vel)
        self.sprite.dest_centre = self.pos
        self.vel.multiply(0.50)
        self.sprite.rot = round(self.rot, 3)
        # self.temp_animation.rot = round(self.rot, 3)
        if self.timer.transition(200):
            if self.bleeding:
                self.bleeding = False
        self.counter += 1

        if not self.alive:
            del self

    def got_shot(self, bullet) -> bool:
        """
        Checks whether a bullet has hit this instance of zombie or not
        :param bullet: instance of bullet to check collision with
        :return: True if the bullet successfully hit the enemy, else False
        """
        return self.hitbox[0].x <= bullet.hitbox[0].x <= self.hitbox[1].x and \
            self.hitbox[0].y <= bullet.hitbox[0].y <= self.hitbox[1].y or \
            self.hitbox[0].x <= bullet.hitbox[1].x <= self.hitbox[1].x and \
            self.hitbox[0].y <= bullet.hitbox[1].y <= self.hitbox[1].y

    def debug(self, canvas):
        # Draws hit box
        canvas.draw_polyline([(self.hitbox[0].x, self.hitbox[0].y), (self.hitbox[1].x, self.hitbox[0].y)], 12, 'Blue')
        canvas.draw_polyline([(self.hitbox[1].x, self.hitbox[0].y), (self.hitbox[1].x, self.hitbox[1].y)], 12, 'Purple')
        canvas.draw_polyline([(self.hitbox[1].x, self.hitbox[1].y), (self.hitbox[0].x, self.hitbox[1].y)], 12, 'Red')
        canvas.draw_polyline([(self.hitbox[0].x, self.hitbox[1].y), (self.hitbox[0].x, self.hitbox[0].y)], 12, 'Green')
