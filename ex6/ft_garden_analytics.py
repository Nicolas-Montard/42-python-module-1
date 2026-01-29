#!/usr/bin/env python3

class Plant:
    """Plant class that serves as a blueprint for any plant and secure data"""

    def __init__(self, name: str, height: int):
        """initialize Plant"""
        self.name: str = name.capitalize()
        self.__height: int = self.set_height(height)

    def get_info(self):
        """get info of plant"""
        print(f"{self.name} ({self.get_height()}cm, {self.get_age()} days)")

    def grow(self) -> None:
        """grow the plant"""
        self.set_height(self.get_height() + 1)

    def set_height(self, new_height: int) -> int:
        """set height of plant"""
        if (new_height < 0):
            print(
                f"Invalid operation attempted: height {new_height}cm \
                    [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = new_height
            return (new_height)

    def get_height(self) -> int:
        """get height of plant"""
        return (self.__height)


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, is_blooming: bool, flower_color: str) -> None:
        super().__init__(name, height)
        self.is_blooming: bool = is_blooming
        self.flower_color = flower_color

    def get_info(self) -> None:
        """get info of flowering plant"""
        if self.is_blooming:
            print(
                f"{self.name} {self.get_height()}cm {self.flower_color} flowers (blooming)")
        else:
            print(f"{self.name} {self.get_height()}cm {self.flower_color} flowers")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, is_blooming, flower_color, prize_point: int) -> None:
        super().__init__(name, height, is_blooming, flower_color)
        self.prize_point: int = prize_point


class Garden:

    def __init__(self, owner: int) -> None:
        self.owner: int = owner
        self.plants: list[Plant] = []
        self.nb_plant_added = 0
        self.total_growth = 0

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        self.nb_plant_added += 1
        print(f"Added {plant.name} to {self.owner} garden")

    def grow_plants(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1
            print(f"{plant.name} grew 1cm")
