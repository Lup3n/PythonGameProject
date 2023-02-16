from libs.bullet import Bullet
from libs.vector import  Vector
import math
class Weapon:
    def __init__(self, player, type, mags, magsize):
        self.player = player
        self.type = type
        self.magsize = magsize
        self.bullets_left = magsize * mags
        self.current_mag = [magsize, self.bullets_left - magsize]
        self.bullet_spawn_pos = self.rotate_point(self.player.pos.x+50, self.player.pos.y+25, self.player.rot, self.player.pos.x, self.player.pos.y)

    def rotate_point(self, x, y, angle, player_x, player_y):
        # Define the player's position as the origin
        x_origin, y_origin = player_x, player_y

        # Translate the point to be rotated so that the origin is at the center of rotation
        x -= x_origin
        y -= y_origin

        # Rotate the point by the desired angle
        x_rotated = x * math.cos(angle) - y * math.sin(angle)
        y_rotated = x * math.sin(angle) + y * math.cos(angle)

        # Translate the rotated point back to its original position
        x_rotated += x_origin
        y_rotated += y_origin

        return Vector(x_rotated, y_rotated)

    def reload(self):
        if self.current_mag[0] < self.magsize and self.bullets_left > 0:
            max_bullets = self.magsize - self.current_mag[0]
            if self.bullets_left >= self.magsize:
                self.current_mag[0] += max_bullets
                self.bullets_left -= max_bullets
                self.current_mag[1] -= max_bullets
            else:
                self.current_mag[0] += self.bullets_left
                self.current_mag[1] -= self.bullets_left
                self.bullets_left -= self.bullets_left



    def fire(self):
        if self.bullets_left > 0 and self.current_mag[0] > 0:
            self.current_mag[0] -= 1
            self.player.entities.append(Bullet(self.player.rot, self.bullet_spawn_pos))




