import random
from typing import Dict

from classes.Material import Material
from classes.Part import Part, Engine

class Crafter:
    def __init__(self, materials: Dict[Material, int], part_type):
        self.materials = materials
        self.type = part_type

    def pre_calculation(self):
        quality = self.quality_calculator()
        mass = self.linear_stat_calculator("mass")
        #durability = self.linear_stat_calculator("durability")
        return {
            "quality":quality,
            "mass": mass
        }

    def confirm(self):
        part = self.type(self.pre_calculation())
        part.quality += random.randint(-1, 1)
        part.quality = max(1, min(19, part.quality))
        return part


    def quality_calculator(self):
        if not self.materials:
            return 0

        quality = 0
        total_amount = 0
        matrix = self.type.get_matrix()

        for material, amount in self.materials.items():
            if amount <= 0:
                continue

            coefficient = matrix.get(material.name, 0.7)
            quality += coefficient * amount
            total_amount += amount

        if total_amount == 0:
            return 0

        quality /= total_amount
        quality = (quality - 0.28) / (1 - 0.28)
        quality = max(0, min(1, quality))
        quality = round(2 + 16 * (quality ** 1.5))
        return quality

    def linear_stat_calculator(self, stat_name):
        total_stat = 0
        for material, amount in self.materials.items():
            if amount <= 0:
                continue

            total_stat += getattr(material, stat_name) * amount

        return total_stat

    def non_linear_stat_calculator(self, stat_name):
        ...


if __name__ == "__main__":
    metal = Material("metal", 1.0, 2.0, 0.1)
    plastic = Material("plastic", 0.8, 0.8, 0.9)
    mats = {metal: 4, plastic: 6}
    test = Crafter(mats, Engine)
    print(test.pre_calculation())