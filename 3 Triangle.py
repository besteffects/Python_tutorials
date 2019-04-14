Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def f(x)
SyntaxError: invalid syntax
>>> def f(x): return x**2

>>> f(3)
9
>>> result = f(3)
>>> result
9
>>> def area(base, height):
	return base*height/2

>>> area(3,4)
6.0
>>> area (10,7.45)
37.25
>>> ================================ RESTART ================================
>>> area(4,4)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    area(4,4)
NameError: name 'area' is not defined
>>> ================================ RESTART ================================
>>> 
>>> area(10,2)
10.0
>>> perimeter(3,4,5)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    perimeter(3,4,5)
NameError: name 'perimeter' is not defined
>>> ================================ RESTART ================================
>>> 
>>> perimeter(3,4,5)
12
>>> help(round)
Help on built-in function round in module builtins:

round(...)
    round(number[, ndigits]) -> number
    
    Round a number to a given precision in decimal digits (default 0 digits).
    This returns an int when called with one argument, otherwise the
    same type as the number. ndigits may be negative.

>>> round(45,8)
45
>>> round()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    round()
TypeError: Required argument 'number' (pos 1) not found
>>> round(45.345,2)
45.34
>>> round(45)
45
>>> round(45.345,2,5)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    round(45.345,2,5)
TypeError: round() takes at most 2 arguments (3 given)
>>> round()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    round()
TypeError: Required argument 'number' (pos 1) not found
>>> help(id)
Help on built-in function id in module builtins:

id(...)
    id(object) -> integer
    
    Return the identity of an object.  This is guaranteed to be unique among
    simultaneously existing objects.  (Hint: it's the object's memory address.)

>>> x=8/4
>>> x
2.0
>>> x=12//3
>>> x
4
>>> x=3
>>> y=5
>>> x=y
>>> x
5
>>> x=3
>>> y=5
>>> x=y
>>> y
5
>>> 8=x
SyntaxError: can't assign to literal
>>> round(45.342)
45
>>> def bigger(x):
	return x**x
bigger(12)
SyntaxError: invalid syntax
>>> 
>>> bigger(12)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    bigger(12)
NameError: name 'bigger' is not defined
>>> ================================ RESTART ================================
>>> def bigger(x):
	return x**x

>>> bigger(12)
8916100448256
>>> HELP(ID)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    HELP(ID)
NameError: name 'HELP' is not defined
>>> help(id)
Help on built-in function id in module builtins:

id(...)
    id(object) -> integer
    
    Return the identity of an object.  This is guaranteed to be unique among
    simultaneously existing objects.  (Hint: it's the object's memory address.)

>>> 
