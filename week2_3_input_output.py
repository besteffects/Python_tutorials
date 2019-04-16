Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> input("What is your name?")
What is your name? Jen
' Jen'
>>> input("What is your name?")
What is your name?
''
>>> name = input("What is your name?")
What is your name? Jen
>>> name
' Jen'
>>> name=input("What is your name? ")
What is your name? Jen
>>> name
'Jen'
>>> location=input("What is your location? ")
What is your location? Toronto
>>> name
'Jen'
>>> location
'Toronto'
>>> print(name, "lives in", location)
Jen lives in Toronto
>>> num_coffee=input("how many cups of coffee? ")
how many cups of coffee? 2
>>> num_coffee
'2'
>>> age=input("How old are you")
How old are you12
>>> age=input("How old are you? ")
How old are you? 12
>>> '''hello'''
'hello'
>>> print('''How
are
you?''')
How
are
you?
>>> s='''How
are
you?'''
>>> s
'How\nare\nyou?'
>>> print('3\t4\t5')
3	4	5
>>> print('\\')
\
>>> print('\')
      
SyntaxError: EOL while scanning string literal
>>> print('don\'t')
don't
>>> print("He says, \"hi\"")
He says, "hi"
>>> 
