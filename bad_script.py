import math,sys
def area(radius):return math.pi*radius*radius
def perimeter(radius): return 2*math.pi*radius
def print_circle_info(radius):
  area_result=area(radius)
  perimeter_result = perimeter(radius)
  print("Area:",area_result)
  print("Perimeter:",perimeter_result)
print_circle_info(5)
