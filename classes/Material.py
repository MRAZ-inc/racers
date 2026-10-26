from dataclasses import dataclass

@dataclass
class Material:
    name: str
    mass: float
    durability: float
    max_speed: float
    acceleration: float
    handling: float

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(other, Material):
            return NotImplemented
        return self.name == other.name