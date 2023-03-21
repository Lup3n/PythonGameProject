import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from libs.vector import Vector
from libs.clock import Clock
import math

from libs.spritesheet import get_path


class Gui:
    def __init__(self, player, frame):
        self.player = player
        self.frame = frame
        self.gun_img = simplegui.load_image(get_path("gun.png"))
        self.source_size = Vector(self.gun_img.get_width(), self.gun_img.get_height())
        self.source_centre = Vector(self.source_size.x / 2, self.source_size.y / 2)
        self.dest_size = Vector(100, 100)
        self.pos = Vector(frame.x - (self.dest_size.x / 2), frame.y - (self.dest_size.y / 2))

        self.guiItems = []
        self.mags = self.player.weapon.current_mag[0]
        self.bullets = self.player.weapon.bullets_left
        self.bullet_img = simplegui.load_image(get_path("bullet.png"))
        self.kills = 0
        self.message = []
        self.canvas = None
        self.damaged_effect = False

        self.blood = simplegui.load_image(get_path("blood.png"))
        self.blood_source_size = Vector(self.blood.get_width(), self.blood.get_height())
        self.blood_source_centre = Vector(self.blood_source_size.x / 2, self.blood_source_size.y / 2)
        self.blood_pos = Vector(self.player.pos.x, self.player.pos.y)
        self.timer = Clock(0)
        self.effects = []

        self.debug = False

    def draw(self, canvas):
        # Gun Stuff
        self.guiItems.append(canvas.draw_image(self.gun_img,
                                               (self.source_centre.x, self.source_centre.y),
                                               (self.source_size.x, self.source_size.y),
                                               (self.pos.x, self.pos.y),
                                               (self.dest_size.x, self.dest_size.y)))

        canvas.draw_text((str(self.mags) + "/" + str(self.bullets)), (self.pos.x - 50, self.pos.y - 50), 24, 'White')
        canvas.draw_text(("Kills: " + str(self.kills)), (10, 20), 24, 'White')
        canvas.draw_text(("Health: " + str(self.player.health)), (self.frame.x - 120, 20), 24, 'White')
        canvas.draw_text(("Lives: " + str(self.player.lives)), (self.frame.x - 120, 50), 24, 'White')
        if self.damaged_effect:
            canvas.draw_image(self.blood,
                              (self.blood_source_centre.x, self.blood_source_centre.y),
                              (self.blood_source_size.x, self.blood_source_size.y),
                              self.player.pos.get_p(),  # now blood is on user
                              (100, 100))

        if self.debug:
            y = math.sin(self.player.rot)
            x = math.cos(self.player.rot)
            # canvas.draw_text(("Pos: " + str((round(self.player.pos.x, 1), round(self.player.pos.y, 1)))), (self.player.pos.x + 40, self.player.pos.y+ 50), 24, 'White')
            # canvas.draw_text(("Vel: " + str(self.player.vel.get_p())), (self.player.pos.x + 40, self.player.pos.y+ 90), 24, 'White')
            # canvas.draw_line()

            source = self.player.weapon.bullet_spawn_pos.copy()
            end = source.copy().add(Vector(x * 2000, y * 2000))
            canvas.draw_line((source.x, source.y), (end.x, end.y), 2, 'Red')

    def update(self):
        self.timer.tick()
        self.mags = self.player.weapon.current_mag[0]
        self.bullets = self.player.weapon.bullets_left
        self.kills = self.player.kills
        if self.timer.transition(100):
            if self.damaged_effect:
                self.damaged_effect = False
                self.blood_pos = Vector(self.player.pos.x, self.player.pos.y)
