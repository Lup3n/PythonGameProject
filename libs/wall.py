from libs.vector import Vector


class Wall:
    def __init__(self, pos: tuple[int, int], border: int, color: str, direction_wall: str) -> None:
        self.border = border
        self.color = color
        self.pos = Vector(pos[0], pos[1])
        length = 50
        self.hitbox = (
        Vector(self.pos.x - length, self.pos.y - length), Vector(self.pos.x + length, self.pos.y + length))
        """
        if direction_wall == "b":
            self.dir_wall = "b"
            self.edge_r = self.start_p[1] - self.border
            self.normal = Vector(0, -1)
        elif direction_wall =="l":
            self.dir_wall = "l"
            self.edge_r = self.start_p[0] + self.border
            self.normal = Vector(-1, 0)
        elif direction_wall == "t":
            self.dir_wall = "t"
            self.edge_r = self.start_p[1] + self.border
            self.normal = Vector(0, 1)
        elif direction_wall == "b":
            self.dir_wall = "b"
            self.edge_r = self.start_p[1] - self.border
            self.normal = Vector(0, -1)
        else:
            raise ValueError("argument [direction_wall] must be 'r' or 'l'!")
        """

    def draw(self, canvas):
        # canvas.draw_line(self.start_p,self.end_pos,self.border * 2 + 1,self.color)
        canvas.draw_polyline([(self.hitbox[0].x, self.hitbox[0].y), (self.hitbox[1].x, self.hitbox[0].y)], 12, 'Blue')
        canvas.draw_polyline([(self.hitbox[1].x, self.hitbox[0].y), (self.hitbox[1].x, self.hitbox[1].y)], 12, 'Purple')
        canvas.draw_polyline([(self.hitbox[1].x, self.hitbox[1].y), (self.hitbox[0].x, self.hitbox[1].y)], 12, 'Red')
        canvas.draw_polyline([(self.hitbox[0].x, self.hitbox[1].y), (self.hitbox[0].x, self.hitbox[0].y)], 12, 'Green')

    def hit(self, other) -> bool:
        """
        TODO: wall3 check extends 4ever
        Issue: it is not limited to the wall
        :param other: an object instance
        :return: boolean whether it's hitting the wall

        h = False
        match self.dir_wall:
            case "r":
                h = (other.offset_l() >= self.edge_r)  # edited
            case "l":
                h = (other.offset_l() - other.radius * 2 <= self.edge_r)
            case "t":
                h = (other.offset_t() - other.radius * 2 <= self.edge_r)
            case "b":
                h = (other.offset_t() >= self.edge_r) and (self.start_p[0]<other.pos.x<self.end_pos[0])

        return h
        """
        pass

    def newHit(self, player) -> bool:
        if self.check1(player) and self.check2(player):
            player.vel = Vector(0, -0.2)

        elif self.check3(player) and self.check4(player):
            player.vel = Vector(-.2, 0)
            return True
        return False

    def check1(self, player):
        if self.hitbox[0].x <= player.hitbox[0].x <= self.hitbox[1].x:
            return True

    def check2(self, player):
        return self.hitbox[0].y <= player.hitbox[0].y <= self.hitbox[1].y

    def check3(self, player):
        return self.hitbox[0].x <= player.hitbox[1].x <= self.hitbox[1].x

    def check4(self, player):
        return self.hitbox[0].y <= player.hitbox[1].y <= self.hitbox[1].y
