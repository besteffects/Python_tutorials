def merge(L):
    merged = []
    for i in range(0, len(L), 3):
        merged.append(L[i] + L[i + 1] + L[i + 2])
    return merged

print(merge([1, 2, 3, 4, 5, 6, 7, 8, 9]))

#What is printed by the code above?
#Answer [6, 15, 24]



#2 
def mystery(s):
    """ (str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]: # <--- How many times is         this line reached? (answer 2)
            matches = matches + 1

    return matches == (len(s) // 2)

mystery('civil')

# 3 Which is the best docstring description for function mystery mystery?
def mystery(s):
    """ (str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]:
            matches = matches + 1

    return matches == (len(s) // 2)
# Answer: Return True if and only if s is equal to the reverse of s

# 4 In one of the Week 6 lecture videos, we wrote the function shift_left.
# Consider this function, which shifts in the other direction:
def shift_right(L):
    ''' (list) -> NoneType
    L=['a', 'b','c','d']
    Shift each item in L one position to the rightand shift the last
    item to the first position.

    Precondition: len(L) >= 1
    '''

    last_item = L[-1]

    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]
    L[0] = last_item

#5 Correct
def make_pairs(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with     the string from thecorresponding position of list1 and the     int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''

    pairs = []

    for i in range(len(list1)):
        inner_list = []
        inner_list.append(list1[i])
        inner_list.append(list2[i])
        pairs.append(inner_list)

    return pairs

#incorrect result [['C', 3]]
def make_pairs2(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with     the string from thecorresponding position of list1 and the     int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs2(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''

    pairs = []

    for i in range(len(list1)):
        inner_list = []
        inner_list.append(list1[i])
        inner_list.append(list2[i])
    pairs.append(inner_list)

    return pairs

#incorrect result [['A', 1, 'B', 2, 'C', 3], ['A', 1, 'B', 2, 'C', 3], ['A', 1, 'B', 2, 'C', 3]]
def make_pairs3(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with     the string from thecorresponding position of list1 and the     int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs3(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''

    pairs = []

    inner_list = []
    for i in range(len(list1)):
        inner_list.append(list1[i])
        inner_list.append(list2[i])
        pairs.append(inner_list)

    return pairs

#correct result 
def make_pairs4(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with     the string from thecorresponding position of list1 and the     int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs4(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''

    pairs = []

    for i in range(len(list1)):
        pairs.append([list1[i], list2[i]])

    return pairs
#6 values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Using values and indexing with non-negative indices, write an expression
#that evaluates to 5. Do not use addition, subtraction, or parentheses
# (brackets ([]] are required).
# answer values[1][1]

#7 treats = [['apple', 'pie'], ['vanilla', 'ice-cream'], ['chocolate', 'cake']]
# Using treats and indexing with only negative indices, write an expression
#that evaluates to 'pie'. Do not use addition, subtraction, or parentheses
# (brackets[ ] are required).
# answer treats[-3][-1] 

#8
for i in range(2, 5):
    for j in range(4, 9):
        print(i, j)

# Trace the code above in the Python Visualizer. How many times is print(i, j)
# executed?
# answer 15

#9 Select the code fragment(s) that make the function above match its docstring description.

def contains1(value, lst): #correct
    """ (object, list of list) -> bool
  
   Return whether value is an element of one of the nested        lists in lst.

   >>> contains1('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
   True
   """
    found = False
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == value:
                found = True   
    return found


def contains2(value, lst): 
    """ (object, list of list) -> bool
  
   Return whether value is an element of one of the nested        lists in lst.

   >>> contains2('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
   True
   """
    found = False
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == value:
                found = True   
    return found

#False - not correct
def contains3(value, lst): 
    """ (object, list of list) -> bool
  
   Return whether value is an element of one of the nested        lists in lst.

   >>> contains3('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
   True
   """
    found = False
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            found = (lst[i][j] == value) 
    return found

#False - not correct
def contains4(value, lst): 
    """ (object, list of list) -> bool
  
   Return whether value is an element of one of the nested        lists in lst.

   >>> contains4('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
   True
   """
    found = False
    for item in lst:
        if value == item:
            value = True
    return found
# 10 A file has a section at the top that has a preamble describing the contents of the
# file, then a blank line, then a list of high temperatures for each day in January all
# on one line, then a list of high temperatures for each day in February all on one line,
# then lists for March, April, and so on through December, each on one line.
# There are thousands of lines of information after that temperature data that you
# aren't currently interested in.
# You want to write a program that prints the average of the high temperatures in January.
# Which of the four file-reading approaches should you use?
# Answer - readline approach


#11 # data_file refers to a file open for reading.
for line in data_file:
     print(line)
#The program above prints the lines of the file but adds an extra blank line after each
#line. Select the code fragment(s) that when used as replacement(s) for print(line)
# will print the lines without extra blank lines.

# Note: use help to find out information about any functions or methods that you are
# not familiar with.

"""
1) correct
str2="line1\n\nline2\n\nline3"
>>> print(str2)
print(line,end='')

2) 
str2="line1\n\nline2\n\nline3"
print(line-'\n')
TypeError: unsupported operand type(s) for -: 'str' and 'str'

3) 
str2="line1\n\nline2\n\nline3"
print(str2.strip())

4) Correct
str2="line1\n\nline2\n\nline3"
str2="line1\nline2\nline3"
print(line.rstrip('\n'))
"""
