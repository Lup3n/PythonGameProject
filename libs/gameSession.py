from gui import Gui
from interaction import Interaction
from statusbar import StatusBar
from player import Player
from level import Level
from vector import Vector
from keyboard import Keyboard
from camera import Camera


class GameSession:
    def __init__(self, size: tuple[int, int], map):
        self.width = size[0]
        self.height = size[1]
        self.level = Level()

        self.player = Player(Vector(200, 200))
        self.keyboard = Keyboard()
        self.camera = Camera(self.player)
        self.enemies = []
        self.level = Level(self.player)

        self.statusbar = StatusBar(self.player, Vector(self.width, self.height), self.enemies)
        self.inter = Interaction(self.player, self.keyboard, Vector(self.width, self.height))
        self.status_bar = StatusBar(self.player, Vector(self.width, self.height), self.enemies)
        self.player_gui = Gui(self.player, Vector(self.width, self.height))
        self.player.gui = self.player_gui


