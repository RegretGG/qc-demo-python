import math
import sys


def area(radius):
    return math.pi * radius * radius


def perimeter(radius):
    return 2 * math.pi * radius


def print_circle_info(radius):
    area_result = area(radius)
    perimeter_result = perimeter(radius)
    print(f"Area: {area_result:.2f}")
    print(f"Perimeter: {perimeter_result:.2f}")


print_circle_info(5)