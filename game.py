import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from libs.player import Player
from libs.vector import Vector
from libs.keyboard import Keyboard
from libs.interaction import Interaction
from libs.gui import Gui
from libs.enemy import Enemy
from libs.animated import Back
from libs.wall import Wall
from libs.level import Level
from libs.spritesheet import get_path
from libs.collisions import Collisions
import math
import random
from libs.camera import Camera

WIDTH = 1280
HEIGHT = 720
WELCOME = True
counter = 0
enemies = []


class Game:
    def __init__(self):
        # Basic Prerequisites
        self.player = Player(Vector(WIDTH / 2, HEIGHT / 2))
        self.keyboard = Keyboard()
        self.inter = Interaction(player, keyboard, Vector(WIDTH, HEIGHT))
        self.gui = Gui(self.player, Vector(WIDTH, HEIGHT))
        self.enemies = []

        # Map Shizz
        self.background = None

        # Stat Variables
        self.kills = 0
        self.enemies_count = len(enemies)

    def start(self):
        self.player.lives = 3
        self.player.health = 100
        self.pos = Vector(100, 100)

    def background(self):
        print("Background")

    def run(self, canvas):
        self.update()
        self.draw(canvas)

    def spawn_enemy(self):
        self.enemies.append(Enemy(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)), self.player,
                            self.gui)

    def value_update(self):
        self.enemies_count = len(self.enemies)

    def update(self):
        self.background()
        self.inter.update()
        self.player.update()
        self.gui.update()

    def draw(self, canvas):
        self.player.draw(canvas)
        self.gui.draw(canvas)
        for x in self.enemies:
            x.update()
            x.draw(canvas)


def mouse_handler(position):
    global WELCOME
    if WELCOME:
        WELCOME = False
    else:
        print("meow")


test = Back(Vector(WIDTH, HEIGHT))
intro = simplegui.load_image(get_path("newSprites\\IntroductionPage.png"))

pos = Vector(-640, HEIGHT // 2)


def update_ground(canvas):
    global pos

    if pos.x + intro.get_width() / 2 < WIDTH:
        inc = Vector(16, 0)
        pos = pos.add(inc)

    canvas.draw_image(intro,
                      (intro.get_width() / 2, 360),
                      (intro.get_width(), intro.get_height()),
                      pos.get_p(),
                      (1280, 720))


def welcome_screen(canvas):
    # test.draw(canvas)
    # test.update()
    update_ground(canvas)
    """
    canvas.draw_text('Welcome To ZoomBie',
                     ((WIDTH / 2) - (frame.get_canvas_textwidth('Welcome To ZoomBie', 50) // 2), 40),
                     50, 'White', 'sans-serif')

    text = ["The objective of the game is to try to survive all the waves and kill the zombies", "The Controls are:",
            "W - Up", "S - Down", "A - Left", " D - Right", "Right Arrow = Rotate Clockwise",
            " Left Arrow = Rotate AntiClockwise"]
    for i in range(len(text)):
        canvas.draw_text(text[i],
                         ((WIDTH // 40), 80 * (i + 1)),
                         25, 'White', 'sans-serif')

    canvas.draw_text('Click To Begin',
                     ((WIDTH - (frame.get_canvas_textwidth('Click To Begin', 50)) * 2), HEIGHT // 2),
                     50, 'White', 'sans-serif')
    """

    pass


pavement = simplegui.load_image(get_path("newSprites\\pavement.png"))
new_pavement = simplegui.load_image(get_path("newSprites\\Pavement_tiles.png"))


def background(canvas, camera):
    ws = len(level.map[0])
    hs = len(level.map)

    x = (ws-1) * 95
    y = (hs-1) * 95
    # for i in range(WIDTH // (WIDTH // 30)):
    #    for j in range(HEIGHT // (HEIGHT // 30)):
    # canvas.draw_image(pavement,
    #                  (pavement.get_width() / 2, pavement.get_height() / 2),
    #                  (512,512),
    #                  (i, j),
    #                  (30, 30))
    # canvas.draw_polyline(
    #    [(i * (WIDTH / 30) - camera.x, j * (HEIGHT / 30) - camera.y),
    #     (i * (WIDTH / 30) - camera.x + WIDTH / 30, j * (HEIGHT / 30) - camera.y),
    #     (i * (WIDTH / 30) - camera.x + WIDTH / 30, j * (HEIGHT / 30) - camera.y + HEIGHT / 30)], 1, 'gray')

    canvas.draw_image(new_pavement,
                      (new_pavement.get_width() / 2, new_pavement.get_height() / 2),
                      (new_pavement.get_width(), new_pavement.get_height()),
                      (x/2 - camera.x, y/2 - camera.y),
                      (ws*95, hs*95))


def draw(canvas):
    if WELCOME:
        welcome_screen(canvas)
    else:
        background(canvas, camera)

        inter.update()

        player.update(camera)
        player.weapon.current_mag[0] = 200  # infinite ammo
        player.draw(canvas)
        player.draw_health_bar(canvas)
        player_gui.draw(canvas)
        player_gui.update()
        level.draw(canvas, player, camera, enemies)
        for x in enemies:
            x.update(camera)
            x.draw(canvas)

        if len(enemies) < 4:
            # currently no enemies added
            # enemies.append(Enemy(Vector(random.randint(100, WIDTH-100), random.randint(100, HEIGHT-100)), player, player_gui))
            pass

        if len(player.entities) > 0:
            for bullet in player.entities:
                bullet.draw(canvas)
                bullet.update()
                if bullet.off_screen():
                    player.entities.remove(bullet)
                    del bullet
                    break

                for j in enemies:
                    if j.got_shot(bullet):
                        j.health -= 50
                        j.bleed()
                        if j.health <= 0:
                            enemies.remove(j)
                            player.kills += 1
                            break
                        player.entities.remove(bullet)
                        break

                # i.draw(canvas)
                # i.update()

            # canvas.draw_polyline([[player.entities[i].hitbox[0].x, player.entities[i].hitbox[0].y], [player.entities[i].hitbox[1].x, player.entities[i].hitbox[0].y], [player.entities[i].hitbox[1].x, player.entities[i].hitbox[1].y]], 20, 'Blue')


player = Player(Vector(200, 200))
level = Level(player)
keyboard = Keyboard()
camera = Camera(player)
player_gui = Gui(player, Vector(WIDTH, HEIGHT))
player.gui = player_gui
inter = Interaction(player, keyboard, Vector(WIDTH, HEIGHT))
enemies.append(Enemy(Vector(300, 300), player, player_gui))
enemies.append(Enemy(Vector(900, 200), player, player_gui))
enemies.append(Enemy(Vector(500, 500), player, player_gui))
frame = simplegui.create_frame("Game", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keyboard.keyDown)
frame.set_keyup_handler(keyboard.keyUp)
frame.set_mouseclick_handler(mouse_handler)
frame.start()
