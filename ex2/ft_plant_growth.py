#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: nmontard <nmontard@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 11:16:08 by nmontard        #+#    #+#               #
#  Updated: 2026/01/29 11:26:43 by nmontard        ###   ########.fr        #
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
        print(f"{self.name}: {self.height}cm, {self.age_in_days} days old")
        if self.growth_since_last != 0:
            print(f"Growth this week: +{self.growth_since_last}cm")


def main(plants: list[Plant]) -> None:
    """simulate plant growth over time"""
    print("=== Day 1 ===")
    for plant in plants:
        plant.get_info()
        print("")
        plant.age(6)
    print("=== Day 7 ===")
    for plant in plants:
        plant.get_info()
        print("")


if __name__ == "__main__":
    plant1 = Plant("rose", 25, 30)
    plant2 = Plant("sunflower", 80, 45)
    plant3 = Plant("cactus", 15, 120)
    tab = [plant1, plant2, plant3]
    main(tab)
