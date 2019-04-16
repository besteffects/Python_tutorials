def area(base, height):
    '''(number, number) -> number
    Return the area of a triangle with dimensions base
    and height.
    >>>area(10,5)
    25.0
    >>>area(2.5, 3)
    3.75
    '''

    return base * height / 2


def convert_to_celsius(fahrenheit):
    '''
(number) -> float
Return the number of Celsius degrees equivalent to fahrenheit degrees
>>> convert_to_celsius(32)
0.0
>>>convert_to_celsius(212)
100.0
'''
    return (fahrenheit - 32) * 5 / 9
