from libs.wall import Wall
from libs.enemy import Enemy
from libs.vector import Vector

_ = False
example_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, 1, _, _, _, 1, _, _, _, _, 2, 1],
    [1, _, _, _, 1, 69, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, 2, _, _, _, _, 1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1, 1, 1, _, _, _, _, 1],
    [1, _, 1, _, _, _, _, _, _, _, _, _, _, 1, _, 1],
    [1, 2, 1, _, _, _, _, _, _, _, _, _, _, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

corridor_level = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, 1],
    [1, 3, _, _, _, _, _, _, _, 1, _, _, _, _, _, 2, _, _, _, _, _, _, _, 1, _, _, 2, _, _, 1],
    [1, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 2, _, _, _, _, _, _, 2, 2, _, _, 1],
    [1, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 69, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

test_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, 1, _, _, _, 1, _, _, _, _, _, 1],
    [1, _, _, _, 1,69, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 2, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1, 1, 1, _, _, _, _, 1],
    [1, _, 1, _, _, _, _, _, _, _, _, _, _, 1, _, 1],
    [1, _, 1, _, _, _, _, _, _, _, _, _, _, 1, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Level:
    def __init__(self, player) -> None:
        self.map = test_map
        self.world_map = {}
        self.list_walls: list[Wall, ...] = []
        self.temp_enemies = []
        self.get_map(player)

    def get_map(self, player):

        for j, row in enumerate(self.map):
            for i, value in enumerate(row):
                if value == 1:
                    self.world_map[(i, j)] = value
                    w = Wall((i * 95, j * 95), 4, "pink")
                    self.list_walls.append(w)
                elif value == 69:
                    self.world_map[(i, j)] = value
                    w = Wall((i * 95, j * 95), 4, "pink", 1)
                    self.list_walls.append(w)
                elif value == 2:
                    #TODO: needs to be fixed
                    self.temp_enemies.append(Enemy(Vector((i * 95)-50, (j * 95)-50), player, "Hello"))
                elif value == 3: # not functioning
                    player.pos = Vector((i)*100, j*100)

        # print(self.world_map)

    def draw(self, canvas, player, camera, enemies: list[Enemy]):
        # random data for reference
        width = 50
        height = 50
        x0 = 600
        y0 = 600
        line_width = 5

        """
          A            B
          --------------
          |            |
          |     .      |
          |            |
          -------------- 
          D            C
          . ->would be the center
        
        canvas.draw_polygon(((x0-width, y0-width),  # A
                             (x0 + width, y0-width),  # B
                             (x0 + width, y0 + width),  # C
                             (x0-width, y0 + height)),  # D
                            line_width, "Pink", "Red")
        """
        """
        for pos in self.world_map:
            canvas.draw_polygon(((pos[0] * 100 - width, pos[1] * 100 - width),  # A
                                 (pos[0] * 100 + width, pos[1] * 100 - width),  # B
                                 (pos[0] * 100 + width, pos[1] * 100 + width),  # C
                                 (pos[0] * 100 - width, pos[1] * 100 + height)),  # D
                                line_width, "Pink", "Red")
        """
        if self.temp_enemies != 0:
            enemies.extend(self.temp_enemies)
            self.temp_enemies = []
        for wall in self.list_walls:
            wall.draw(canvas, camera)
            wall.check_collision(player)
            for enemy in enemies:
                wall.check_collision(enemy)
