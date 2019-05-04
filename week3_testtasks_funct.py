import math

def function(eggs):
    if eggs %12 ==0:
        return False
    else:
        return True

def fruit_color(fruit):
    if fruit == 'apple':
        return 'red'
    elif fruit == 'banana':
        return 'yellow'
    elif fruit == 'pear':
        return 'green'        
print(fruit_color('apple'))

def fruit_color1(fruit):
    if fruit == 'apple':
        return 'red'
    elif fruit == 'banana':
        return 'yellow'
    elif fruit == 'pear':
        return 'green'
print(fruit_color1('peach'))

def weather_report(temp):
    if temp >= 20:
        return 'warm enough for ice cream'
    elif temp >= 0:
        return 'above freezing'

def passing_grade(grade1, grade2):
    total = 0
    grade_count = 0
if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
else:
    total = total + grade2
    grade_count = grade_count + 1

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)
