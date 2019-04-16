Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("hello")"
SyntaxError: EOL while scanning string literal
>>> print ("hello")
hello
>>> prnt(3+7-3)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    prnt(3+7-3)
NameError: name 'prnt' is not defined
>>> print(3 + 7 - 3)
7
>>> print("hello", "there")
hello there
>>> answer_return=square_return(4)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    answer_return=square_return(4)
NameError: name 'square_return' is not defined
>>> ================================ RESTART ================================
>>> 
>>> answer_return=square_return(4)
>>> answer_return
16
>>> answer_print=square_print(4)
The square of num is 16
>>> answer_print
>>> answer_return*5
80
>>> answer_print*5
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    answer_print*5
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
>>> ================================ RESTART ================================
>>> 
>>> result=add(1,3)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    result=add(1,3)
  File "C:/Self-eduction/Python_Coursera/week2_2_input_output_function.py", line 6, in add
    print(number1+number2)
NameError: name 'number2' is not defined
>>> ================================ RESTART ================================
>>> 
>>> result = add(1, 3)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    result = add(1, 3)
  File "C:/Self-eduction/Python_Coursera/week2_2_input_output_function.py", line 6, in add
    print(number1+number2)
NameError: name 'number2' is not defined
>>> ================================ RESTART ================================
>>> 
>>> result=add(1,3)
4
>>> new result=result+1
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
>>> result = add(1,3)
>>> new result=result+1
SyntaxError: invalid syntax
>>> new_result=result+1
>>> new_result
5
>>> ================================ RESTART ================================
>>> 
Hello
>>> result=add(1,3)
>>> ================================ RESTART ================================
>>> 
Hello
>>> result=add(1,3)
4
>>> ================================ RESTART ================================
>>> 
Hello
>>> ================================ RESTART ================================
>>> 
>>> result=add(1,3)
4
>>> ================================ RESTART ================================
>>> 
>>> 
