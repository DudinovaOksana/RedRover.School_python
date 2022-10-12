# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
import math
def square (square_side):
    perimeter_of_square = 4*square_side
    area_of_square = square_side ** 2
    diagonal_of_square = square_side * math.sqrt(2)
    return perimeter_of_square, area_of_square, diagonal_of_square
print(square(3))
