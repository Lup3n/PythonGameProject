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
        self.enemies = len(enemies)

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
        self.enemies = len(self.enemies)

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


def welcome_screen(canvas):
    test.draw(canvas)
    test.update()
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


test = Back(Vector(WIDTH, HEIGHT))


def background(canvas,camera):
    for i in range(WIDTH // (WIDTH // 30)):
        for j in range(HEIGHT // (HEIGHT // 30)):
            canvas.draw_polyline(
                [(i * (WIDTH / 30)-camera.x, j * (HEIGHT / 30)-camera.y), (i * (WIDTH / 30)-camera.x + WIDTH / 30, j * (HEIGHT / 30)-camera.y),
                 (i * (WIDTH / 30)-camera.x + WIDTH / 30, j * (HEIGHT / 30)-camera.y + HEIGHT / 30)], 1, 'gray')


def draw(canvas):
    if WELCOME:
        welcome_screen(canvas)
    else:
        background(canvas, camera)
        level.draw(canvas, player, camera, enemies)

        inter.update()

        player.update(camera)
        player.weapon.current_mag[0] = 200
        player.draw(canvas)
        player_gui.draw(canvas)
        player_gui.update()
        for x in enemies:
            x.update(camera)

            x.draw(canvas)

        if len(enemies) < 4:
            #currently no enemies added
            # enemies.append(Enemy(Vector(random.randint(100, WIDTH-100), random.randint(100, HEIGHT-100)), player, player_gui))
            pass

        if len(player.entities) > 0:
            for i in player.entities:
                if player.entities:

                    if i.pos.x > WIDTH + 10 or i.pos.x < -10 or i.pos.y > HEIGHT + 10 or i.pos.y < -10:
                        player.entities.remove(i)
                        break

                i.draw(canvas)
                i.update()

                for j in enemies:
                    if j.hitbox[0].x <= i.hitbox[0].x <= j.hitbox[1].x and \
                            j.hitbox[0].y <= i.hitbox[0].y <= j.hitbox[1].y or \
                            j.hitbox[0].x <= i.hitbox[1].x <= j.hitbox[1].x and \
                            j.hitbox[0].y <= i.hitbox[1].y <= j.hitbox[1].y:
                        j.health -= 50
                        j.bleed()
                        if j.health <= 0:
                            enemies.remove(j)
                            player.kills += 1
                            break
                        player.entities.remove(i)
                        break

            # canvas.draw_polyline([[player.entities[i].hitbox[0].x, player.entities[i].hitbox[0].y], [player.entities[i].hitbox[1].x, player.entities[i].hitbox[0].y], [player.entities[i].hitbox[1].x, player.entities[i].hitbox[1].y]], 20, 'Blue')



player = Player(Vector(200, 200))
level = Level()
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
