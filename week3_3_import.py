import math

def perimeter(side1, side2, side3):
    ''' (number, number, number) -> number

    Return the perimeter of the triangle with sides of
    length side1, side2 and side3.

    >>> perimeter(3, 4, 5)
    12
    >>> perimeter(10.5, 6, 9.3)
    25.8
    '''
    return side1 + side2 + side3

# 1. Examples
# 2. Type Contract
# 3. Header
# 4. Description
# 5. Body
# 6. Test

def semiperimeter(side1, side2, side3):
    '''
    (number, number, number) -> float

    Return the semiperimeter of a triangle with sides of
    length side1, side2 and side3.

    >>> semiperimeter (3, 4, 5)
    6.0
    >>> semiperimeter(10.5, 6, 9.3)
    12.9
    '''
    return perimeter(side1, side2, side3)/2


def area_hero(side1, side2, side3):
    '''(number, number, number) -> float

    Return the area of a triangle with sides of length
    side1, side2, and side3.

    >>> area_hero(3,4,5)
    6.0
    >>>area_hero(10.5, 6, 9.3)
    27.73168584850189
    '''

    semi = semiperimeter(side1, side2, side3)
    area = math.sqrt(semi* (semi - side1) * (semi - side2) * (semi -  side3))
    return area
