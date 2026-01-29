#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: nmontard <nmontard@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 10:23:33 by nmontard        #+#    #+#               #
#  Updated: 2026/01/29 11:21:57 by nmontard        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    """Plant class that serves as a blueprint for any plant"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """initialize Plant"""
        self.name: str = name.capitalize()
        self.height: int = height
        self.age: int = age


def main(plants: list[Plant]) -> None:
    """manages data for plants and displays their information
    in an organized way."""
    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    plant1 = Plant("rose", 25, 30)
    plant2 = Plant("sunflower", 80, 45)
    plant3 = Plant("cactus", 15, 120)
    tab = [plant1, plant2, plant3]
    main(tab)
