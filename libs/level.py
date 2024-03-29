import random
from enum import Enum

from libs.wall import Wall
from libs.enemy import Enemy
from libs.vector import Vector


class WallOptions(Enum):
    NORMAL = "levelSprites/wall.png"
    COLOSSUS = "levelSprites/ColossusWanted.jpg"
    ADRIAN = "levelSprites/wallAdrian.jpg"
    COMPSOC = "levelSprites/wallCompSoc.jpg"


class Level:
    def __init__(self, player, map_arr, game) -> None:
        self.map = map_arr
        self.world_map = {}
        self.list_walls: list[Wall, ...] = []
        self.easter_egg_walls = []
        self.enemies_spawn_pos = []
        self.get_map(player)

    def get_map(self, player):
        """
        Function that initialises dictionary that stores every wall location to be drawn on the screen.
        :param player: player instance to set its position
        """

        for j, row in enumerate(self.map):
            for i, value in enumerate(row):
                if value == 1:
                    self.world_map[(i, j)] = value
                    w = Wall((i * 95, j * 95), 4, WallOptions.NORMAL.value)
                    self.list_walls.append(w)
                elif value == 69:
                    self.world_map[(i, j)] = value
                    w = Wall((i * 95, j * 95), 4, random.choice(list(WallOptions)).value)
                    self.list_walls.append(w)
                elif value == 2:
                    self.enemies_spawn_pos.append([i * 95, j * 95])
                elif value == 3:  # not functioning
                    player.pos = Vector((i * 95) - player.pos.x, (j * 95) - player.pos.y)

        # print(self.world_map)

    def draw(self, canvas, player, camera, enemies: list[Enemy]):
        """
        Function to draw the level and the render the wall.
        :param canvas: Canvas on which to draw the sprites.
        :param player: Player instance to check the player's collision with the walls.
        :param camera: Camera instance to offset walls.
        :param enemies: List of enemies on the level to check their collision with the walls.

        """

        """
        For reference. ::
        | A            B
        | +------------+
        | |            |
        | |     .      |
        | |            |
        | +------------+
        | D            C

         . ->would be the center

        wall collision:
        canvas.draw_polygon(((x0-width, y0-width),  # A
                             (x0 + width, y0-width),  # B
                             (x0 + width, y0 + width),  # C
                             (x0-width, y0 + height)),  # D
                            line_width, "Pink", "Red")
        """
        for wall in self.list_walls:
            wall.draw(canvas, camera)
            wall.check_collision(player)
            for enemy in enemies:
                wall.check_collision(enemy)
