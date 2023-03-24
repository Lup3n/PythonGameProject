from libs.vector import Vector
from libs.player import Player


class Camera:
    def __init__(self, target: Player) -> None:
        self.x = target.pos.x
        self.y = target.pos.y
        self.pos = Vector()

    def center_camera(self, vel):
        self.x += vel.x
        self.y += vel.y
