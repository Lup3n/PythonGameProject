from libs.vector import Vector
import math

class Interaction:
    def __init__(self, object, keyboard, frame):
        self.object = object
        self.keyboard = keyboard
        self.frame = frame

    def update(self):
        for x in self.keyboard.keys:
            if x["down"] == True:
                if self.object.pos.x > self.frame.x+25:
                    self.object.pos = Vector(0, self.object.pos.y)
                elif self.object.pos.x < -25:
                    self.object.pos = Vector(self.frame.x, self.object.pos.y)
                elif self.object.pos.y < -25:
                     self.object.pos = Vector(self.object.pos.x, self.frame.y)
                elif self.object.pos.y > self.frame.y+25:
                    self.object.pos = Vector(self.object.pos.x, 0)



                if "vec" in x:
                    self.object.vel.add(x["vec"])
                elif "rot" in x:
                    if round(self.object.rot, 2) > 2*math.pi:
                        self.object.rot -= 2*math.pi
                    elif round(self.object.rot, 2) < -2*math.pi:
                        self.object.rot += 2*math.pi
                    self.object.rot += x["rot"]
                elif "action" in x:
                    if x["action"] == "shoot":
                        self.object.weapon.fire()
                        x["down"] = False
                    elif x["action"] == "reload":
                        self.object.weapon.reload()
                        x["down"] = False



