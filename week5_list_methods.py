Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> colours =[]
>>> prompt = 'Enter another one of your favourite colours (type return to end):'
>>> colour = input(prompt)
Enter another one of your favourite colours (type return to end):blue
>>> colours
[]
>>> while colour != '';
SyntaxError: invalid syntax
>>> while colour !='':
	colours.append(colour)
	colour = input(prompt)

	
Enter another one of your favourite colours (type return to end):yellow
Enter another one of your favourite colours (type return to end):brown
Enter another one of your favourite colours (type return to end):
>>> colours
['blue', 'yellow', 'brown']
>>> colours.extend('hot pink', 'neon green')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    colours.extend('hot pink', 'neon green')
TypeError: extend() takes exactly one argument (2 given)
>>> colours.extend(['brown']
>>> colours.extend(['hot pink', 'neon green'])
	       
SyntaxError: invalid syntax
>>> colours.extend(['hot pink', 'neon green'])
>>> colours
['blue', 'yellow', 'brown', 'hot pink', 'neon green']
>>> colours.pop()
'neon green'
>>> colours
['blue', 'yellow', 'brown', 'hot pink']
>>> colours.pop(2)
'brown'
>>> colours
['blue', 'yellow', 'hot pink']
>>> colours.remove('black')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    colours.remove('black')
ValueError: list.remove(x): x not in list
>>> if colours (count("yellow")>0:
	    
SyntaxError: invalid syntax
>>> if colours.count("yellow")>0:
	colours.remove('yellow')

	
>>> colours
['blue', 'hot pink']
>>> if 'yellow' in colours:
	colours.remove('yellow')

	
>>> colours
['blue', 'hot pink']
>>> colours.extend('auburn', 'taupe', 'magenta')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    colours.extend('auburn', 'taupe', 'magenta')
TypeError: extend() takes exactly one argument (3 given)
>>> colours.extend(['auburn', 'taupe', 'magenta'])
>>> colours
['blue', 'hot pink', 'auburn', 'taupe', 'magenta']
>>> colours.sort()
>>> colours
['auburn', 'blue', 'hot pink', 'magenta', 'taupe']
>>> colours.reverse()
>>> colourse
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    colourse
NameError: name 'colourse' is not defined
>>> colours
['taupe', 'magenta', 'hot pink', 'blue', 'auburn']
>>> colours.insert(2, "brown")
>>> colours
['taupe', 'magenta', 'brown', 'hot pink', 'blue', 'auburn']
>>> colours.remove("brown")
>>> colours.insert(-2,'brown')
>>> colours
['taupe', 'magenta', 'hot pink', 'brown', 'blue', 'auburn']
>>> colours.index("neon green")
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    colours.index("neon green")
ValueError: 'neon green' is not in list
>>> if "hot pink" in colours:
	where = colours.index ('hot pink')
	colours.pop(where)

	
'hot pink'
>>> colours
['taupe', 'magenta', 'brown', 'blue', 'auburn']
>>> 
