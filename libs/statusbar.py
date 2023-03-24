import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from libs.spritesheet import get_path
from libs.vector import Vector
from libs.player import Player


class StatusBar:

    def __init__(self, player: Player, frame, enemies) -> None:
        """
        Constructor for the StatusBar class
        :param player: Player instance to access health and ammunition of the player
        :param frame: A Vector Instance of the screen size.
        :param enemies: list of enemies currently on screen
        """
        self.player = player
        self.frame = frame
        self.enemies = enemies
        self.health_bar_length = 400
        self.dest_size = Vector(100, 100)
        self.pos = Vector(frame.x - (self.dest_size.x / 2), frame.y - (self.dest_size.y / 2))
        self.health_ratio = self.player.health / self.health_bar_length
        self.lives_bar_length = 90
        self.lives_ratio = self.player.lives / self.lives_bar_length
        self.skull_img = simplegui.load_image(get_path("StatusBarSprites/skull.png"))
        self.skull_source_centre = Vector(self.skull_img.get_width() / 2, self.skull_img.get_height() / 2)
        self.ammo = simplegui.load_image(get_path("StatusBarSprites/ammo.png"))
        self.ammo_source_centre = Vector(self.ammo.get_width() / 2, self.ammo.get_height() / 2)
        self.zombie = simplegui.load_image(get_path("StatusBarSprites/zombie.png"))
        self.zombie_source_centre = Vector(self.zombie.get_width() / 2, self.zombie.get_height() / 2)
        self.status = simplegui.load_image(get_path("StatusBarSprites/status.png"))
        self.status_source_centre = Vector(self.status.get_width() / 2, self.status.get_height() / 2)
        self.count = 0

    def draw(self, canvas):
        # Background
        status_dest_size = (self.status.get_width() * 2.5, self.status.get_height())
        canvas.draw_image(self.status,
                          (self.status_source_centre.x, self.status_source_centre.y),
                          (self.status.get_width(), self.status.get_height()),
                          (630, 870),
                          status_dest_size)

        self.enemies_remaining(canvas)

        self.show_ammo(canvas)

        self.display_kills(canvas)

        self.health_bar(canvas)

        self.show_lives(canvas)

    def health_bar(self, canvas):
        heath_perc = self.player.health / 100.0
        ratio = (int(255 * (1 - heath_perc)), int(255 * heath_perc), 0)
        health_colour = 'rgb' + str(tuple(ratio))

        health_bar_width = int(self.player.health / self.health_ratio)
        max_health_bar = [(430, 580), (430 + self.health_bar_length, 580), (430 + self.health_bar_length, 580 + 25),
                          (430, 580 + 25)]
        canvas.draw_polygon(max_health_bar, 0, "Grey", "Grey")

        if self.player.health > 0:
            health_bar = [(430, 580), (430 + health_bar_width, 580), (430 + health_bar_width, 580 + 25),
                          (430, 580 + 25)]
            canvas.draw_polygon(health_bar, 0, "red", health_colour)

        canvas.draw_polygon([(430, 580), (430 + self.health_bar_length, 580),
                             (430 + self.health_bar_length, 580 + 25), (430, 580 + 25)], 3, "White")
        canvas.draw_text(str(int(self.player.health)), (625, 600), 22, "White", 'sans-serif')

    def display_kills(self, canvas):
        skull_dest_size = (self.skull_img.get_width() // 5, self.skull_img.get_height() // 5)

        canvas.draw_image(self.skull_img,
                          (self.skull_source_centre.x, self.skull_source_centre.y),
                          (self.skull_img.get_width(), self.skull_img.get_height()),
                          (100, 650),
                          skull_dest_size)
        canvas.draw_text(":" + str(self.player.kills), (200, 675), 70, 'Red')

    def enemies_remaining(self, canvas):
        zombie_dest_size = (self.zombie.get_width() // 12, self.zombie.get_height() // 12)

        canvas.draw_image(self.zombie,
                          (self.zombie_source_centre.x, self.zombie_source_centre.y),
                          (self.zombie.get_width(), self.zombie.get_height()),
                          (600, 685),
                          zombie_dest_size)

        enemy_count = len(self.enemies)
        canvas.draw_text(":" + str(enemy_count), (640, 700), 40, 'Red')

    def show_ammo(self, canvas):
        ammo_dest_size = (self.ammo.get_width() // 6, self.ammo.get_height() // 6)

        canvas.draw_image(self.ammo,
                          (self.ammo_source_centre.x, self.ammo_source_centre.y),
                          (self.ammo.get_width(), self.ammo.get_height()),
                          (1025, 650),
                          ammo_dest_size)
        canvas.draw_text(":" + (str(self.player.weapon.current_mag[0])) + "/" + str(self.player.weapon.bullets_left),
                         (self.frame.x - 200, self.frame.y - 50),
                         60, 'Red')

    def show_lives(self, canvas):
        transition_width = 0
        transition_color = "Red"

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
