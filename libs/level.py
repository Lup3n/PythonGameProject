from libs.wall import Wall

_ = False
example_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, 1, _, _, _, 1, _, _, _, _, _, 1],
    [1, _, _, _, 1, 1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1, 1, 1, _, _, _, _, 1],
    [1, _, 1, _, _, _, _, _, _, _, _, _, _, 1, _, 1],
    [1, _, 1, _, _, _, _, _, _, _, _, _, _, 1, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Level:
    def __init__(self) -> None:
        self.map = example_map
        self.world_map = {}
        self.list_walls: list[Wall, ...] = []
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
                    w = Wall((i*100, j*100), 4, "pink")
                    self.list_walls.append(w)
        print(self.world_map)

    def draw(self, canvas, player,camera, enemies):
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
        for wall in self.list_walls:
            wall.draw(canvas, camera)
            wall.newHit(player)
            for enemy in enemies:
                wall.newHit(enemy)

