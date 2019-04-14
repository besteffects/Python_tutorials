Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> 'hello'
'hello'
>>> sunny_greeting='What a beautiful day'
>>> storm_greeting='Wow you're dripping wet'
SyntaxError: invalid syntax
>>> "Wow, you're dripping wet."
"Wow, you're dripping wet."
>>> 'wow, you\'re dripping wet'
"wow, you're dripping wet"
>>> storm_greeting
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    storm_greeting
NameError: name 'storm_greeting' is not defined
>>> storm_greeting='Wow, you\'re dripping wet'
>>> storm_greeting
"Wow, you're dripping wet"
>>> 'persona1' + 'penguin'
'persona1penguin'
>>> 'I want to be your personal ' + 'penguin' +'!'
'I want to be your personal penguin!'
>>> puzzle_start=:'I want to be your personal '
SyntaxError: invalid syntax
>>> puzzle_start='I want to be your personal '
>>> punctuation = '!'
>>> noun='earthworm'
>>> puzzle_start + noun + punctuation
'I want to be your personal earthworm!'
>>> 'ha'*5
'hahahahaha'
>>> 'Bwa' +'ha'*5
'Bwahahahahaha'
>>> ('Bwa' +'ha')*5
'BwahaBwahaBwahaBwahaBwaha'
>>> 'My shoe size is' +8.5
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    'My shoe size is' +8.5
TypeError: Can't convert 'float' object to str implicitly
>>> 'ha'*5
'hahahahaha'
>>> 'ha'*'5'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    'ha'*'5'
TypeError: can't multiply sequence by non-int of type 'str'
>>> 'a'='b'
SyntaxError: can't assign to literal
>>> 'a'/'b'
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    'a'/'b'
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> 'a'**'b'
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    'a'**'b'
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
>>> 
