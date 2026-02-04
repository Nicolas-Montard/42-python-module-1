#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: nmontard <nmontard@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 12:49:32 by nmontard        #+#    #+#               #
#  Updated: 2026/02/04 15:11:51 by nmontard        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class SecurePlant:
    """Plant class that serves as a blueprint for any plant and secure data"""

    def __init__(self, name: str = "Plant", height: int = 0, age: int = 0):
        """initialize Plant"""
        self.name: str = name.capitalize()
        print(f"plant created: {self.name}")
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
            print(f"Height updated: {new_height}cm [OK]")
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
            print(f"Height updated: {new_age} days [OK]")
            return (new_age)

    def get_age(self) -> int:
        """get age of plant"""
        return (self.__age)


def plant_factory(plants_info: list[list]) -> list[SecurePlant]:
    """create plants"""
    plants: list[SecurePlant] = []
    for plant_info in plants_info:
        plants.append(SecurePlant(plant_info[0], plant_info[1], plant_info[2]))
    return (plants)


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plants = plant_factory([["rose", 25, 30]])
    plants[0].set_height(-5)
    print("\nCurrent plant: ", end="")
    plants[0].get_info()
