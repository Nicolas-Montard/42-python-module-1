#!/usr/bin/env python3

class Plant:
    """Plant class that serves as a blueprint for any plant and secure data"""

    def __init__(self, name: str = "Plant", height: int = 0, age: int = 0):
        """initialize Plant"""
        self.name: str = name.capitalize()
        self.__height: int = self.set_height(height)
        self.__age: int = self.set_age(age)

    def get_info(self):
        """get info of plant"""
        print(f"{self.name} ({self.get_height()}cm, {self.get_age()} days)")

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

    def set_age(self, new_age: int) -> int:
        """set age of plant"""
        if (new_age < 0):
            print(
                f"Invalid operation attempted: age {new_age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = new_age
            return (new_age)

    def get_age(self) -> int:
        """get age of plant"""
        return (self.__age)


class Flower(Plant):
    """Inherit Plant class and serves as a blueprint for any flower"""

    def __init__(self, name: str = "Plant", height: int = 0,
                 age: int = 0, color: str = "red") -> None:
        """initialize Flower"""
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """Make the flower bloom"""
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        """get info of Flower"""
        print(f"{self.name} (Flower): {self.get_height()}cm, \
              {self.get_age()} days, {self.color} color")


class Tree(Plant):
    """Inherit Plant class and serves as a blueprint for any tree"""

    def __init__(self, name: str = "Plant", height: int = 0,
                 age: int = 0, trunk_diameter: int = 0) -> None:
        """initialize tree"""
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.name} provides \
              {self.get_height() * self.trunk_diameter // 320} \
                square meters of shade")

    def get_info(self):
        """get info of tree"""
        print(f"{self.name} (Tree): {self.get_height()}cm, \
              {self.get_age()} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """Inherit Plant class and serves as a blueprint for any Vegetable"""

    def __init__(self, name: str = "Plant", height: int = 0, age: int = 0,
                 harvest_season: str = "summer",
                 nutritional_value: bool = True) -> None:
        """initialize Vegetable"""
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: bool = nutritional_value

    def get_info(self) -> None:
        """get info of vegeable"""
        print(
            f"{self.name} (Vegetable): {self.get_height()}cm, \
                {self.get_age()} days, {self.harvest_season} harvest")

    def show_nutritional_value(self) -> None:
        """give nutritional value"""
        if (self.nutritional_value is True):
            print(f"{self.name} is rich in vitamin C")
        else:
            print(f"{self.name} is not rich in vitamin C")


if __name__ == "__main__":
    flower1 = Flower("Rose", 25, 30, "red")
    flower2 = Flower("Tulipe", 30, 40, "white")
    tree1 = Tree("Oak", 500, 1825, 50)
    tree2 = Tree("Pine", 300, 1500, 30)
    vegetable1 = Vegetable("Tomato", 80, 90, "summer", 1)
    vegetable2 = Vegetable("carrot", 50, 60, "winter", 1)
    print("=== Garden Plant Types ===\n")
    flower1.get_info()
    flower1.bloom()
    print("")
    tree1.get_info()
    tree1.produce_shade()
    print("")
    vegetable1.get_info()
    vegetable1.show_nutritional_value()
