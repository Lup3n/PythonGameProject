from libs.vector import Vector
from libs.player import Player


class Camera:
    def __init__(self, target: Player) -> None:
        self.x = target.pos.x
        self.y = target.pos.y
        self.pos = Vector()

    def center_camera(self, player, vel):
        self.x += vel.x
        self.y += vel.y

    """
        def center_camera(self,player, vel):
        self.pos = Vector(1280 // 2, 720 // 2)
        if player.pos != self.pos:
            vect: Vector = player.pos - self.pos
            self.x += vect.x
            self.y += vect.y
    """