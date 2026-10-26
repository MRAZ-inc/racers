import random
import json
from pathlib import Path


class Part:
    matrix_name = None

    def __init__(self, name, mass, durability, max_speed, acceleration, handling, quality):
        self.name = name
        self.mass = mass
        self.max_durability = durability
        self.durability = self.max_durability
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.handling = handling
        self.quality = quality
        self.broken = False
        self.broke = False

    def check_durability(self):
        if not self.broken:
            if random.randint(1, 20) > self.quality:
                self.durability -= 1
                if self.durability <= 0:
                    self.broken = True
                    self.broke = True

    def reset(self):
        self.durability = self.max_durability
        self.broke = False
        self.broken = False

    @classmethod
    def get_matrix(cls):
        path = Path("matrix") / f"{cls.matrix_name}.json"

        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

class Engine(Part):
    matrix_name = "engine"

if __name__ == "__main__":
    taet = Part(10, 10, 10, 10)
    print(taet.durability)
    #print(taet.acceleration)
    print(Engine.get_matrix())