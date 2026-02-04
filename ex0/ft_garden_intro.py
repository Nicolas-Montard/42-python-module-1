#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_intro.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: nmontard <nmontard@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/26 14:29:09 by nmontard        #+#    #+#               #
#  Updated: 2026/02/04 15:08:49 by nmontard        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def main(plant: str, height: str, age: str) -> None:
    """displays information about a plant in the garden."""
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant}")
    print(f"Height: {height}")
    print(f"age: {age}\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    main("Rose", "25cm", "30 Days")
