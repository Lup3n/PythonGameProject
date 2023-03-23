from libs.spritesheet import Spritesheet
from libs.vector import Vector
from libs.weapon import Weapon


class Player:
    """
    Class representation of the Player.
    It will be responsible for shooting bullets and animating.
    """

    def __init__(self, pos=Vector(0, 0), gui=None):
        """
        :param pos: Starting player position. *Default value is at (0,0)*
        :param gui:
        """
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
        # We add 20 so that the players hitbox is smaller so that it feel easier to play
        self.hitbox = (Vector(self.pos.x - 20, self.pos.y - 20),
                       Vector(self.pos.x + 20,
                              self.pos.y + 20))

        # Sprite
        self.sheet = "sheets\\idle.png"
        self.sprite = Spritesheet(self.sheet, self.pos, 20, 1, 4, self.rot)

        self.weapon = Weapon(self, "handgun", 3, 12)
        self.gui = gui

        # myColor = new Color(2.0f * x, 2.0f * (1 - x), 0);
        self.x = self.health / 100.0
        self.myColor = (2.0 * self.x, 2.0 * (1 - self.x), 0)

    #def animation(self, state):

    #    if state == "idle":
    #        self.sheet = "sheets\\idle.png"
    #    elif state == "move":
    #        self.sheet = "sheets\\move.png"

    def draw(self, canvas):
        """
        Function draws player sprite
        :param canvas: Canvas on which to draw the sprites.
        """
        self.sprite.draw(canvas)
        # canvas.draw_polyline([(self.hitbox[0].x, self.hitbox[0].y), (self.hitbox[1].x, self.hitbox[0].y)], 12, 'Blue')
        # canvas.draw_polyline([(self.hitbox[1].x, self.hitbox[0].y), (self.hitbox[1].x, self.hitbox[1].y)], 12, 'Purple')
        # canvas.draw_polyline([(self.hitbox[1].x, self.hitbox[1].y), (self.hitbox[0].x, self.hitbox[1].y)], 12, 'Red')
        # canvas.draw_polyline([(self.hitbox[0].x, self.hitbox[1].y), (self.hitbox[0].x, self.hitbox[0].y)], 12, 'Green')

    def update(self, camera):
        """
        Update player's variables as the game progresses
        :param camera: Camera instance to update the offset for each
        """
        self.count += 1

        self.sprite.dest_centre = self.pos
        # -150 is so that the player is centered on the yaxis with the status bar
        self.pos = Vector(1280 // 2, (720 // 2) - 150)
        self.vel.multiply(0.85)

        # Update camera offset
        camera.center_camera(self.vel)

        self.sprite.rot = round(self.rot, 3)
        self.weapon.bullet_spawn_pos = self.weapon.rotate_point(self.pos.x + 50, self.pos.y + 25, self.rot, self.pos.x,
                                                                self.pos.y)

        # We add 20 so that the players hitbox is smaller so that it feel easier to play
        self.hitbox = (Vector(self.pos.x - 20, self.pos.y - 20), Vector(self.pos.x + 20, self.pos.y + 20))
