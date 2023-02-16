class Collisions:
    def __init__(self, object1, object2):
        self.ob1 = object1
        self.ob2 = object2
        self.collision = False

    def update(self):
        if self.ob1.hit(self.ob2):
            if not self.in_collision:
                self.in_collision = True
                self.ob2.stop(True, True)
            else:
                self.in_collision = False


    def draw(self):
        self.update()

