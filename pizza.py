#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Sept 2020
# This program calculates the price of pizza

import constants


def main():
    # this function calculates the price of the pizza

    # input
    diameter = int(
        input("Enter the diameter of the pizza you would " + "like (inch): ")
    )

    # process
    sub_total = constants.LABOUR + constants.RENT + (diameter * constants.COST_PER_INCH)

    total = sub_total + (sub_total * constants.HST)

    # output
    print("")
    print("The cost of a {0} inch pizza is ${1:,.2f}".format(diameter, total))
    print(" \nDone.")


if __name__ == "__main__":
    main()
