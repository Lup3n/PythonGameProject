class Clock:
    def __init__(self, time):
        self.time = time

    def tick(self):
        self.time += 1

    def transition(self, duration):
        return (self.time % duration == 0)