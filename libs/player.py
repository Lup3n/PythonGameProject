from libs.spritesheet import Spritesheet
from libs.vector import Vector
from libs.bullet import Bullet
from libs.weapon import Weapon
from Settings import PATH
import math

class Player:
    def __init__(self, pos=Vector(100,100), gui=None):
        # Core Mechanics
        self.pos = pos
        self.vel = Vector()
        self.rot = 0.0
        self.health = 100
        self.lives = 3
        self.weapon = "handgun"
        self.entities = []
        self.count = 0
        self.kills = 0
        self.hitbox = (Vector(self.pos.x-20, self.pos.y-20), Vector(self.pos.x+20, self.pos.y+20)) # We add 20 so that the players hitbox is smaller so that it feel easier to play


        #Sprite
        self.sheet = PATH+"/sheets/idle.png"
        self.sheet_dims = Vector(5060, 216)
        self.sprite = Spritesheet(self.sheet, self.sheet_dims, self.pos, 20, 1, 4, self.rot)

        self.weapon = Weapon(self, "handgun", 3, 12)
        self.gui = gui
    def offset_l(self):
        return self.pos.x - self.radius


    def animation(self, state):
        if state == "idle":
            self.sheet = PATH+"/sheets/idle.png"
            self.sheet_dims = Vector(5060, 216)
        elif state == "move":
            self.sheet = PATH+"/sheets/move.png"
            self.sheet_dims = Vector(5160, 220)

    def draw(self, canvas):
        self.sprite.draw(canvas)
        # canvas.draw_polyline([(self.hitbox[0].x, self.hitbox[0].y), (self.hitbox[1].x, self.hitbox[0].y)], 12, 'Blue')
        # canvas.draw_polyline([(self.hitbox[1].x, self.hitbox[0].y), (self.hitbox[1].x, self.hitbox[1].y)], 12, 'Purple')
        # canvas.draw_polyline([(self.hitbox[1].x, self.hitbox[1].y), (self.hitbox[0].x, self.hitbox[1].y)], 12, 'Red')
        # canvas.draw_polyline([(self.hitbox[0].x, self.hitbox[1].y), (self.hitbox[0].x, self.hitbox[0].y)], 12, 'Green')


    def update(self):
        self.count += 1
        self.pos.add(self.vel)
        self.sprite.dest_centre = self.pos
        self.vel.multiply(0.85)
        self.sprite.rot = round(self.rot, 3)
        self.weapon.bullet_spawn_pos = self.weapon.rotate_point(self.pos.x+50, self.pos.y+25, self.rot, self.pos.x, self.pos.y)
        self.hitbox = (Vector(self.pos.x-20, self.pos.y-20), Vector(self.pos.x+20, self.pos.y+20)) # We add 20 so that the players hitbox is smaller so that it feel easier to play



