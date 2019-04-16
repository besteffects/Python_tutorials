def area(base, height):
    '''(number, number) -> number

    Return the area of a triangle with given base and
    height.

    >>> area(10, 40)
    200.0
    >>> area(3.4, 7.5)
    12.75
    '''

    return base * height / 2

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
# Task: write a function to calculate the semiperimeter of a triangle
# (That's half of the perimeter)


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
    return(side1 + side2 + side3)/2

