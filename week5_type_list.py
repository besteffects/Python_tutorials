Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> grades= [80, 90, 70]
>>> grades[0]
80
>>> grades[1]
90
>>> grades[2]
70
>>> grades[1:2]
[90]
>>> grades[0:2]
[80, 90]
>>> 80 in grades
True
>>> 60 in grades
False
>>> len(grades)
3
>>> min(grades)
70
>>> max(grades)
90
>>> sum(grades)
240
>>> subjects = ['bio', 'cs', 'math', 'history']
>>> len(subjects)
4
>>> min(subjects)
'bio'
>>> max(subjects)
'math'
>>> sum(subbects)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    sum(subbects)
NameError: name 'subbects' is not defined
>>> temperature=[18,20,22.5,24]
>>> temperature[-1]
24
>>> temperature[4]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    temperature[4]
IndexError: list index out of range
>>> temperature[3:]
[24]
>>> temperature[3:4]
[24]
>>> len([1,2,3,4])
4
>>> len(["math"])
1
>>> min([10,8,4])
4
>>> sum([4])
4
>>> street_address = [10, 'Main Street']
>>> for grade in grades:
	print(grade)

	
80
90
70
>>> for item in subjects:
	print(item)

	
bio
cs
math
history
>>> for item in street_address:
	print(item)

	
10
Main Street
>>> 
