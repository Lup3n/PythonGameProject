import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from libs.spritesheet import Spritesheet, get_path
from libs.vector import Vector
from libs.enemy import Enemy
import math
import random

class StatusBar:

    def __init__(self, player, frame, enemies):
        self.player = player
        self.frame = frame
        self.enemies = enemies
        self.health_bar_length = 400
        self.dest_size = Vector(100, 100)
        self.pos = Vector(frame.x - (self.dest_size.x / 2), frame.y - (self.dest_size.y / 2))
        self.health_ratio = self.player.health / self.health_bar_length
        self.lives_bar_length = 90
        self.lives_ratio = self.player.lives / self.lives_bar_length
        self.skull_img = simplegui.load_image(get_path("/skull.png"))
        self.skull_source_size = Vector(self.skull_img.get_width(), self.skull_img.get_height())
        self.skull_source_centre = Vector(self.skull_source_size.x / 2, self.skull_source_size.y / 2)
        self.ammo = simplegui.load_image(get_path("/ammo.png"))
        self.ammo_source_size = Vector(self.ammo.get_width(), self.ammo.get_height())
        self.ammo_source_centre = Vector(self.ammo_source_size.x / 2, self.ammo_source_size.y / 2)
        self.zombie = simplegui.load_image(get_path("/zombie.png"))
        self.zombie_source_size = Vector(self.zombie.get_width(), self.zombie.get_height())
        self.zombie_source_centre = Vector(self.zombie_source_size.x / 2, self.zombie_source_size.y / 2)
        self.status = simplegui.load_image(get_path("/status.png"))
        self.status_source_size = Vector(self.status.get_width(), self.status.get_height())
        self.status_source_centre = Vector(self.status_source_size.x / 2, self.status_source_size.y / 2)
        self.count = 0

    def draw(self, canvas):
        transition_width = 0
        transition_color = "Red"

        status_dest_size = (self.status_source_size.x * 2.5, self.status_source_size.y)

        canvas.draw_image(self.status,
                          (self.status_source_centre.x, self.status_source_centre.y),
                          (self.status_source_size.x , self.status_source_size.y),
                          (630, 870),
                          status_dest_size)

        zombie_dest_size = (self.zombie_source_size.x // 12, self.zombie_source_size.y // 12)

        canvas.draw_image(self.zombie,
                          (self.zombie_source_centre.x, self.zombie_source_centre.y),
                          (self.zombie_source_size.x, self.zombie_source_size.y),
                          (600, 685),
                          zombie_dest_size)

        ammo_dest_size = (self.ammo_source_size.x // 6, self.ammo_source_size.y // 6)

        canvas.draw_image(self.ammo,
                          (self.ammo_source_centre.x, self.ammo_source_centre.y),
                          (self.ammo_source_size.x, self.ammo_source_size.y),
                          (1025, 650),
                          ammo_dest_size)

        skull_dest_size = (self.skull_source_size.x // 5, self.skull_source_size.y // 5)

        canvas.draw_image(self.skull_img,
                          (self.skull_source_centre.x, self.skull_source_centre.y),
                          (self.skull_source_size.x, self.skull_source_size.y),
                          (100, 650),
                          skull_dest_size)

        enemy_count = len(self.enemies)
        canvas.draw_text(":" + str(enemy_count), (640, 700), 40, 'Red')
        canvas.draw_text(":" + str(self.player.kills), (200, 675), 70, 'Red')
        canvas.draw_text(":" + (str(self.player.weapon.current_mag[0])) + "/" + str(self.player.weapon.bullets_left), (self.frame.x - 200, self.frame.y - 50),
                         60, 'Red')

        health_bar_width = int(self.player.health / self.health_ratio)
        if self.player.health > 0:
            health_bar = [(430, 580), (430 + health_bar_width, 580), (430 + health_bar_width, 580 + 25),
                          (430, 580 + 25)]
        else:
            health_bar = [(430, 580), (430, 580), (430, 580 + 25), (430, 580 + 25)]

        max_health_bar = [(430, 580), (430 + self.health_bar_length, 580), (430 + self.health_bar_length, 580 + 25),
                          (430, 580 + 25)]


        canvas.draw_polygon(max_health_bar, 0, "Grey", "Grey")
        canvas.draw_polygon(health_bar, 0, "Red", "Red")
        canvas.draw_polygon([(430, 580), (430 + self.health_bar_length, 580),
                             (430 + self.health_bar_length, 580 + 25), (430, 580 + 25)], 3, "White")
        canvas.draw_text(str(int(self.player.health)), (625, 600), 22, "White", 'sans-serif')

        lives_bar_width = int(self.player.lives / self.lives_ratio)
        lives_bar = [(590, 620), (590 + lives_bar_width, 620), (590 + lives_bar_width, 620 + 25), (590, 620 + 25)]
        max_lives_bar = [(590, 620), (590 + self.lives_bar_length, 620), (590 + self.lives_bar_length, 620 + 25),
                         (590, 620 + 25)]
        transition_bar = [(590 + lives_bar_width, 620), (590 + lives_bar_width + transition_width, 620),
                          (590 + lives_bar_width + transition_width, 620 + 25), (590 + lives_bar_width, 620 + 25)]

        canvas.draw_polygon(max_lives_bar, 0, "Grey", "Grey")
        canvas.draw_polygon(lives_bar, 0, "Red", "Red")
        canvas.draw_polygon(transition_bar, 0, transition_color, transition_color)
        canvas.draw_polygon([(590, 620), (590 + self.lives_bar_length, 620),
                             (590 + self.lives_bar_length, 620 + 25), (590, 620 + 25)], 3, "White")

        canvas.draw_line((590 + 30, 620), (590 + 30, 620 + 25), 3, 'White')
        canvas.draw_line((590 + 60, 620), (590 + 60, 620 + 25), 3, 'White')

