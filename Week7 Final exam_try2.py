# Task 2
a = 7
b = a + 3
a = 9
"""
After the code above has been executed, what value does b refer to?
10
"""

# Task 3
"""
What value is returned by a call on function f with argument 10?
40
"""
def f(y):
    x = y * 3
    return y + x
# Task 4
"""
start = 'L'
middle = 8
end = 'R'

Write an expression that evaluates to the string ’L8R’ using only the variables start, middle, end, one call on function
str, and string concatenation.

Do not use unnecessary parentheses: you need them for the function call, but nothing else.
Answer: start+str(middle)+end
"""

# Task 5
def count_max_letters(s1, s2, letter):
    '''(str, str, str) -> int 

    s1 and s2 are strings, and letter is a string of length 1.     Count how manytimes letter appears in s1 and in s2, and ret    urn the bigger of the twocounts.

    >>> count_max_letters('hello', 'world', 'l')
    2
    >>> count_max_letters('cat', 'abracadabra', 'a')
    5
    '''

    return max(s1.count(letter), s2.count(letter))

# Task 6
def same_length(L1, L2):
    '''(list, list) -> bool

    Return True if and only if L1 and L2 contain the same number of elements.
    '''

    return len(L1) == len(L2)

#Task 8
def reverse(s):
     '''(str) -> str

     Return the reverse of s.

     >>> reverse('abc')
    'cba'
    >>> reverse('a')
    'a'
    >>> reverse('madam')
    'madam'
    >>> reverse('1234!')
    '!4321'
    '''

     result = ''
     i = len(s) - 1
     while i >= 0:
        result = result + s[i]
        i=i-1
     return result

# Task 9
def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    [1, 'a']
    '''
  
    result = []
    for k in L:
       if k in d:
          result.append(k)

    return result

# Task 10
def count_values_that_are_keys(d):
    '''(dict) -> int

    Return the number of values in d that are also keys in d.
   
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 3})
    3
    >>> count_values_that_are_keys({1: 1})
    1
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 0})
    2
    >>> count_values_that_are_keys({1: 2})
    0
    '''

    result = 0
    for k in d:
        if d[k] in d:
             result = result + 1

    return result

# Task 11
def double_values(collection):
    for v in range(len(collection)):
         collection[v] = collection[v] * 2

"""
1) correct
L = [1, 2, 3]
double_values(L)

2) correct
d = {0: 10, 1: 20, 2: 30}
double_values(d)

3) incorrect
s = '123'
double_values(s)

4) incorrect
s = '123'
double_values(s)

5) incorrect
d = {1: 10, 2: 20, 3: 30}
double_values(d)
"""

#Task 12
"""
The diagonal of a square nested list goes from the top-left to the bottom-right corner. For example, consider this square nested list:

[[1, 3, 5], [2, 4, 5], [4, 0, 8]]\color{black}{\verb|[[1, 3, 5], [2, 4, 5], [4, 0, 8]]|}[[1,3,5],[2,4,5],[4,0,8]]

That nested list represents this table, where the values on the diagonal are in bold:

1 3 5

2 4 5

4 0 8

Consider this function:
"""
#1 correct
def get_diagonal_and_non_diagonal(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):

            if row == col:
                diagonal.append(L[row][col])
            elif row != col:
                non_diagonal.append(L[row][col])

    return (diagonal, non_diagonal)

#2 correct
def get_diagonal_and_non_diagonal1(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal1([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):

            if row == col:
                diagonal.append(L[row][row])
            else:
                non_diagonal.append(L[row][col])

    return (diagonal, non_diagonal)

#3 correct
def get_diagonal_and_non_diagonal2(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal1([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):

            if row == col:
                diagonal.append(L[row][col])
            else:
                non_diagonal.append(L[row][col])

    return (diagonal, non_diagonal)

#4 incorrect
def get_diagonal_and_non_diagonal3(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal3([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):

            if row == col:
                diagonal.append(L[row][col])

            non_diagonal.append(L[row][col])

    return (diagonal, non_diagonal)

#5 correct
def get_diagonal_and_non_diagonal4(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal4([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):

            if row == col:
                diagonal.append(L[row][col])
            if row != col:
                non_diagonal.append(L[row][col])

    return (diagonal, non_diagonal)

#task 13
"""
Write the missing assignment statement.
Do not call any functions or methods. Do not use unnecessary parentheses.
"""

def add_to_letter_counts(d, s):
    '''(dict of {str: int}, str) -> NoneType

    d is a dictionary where the keys are single-letter strings and the values
    are counts.

    For each letter in s, add to that letter's count in d.

    Precondition: all the letters in s are keys in d.

    >>> letter_counts = {'i': 0, 'r': 5, 'e': 1}
    >>> add_to_letter_counts(letter_counts, 'eerie')
    >>> letter_counts
    {'i': 1, 'r': 6, 'e': 4}
    '''

    for c in s:
        d[c] += 1
