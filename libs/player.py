from libs.spritesheet import Spritesheet
from libs.vector import Vector
from libs.bullet import Bullet
from libs.weapon import Weapon
import math


class Player:
    def __init__(self, pos=Vector(100, 100), gui=None):
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
        self.radius = 40  # test
        self.hitbox = (Vector(self.pos.x - 20, self.pos.y - 20),
                       Vector(self.pos.x + 20,
                              self.pos.y + 20))  # We add 20 so that the players hitbox is smaller so that it feel easier to play

        # Sprite
        self.sheet = "sheets\\idle.png"
        self.sprite = Spritesheet(self.sheet, self.pos, 20, 1, 4, self.rot)

        self.weapon = Weapon(self, "handgun", 3, 12)
        self.gui = gui

        # myColor = new Color(2.0f * x, 2.0f * (1 - x), 0);
        self.x = self.health / 100.0
        self.myColor = (2.0 * self.x, 2.0 * (1 - self.x), 0)

    def animation(self, state):
        if state == "idle":
            self.sheet = "sheets\\idle.png"
        elif state == "move":
            self.sheet = "sheets\\move.png"

    def draw(self, canvas):
        self.sprite.draw(canvas)
        self.draw_health_bar(canvas)
        # [bullet.draw(canvas) for bullet in self.entities]
        # canvas.draw_polyline([(self.hitbox[0].x, self.hitbox[0].y), (self.hitbox[1].x, self.hitbox[0].y)], 12, 'Blue')
        # canvas.draw_polyline([(self.hitbox[1].x, self.hitbox[0].y), (self.hitbox[1].x, self.hitbox[1].y)], 12, 'Purple')
        # canvas.draw_polyline([(self.hitbox[1].x, self.hitbox[1].y), (self.hitbox[0].x, self.hitbox[1].y)], 12, 'Red')
        # canvas.draw_polyline([(self.hitbox[0].x, self.hitbox[1].y), (self.hitbox[0].x, self.hitbox[0].y)], 12, 'Green')

    def update(self, camera):
        self.count += 1

        # print("NUMBER OF BULLETS IN ENTITIES[] IS: " + str(len(self.entities)))

        self.sprite.dest_centre = self.pos

        # self.pos = Vector(1280 // 2, 720 // 2)
        self.vel.multiply(0.85)
        # self.pos.add(self.vel)
        camera.center_camera(self, self.vel)

        self.sprite.rot = round(self.rot, 3)
        self.weapon.bullet_spawn_pos = self.weapon.rotate_point(self.pos.x + 50, self.pos.y + 25, self.rot, self.pos.x,
                                                                self.pos.y)
        self.hitbox = (Vector(self.pos.x - 20, self.pos.y - 20), Vector(self.pos.x + 20,
                                                                        self.pos.y + 20))  # We add 20 so that the players hitbox is smaller so that it feel easier to play

    # Define helper function to draw the health bar
    def draw_health_bar(self, canvas):
        W = 720

        health_bar_width = (W / 2) * (self.health / 100.0)

        canvas.draw_text("Health:", [10, 30], 18, "white")
        canvas.draw_polygon([(10, 10), (10, 40), (W / 2 + 10, 40), (W / 2 + 10, 10)], 2, "white",
                            "blue")

        if self.health >= 0:
            heath_perc = self.health / 100.0
            health_colour = (int(255 * (1 - heath_perc)), int(255 * heath_perc), 0)
            canvas.draw_polygon([(10, 10), (10, 40), (health_bar_width + 10, 40), (health_bar_width + 10, 10)], 2, "white",
                            "rgb" + str(tuple(health_colour)))
