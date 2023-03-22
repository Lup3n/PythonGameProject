import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from libs.player import Player
from libs.vector import Vector
from libs.keyboard import Keyboard
from libs.interaction import Interaction
from libs.gui import Gui
from libs.enemy import Enemy
from libs.animated import Back
from libs.wall import Wall
from libs.statusbar import StatusBar
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
        self.running = False # Can be used in the future to pause the game if needed
        self.welcome_screen = True # Determine whether the introduction should be shown
        self.player = Player(Vector(200, 200))
        self.keyboard = Keyboard()
        self.camera = Camera(self.player)
        self.enemies = []
        self.level = Level(self.player)

        self.statusbar = StatusBar(self.player, Vector(WIDTH, HEIGHT), self.enemies)
        self.inter = Interaction(self.player, self.keyboard, Vector(WIDTH, HEIGHT))
        self.status_bar = StatusBar(self.player, Vector(WIDTH, HEIGHT), self.enemies) 
        self.player_gui = Gui(self.player, Vector(WIDTH, HEIGHT))
        self.player.gui = self.player_gui

        self.intro_pos = Vector(-640, HEIGHT // 2)

    def start(self):
        self.player.lives = 3
        self.player.health = 100
        self.pos = Vector(100, 100)



    def run(self, canvas):
        if self.running and not self.welcome_screen:
            self.update()
            self.draw(canvas)
        else:
            self.introduction(canvas)

    def spawn_enemy(self):
        self.enemies.append(Enemy(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)), self.player,
                            self.gui)

    def value_update(self):
        self.enemies_count = len(self.enemies)
 

    def update(self):
        self.inter.update()
        self.player.update(self.camera)

    def draw(self, canvas):
        self.draw_background(canvas)
        self.player.draw(canvas)
        self.level.draw(canvas, self.player, self.camera, self.enemies)
        for x in self.enemies:
            x.update(self.camera)
            x.draw(canvas)
        self.status_bar.draw(canvas)

        if len(self.player.entities) > 0:
            for bullet in self.player.entities:
                bullet.draw(canvas)
                bullet.update()
                if bullet.off_screen():
                    self.player.entities.remove(bullet)
                    del bullet
                    break

                for j in self.enemies:
                    if j.got_shot(bullet):
                        j.health -= 50
                        j.bleed()
                        if j.health <= 0:
                            self.enemies.remove(j)
                            self.player.kills += 1
                            break
                        self.player.entities.remove(bullet)
                        break
    
    def draw_background(self, canvas):
        new_pavement = simplegui.load_image(get_path("newSprites\\Pavement_tiles.png"))
        ws = len(self.level.map[0])
        hs = len(self.level.map)

        x = (ws-1) * 95
        y = (hs-1) * 95

        canvas.draw_image(new_pavement,
                        (new_pavement.get_width() / 2, new_pavement.get_height() / 2),
                        (new_pavement.get_width(), new_pavement.get_height()),
                        (x/2 - self.camera.x, y/2 - self.camera.y),
                        (ws*95, hs*95))

    def introduction(self, canvas):
        intro = simplegui.load_image(get_path("newSprites\\IntroductionPage.png"))
        if self.intro_pos.x + intro.get_width() / 2 < WIDTH:
            inc = Vector(16, 0)
            self.intro_pos.add(inc)
        canvas.draw_image(intro,
                      (intro.get_width() / 2, 360),
                      (intro.get_width(), intro.get_height()),
                      self.intro_pos.get_p(),
                      (1280, 720))

    def mouse_handler(self, position):
        if self.welcome_screen:
            self.welcome_screen = False
            self.running = True



main = Game()
frame = simplegui.create_frame("Game", WIDTH, HEIGHT)
frame.set_draw_handler(main.run)
frame.set_keydown_handler(main.keyboard.keyDown)
frame.set_keyup_handler(main.keyboard.keyUp)
frame.set_mouseclick_handler(main.mouse_handler)
frame.start()
