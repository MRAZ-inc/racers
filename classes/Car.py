from classes.Part import Part


class Car:
    def __init__(self):
        self.max_speed = 0
        self.acceleration = 0
        self.mass = 0
        self.parts = []

    def update_stats(self):
        self.max_speed = 0
        self.acceleration = 0
        self.mass = 0
        for part in self.parts:
            self.mass += part.mass
            self.acceleration += getattr(part, "acceleration", 0)
            self.max_speed += getattr(part, "max_speed", 0)

    def add_part(self, part: Part):
        self.parts.append(part)
        self.update_stats()

    def check_parts(self):
        for part in self.parts:
            part.check_durability()
            if part.broke:
                self.update_stats()
                part.broke = False

    def reset(self):
        for part in self.parts:
            part.reset()

        self.update_stats()