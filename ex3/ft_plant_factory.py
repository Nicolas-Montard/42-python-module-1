#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: nmontard <nmontard@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 12:32:29 by nmontard        #+#    #+#               #
#  Updated: 2026/01/29 17:12:58 by nmontard        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    """Plant class that serves as a blueprint for any plant"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """initialize Plant"""
        self.name: str = name.capitalize()
        self.height: int = height
        self.age_in_days: int = age
        self.growth_since_last: int = 0

    def grow(self, growth: int) -> None:
        """grow the plant"""
        self.height += growth
        self.growth_since_last = growth

    def age(self, aging: int) -> None:
        """age the plant"""
        self.age_in_days += aging
        self.grow(aging)

    def get_info(self) -> None:
        """get info of plant"""
        print(f"{self.name} ({self.height}cm, {self.age_in_days} days)")


def plant_factory(plants_info: list[list]) -> list[Plant]:
    """create plants"""
    plants: list[Plant] = []
    for plant_info in plants_info:
        plants.append(Plant(plant_info[0], plant_info[1], plant_info[2]))
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.get_info()
    print(f"\nTotal plants created: {len(plants)}")
    return (plants)


if __name__ == "__main__":
    plants = plant_factory([["rose", 25, 30], ["oak", 200, 365],
                            ["cactus", 5, 90], ["sunflower", 80, 45],
                            ["fern", 15, 120]])
