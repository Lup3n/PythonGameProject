from libs.spritesheet import Spritesheet, get_path
from libs.vector import Vector
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from libs.clock import Clock
from Settings import PATH
import math



class Enemy:
    def __init__(self, pos, player, gui):
        self.pos = pos
        self.health = 100
        self.rot = 0
        self.vel = Vector()
        self.gui = gui
        self.player = player
        self.hitbox = (
            Vector(self.pos.x-50, self.pos.y-50),
            Vector(self.pos.x+50, self.pos.y+50))
        self.counter = 0
        self.sheet = "sheets\\zombie.png"
        self.sprite = Spritesheet(self.sheet, self.pos, 17, 1, 4, self.rot)
        self.bleeding = False
        self.alive = True


        self.timer = Clock(0)
        self.blood = simplegui.load_image(get_path("blood.png"))
        self.blood_source_size = Vector(self.blood.get_width(), self.blood.get_height())
        self.blood_source_centre = Vector(self.blood_source_size.x / 2, self.blood_source_size.y / 2)
        self.blood_pos = Vector(self.pos.x, self.pos.y)

    def draw(self, canvas):
        if self.bleed:
            canvas.draw_image(self.blood,
                              (self.blood_source_centre.x, self.blood_source_centre.y),
                              (self.blood_source_size.x, self.blood_source_size.y),
                              (self.blood_pos.x, self.blood_pos.y),
                              (100, 100))
        self.sprite.draw(canvas)
        # Draws hit box
        # canvas.draw_polyline([(self.hitbox[0].x, self.hitbox[0].y), (self.hitbox[1].x, self.hitbox[0].y)], 12, 'Blue')
        # canvas.draw_polyline([(self.hitbox[1].x, self.hitbox[0].y), (self.hitbox[1].x, self.hitbox[1].y)], 12, 'Purple')
        # canvas.draw_polyline([(self.hitbox[1].x, self.hitbox[1].y), (self.hitbox[0].x, self.hitbox[1].y)], 12, 'Red')
        # canvas.draw_polyline([(self.hitbox[0].x, self.hitbox[1].y), (self.hitbox[0].x, self.hitbox[0].y)], 12, 'Green')


    def lookat(self):
        self.rot = math.atan2(self.pos.y - self.player.pos.y, self.pos.x - self.player.pos.x) - math.pi  # Some reason their backs look at you so i just do a 180

    def follow(self):
        self.vel.add((Vector(self.player.pos.x - self.pos.x, self.player.pos.y - self.pos.y)).normalize())

    def bleed(self):
        self.timer.time = 0
        self.bleeding = True


    def update(self):
        if self.alive:
            self.lookat()
            self.follow()

        self.timer.tick()
        self.hitbox = (Vector(self.pos.x - 50, self.pos.y - 50), Vector(self.pos.x + 50, self.pos.y + 50))
        if self.health <= 0:
            self.alive = False
            self.player.kills += 1
        self.hitbox = (Vector(self.pos.x - 50, self.pos.y - 50), Vector(self.pos.x + 50, self.pos.y + 50))
        if self.counter % 30 == 0:
            if self.hitbox[0].x <= self.player.hitbox[0].x <= self.hitbox[1].x and \
                self.hitbox[0].y <= self.player.hitbox[0].y <= self.hitbox[1].y or \
                self.hitbox[0].x <= self.player.hitbox[1].x <= self.hitbox[1].x and\
                self.hitbox[0].y <= self.player.hitbox[1].y <= self.hitbox[1].y:
                self.player.health -= 5
                self.player.gui.damaged_effect = True

        self.pos.add(self.vel)
        self.sprite.dest_centre = self.pos
        self.vel.multiply(0.50)
        self.sprite.rot = round(self.rot, 3)
        if self.timer.transition(50):
            if self.bleeding:
                self.bleeding = False
        self.counter += 1

    # TODO: add collision to wall as player
