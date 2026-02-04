#!/usr/bin/env python3

class Plant:
    """Plant class that serves as a blueprint for any plant"""

    def __init__(self, name: str, height: int) -> None:
        """initialize Plant"""
        self.name: str = name.capitalize()
        self.__height: int = self.set_height(height)

    def get_info(self) -> None:
        """get info of plant"""
        print(f"- {self.name}: {self.get_height()}")

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

    def which_class(self) -> str:
        """return the class name"""
        return ("Plant")


class FloweringPlant(Plant):
    """FloweringPlant class that serves as a blueprint
     for any FloweringPlant"""

    def __init__(self, name: str, height: int,
                 is_blooming: bool, flower_color: str) -> None:
        """initialize FloweringPlant"""
        super().__init__(name, height)
        self.is_blooming: bool = is_blooming
        self.flower_color: str = flower_color

    def get_info(self) -> None:
        """get info of flowering plant"""
        if self.is_blooming:
            print(f"- {self.name}: {self.get_height()}cm, ", end="")
            print(f"{self.flower_color} flowers (blooming)")
        else:
            print(f"- {self.name}: {self.get_height()}cm, ", end="")
            print(f"{self.flower_color} flowers")

    def which_class(self) -> str:
        """return the class name"""
        return ("FloweringPlant")


class PrizeFlower(FloweringPlant):
    """PrizeFlower class that serves as a blueprint for any PrizeFlower"""

    def __init__(self, name, height, is_blooming,
                 flower_color, prize_point: int) -> None:
        """initialize PrizeFlower"""
        super().__init__(name, height, is_blooming, flower_color)
        self.prize_point: int = prize_point

    def get_info(self) -> None:
        """get info of prize plant"""
        if self.is_blooming:
            print(f"- {self.name}: {self.get_height()}cm, ", end="")
            print(f"{self.flower_color} flowers (blooming), ", end="")
            print(f"Prize points: {self.prize_point}")
        else:
            print(f"- {self.name}: {self.get_height()}cm, ", end="")
            print(f"{self.flower_color} flowers, ", end="")
            print(f"Prize points: {self.prize_point}")

    def which_class(self) -> str:
        """return the class name"""
        return ("PrizeFlower")


class Garden:
    """Garden class that contains plant"""

    def __init__(self, owner: str) -> None:
        """initialize Garden"""
        self.owner: str = owner.capitalize()
        self.plants: list[Plant] = []
        self.nb_plant: int = 0
        self.nb_flowering_plant: int = 0
        self.nb_prize_flower: int = 0
        self.total_growth: int = 0

    def add_plant(self, plant: Plant) -> None:
        """add plant to the garden"""
        self.plants.append(plant)
        if (plant.which_class() == "Plant"):
            self.nb_plant += 1
        elif (plant.which_class() == "FloweringPlant"):
            self.nb_flowering_plant += 1
        else:
            self.nb_prize_flower += 1
        print(f"Added {plant.name} to {self.owner} garden")

    def grow_plants(self) -> None:
        """grow all the plant in the garden"""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1
            print(f"{plant.name} grew 1cm")

    @staticmethod
    def create_plant(plant_name: str) -> Plant:
        """factory which create plant"""
        name: str = plant_name.capitalize()
        if name == "Rose":
            return (FloweringPlant("Rose", 25, True, "red"))
        elif name == "Oak":
            return (Plant("Oak Tree", 100))
        elif name == "Sunflower":
            return (PrizeFlower("Sunflower", 50, True, "yellow", 10))
        else:
            return (None)


class GardenManager:
    """GardenManager class which contain gardens ans a helper Gardenstats"""

    def __init__(self) -> None:
        """initialize GardenManager"""
        self.gardens: list[Garden] = []
        self.nb_of_garden: int = 0

    def add_garden(self, garden: Garden) -> None:
        """add a garden to the gardenManager"""
        self.gardens.append(garden)
        self.nb_of_garden += 1

    @classmethod
    def create_garden_network(cls, gardens: dict[str, list[str]]):
        """Class method which create gardens and fill them with plants"""
        garden_manager: GardenManager = cls()
        for owner in gardens.keys():
            plants = gardens[owner]
            garden_manager.add_garden(Garden(owner))
            for plant in plants:
                garden_manager.gardens[-1].add_plant(
                    Garden.create_plant(plant))
        return (garden_manager)

    class GardenStats:
        """class containing helper function for stats"""
        @staticmethod
        def print_nb_of_garden(nb_garden: int) -> None:
            """print the number of gardens"""
            print(f"Total garden managed: {nb_garden}")

        @staticmethod
        def calculate_garden_score(gardens: list[Garden]) -> None:
            """calculate the score of all gardens and print the result"""
            score_list: list[str] = []
            for garden in gardens:
                score = 0
                for plant in garden.plants:
                    score += plant.get_height()
                    if (plant.which_class() == "PrizeFlower"):
                        score += plant.prize_point
                score_list.append(f"{garden.owner}: {score}")
            print("Garden scores - ", end="")
            print(*score_list, sep=", ")

        @staticmethod
        def show_plants_stat(garden: Garden) -> None:
            """show the stats of plants in the garden"""
            print("plants in garden:")
            for plant in garden.plants:
                plant.get_info()
            print("")
            total_nb_plant = garden.nb_plant + \
                garden.nb_prize_flower + garden.nb_flowering_plant
            print(f"Plants added: {total_nb_plant}, ", end="")
            print(f"Total growth: {garden.total_growth}cm")
            print(f"Plant types: {garden.nb_plant} regular, ", end="")
            print(f"{garden.nb_flowering_plant} flowering, ", end="")
            print(f"{garden.nb_prize_flower} prize flowers")

        @staticmethod
        def validate_height(gardens: list[Garden]) -> None:
            """verify if the height of plants in the garden is valid"""
            for garden in gardens:
                for plant in garden.plants:
                    if plant.get_height() < 0:
                        print("Height validation test: False")
                        return (None)
            print("Height validation test: True")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print("")
    garden_manager: GardenManager = GardenManager.create_garden_network(
        {"Alice": ["Oak", "rose", "sunflower"],
         "Bob": ["oak"]})
    print("")
    garden_manager.gardens[0].grow_plants()
    print("")
    print("=== Alice's Garden Report ===")
    GardenManager.GardenStats.show_plants_stat(
        garden_manager.gardens[0])
    print("")
    GardenManager.GardenStats.validate_height(garden_manager.gardens)
    GardenManager.GardenStats.calculate_garden_score(garden_manager.gardens)
    GardenManager.GardenStats.print_nb_of_garden(garden_manager.nb_of_garden)
