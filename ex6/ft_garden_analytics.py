#!/usr/bin/env python3

class Plant:
    """Plant class that serves as a blueprint for any plant and secure data"""

    def __init__(self, name: str, height: int):
        """initialize Plant"""
        self.name: str = name.capitalize()
        self.__height: int = self.set_height(height)

    def get_info(self):
        """get info of plant"""
        print(f"- {self.name} ({self.get_height()}cm, {self.get_age()} days)")

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
                f"- {self.name} {self.get_height()}cm {self.flower_color} flowers (blooming)")
        else:
            print(f"- {self.name} {self.get_height()}cm {self.flower_color} flowers")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, is_blooming, flower_color, prize_point: int) -> None:
        super().__init__(name, height, is_blooming, flower_color)
        self.prize_point: int = prize_point
    
    def get_info(self):
        """get info of prize plant"""
        if self.is_blooming:
            print(
                f"- {self.name} {self.get_height()}cm {self.flower_color} flowers (blooming), Prize points: {self.prize_point}")
        else:
            print(f"- {self.name} {self.get_height()}cm {self.flower_color} flowers, Prize points: {self.prize_point}")


class Garden:
    nb_plant_gardens: int = 0
    total_growth_gardens: int = 0

    def __init__(self, owner: str) -> None:
        self.owner: str = owner.capitalize()
        self.plants: list[Plant] = []
        self.nb_plant: int = 0
        self.total_growth: int = 0

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        self.nb_plant_added += 1
        nb_plant_gardens += 1
        print(f"Added {plant.name} to {self.owner} garden")

    def grow_plants(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1
            total_growth_gardens += 1
            print(f"{plant.name} grew 1cm")

    @staticmethod
    def create_plant(plant_name: str) -> Plant:
        if plant_name == "rose":
            return (FloweringPlant("rose", 25, "red", 1))
        elif plant_name == "oak":
            return (Plant("oak", 100))
        elif plant_name == "sunflower":
            return (PrizeFlower("sunflower", 50, "yellow", 1, 10))
        else:
            return (None)


class GardenManager:
    nb_of_garden: int = 0
    gardens: list[Garden] = []

    def __init__(self) -> None:
        pass

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)
        nb_of_garden += 1

    @classmethod
    def create_garden_network(self, gardens: dict[str, list[str]]) -> None:
        for owner in gardens.keys():
            plants = gardens[owner]
            self.add_garden(Garden(owner))
            self.nb_of_garden += 1
            for plant in plants:
                self.gardens[-1].add_plant(Garden.create_plant(plant))
                print(f"Added {plant.capitalize} to {owner.capitalize} garden")

    class GardenStats:
        @staticmethod
        def print_nb_of_garden(nb_garden: int):
            print(f"Total garden managed: {nb_garden}")

        @staticmethod
        def show_plant_stat_from_garden(garden: Garden):
            print(f"plants in garden:")
            for plant in garden.plants:
                plant.get_info()
        
        @staticmethod
        def calculate_garden_score(gardens: list[Garden]):
            scores : dict[str, int]
            for garden in gardens:
                score = 0
                for plant in garden.plants:
                    score += plant.get_height()
                    #add to score if plant is PrizeFlower


