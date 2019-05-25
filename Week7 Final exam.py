#2
def f(x):
    y = x * 3
    return y - x
#3
What value is returned by a call on function f\color{black}{\verb|f|}f with argument 10\color{black}{\verb|10|}10?
def f(x):
    y = x * 3
    return y - x
Answer: 20

#4
"""
Consider this code:

first = 'pwn'
second = 3
third = 'd'
Write an expression that evaluates to the string 'pwn3d'\color{black}{\verb|'pwn3d'|}’pwn3d’ using only variables first\color{black}{\verb|first|}first, second\color{black}{\verb|second|}second, third\color{black}{\verb|third|}third, one call on function str\color{black}{\verb|str|}str, and string concatenation.

Do not use unnecessary parentheses: you need them for the function call, but nothing else.
"""
first+str(second)+third

#5
def larger_of_smallest(L1, L2):
    '''(list of int, list of int) -> int

    Return the larger of the smallest value in L1 and the small    est value inL2.

    Precondition: L1 and L2 are not empty.

    >>> larger_of_smallest([1, 4, 0], [3, 2])
    2
    >>> larger_of_smallest([4], [9, 6, 3])
    4
    '''

    return max(min(L1),min(L2))
#6
def same_length(L1, L2):
    '''(list, list) -> bool
    
    Return True if and only if L1 and L2 contain the same number of elements.
    same_length([1, 4, 0], [3, 2])
    '''

    if len(L1) == len(L2):
       return True
    else:
       return False
#7
def same_length1(L1, L2):
    '''(list, list) -> bool
    
    Return True if and only if L1 and L2 contain the same number of elements.
    same_length1([1, 4, 0], [3, 2])
    '''

    return len(L1)==len(L2)
#8
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
        i = i-1

     return result
#9
def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    ['a', 1]
    '''

    result = []
    for k in d:
        if k in L:
            result.append(k)

    return result
#10
def are_lengths_of_strs(L1, L2):
    '''(list of int, list of str) -> bool
  
    Return True if and only if all the ints in L1 are the lengths of the strings
    in L2 at the corresponding positions.

    Precondition: len(L1) == len(L2)

    >>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef'])
    True
    '''

    result = True
    for i in range(len(L1)):
       if L1[i] != len(L2[i]):
            #    L1[(i)] != len(L2[(i)])
            result = False
    return result
#11
def double_last_value(L1):
    '''(list of int) -> NoneType

    Double the value at L[-1]. For example, if L[-1] is 3,
    replace it with 6.
    double_last_value([1, 3, 5])
    Precondition: len(L) >= 1.
    '''
    L1 = [1, 3, 5]
    double_last_value(L1)
    print(L1[-1])
 # answer 10. [-1] is index of 5


def get_negative_nonnegative_lists(L):

#12 correct
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the
    inner lists of L and the second item is a list of the non-negative ints
    in those inner lists.

    Precondition: the number of rows in L is the same as the number of
    columns.

    >>> get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    '''

    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            # CODE MISSING HERE
            if L[row][col] < 0:
                neg.append(L[row][col])
            else:
                nonneg.append(L[row][col])
    return (neg, nonneg)

#incorrect. The answer is ([3, 5, 2, 5, 4, 0, 8], [-1, -4])
def get_negative_nonnegative_lists1(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the
    inner lists of L and the second item is a list of the non-negative ints
    in those inner lists.

    Precondition: the number of rows in L is the same as the number of
    columns.

    >>> get_negative_nonnegative_lists1([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    '''

    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            # CODE MISSING HERE
            if L[row][col] < 0:
                nonneg.append(L[row][col])
            else:
                neg.append(L[row][col])
    return (neg, nonneg)

# correct
def get_negative_nonnegative_lists2(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the
    inner lists of L and the second item is a list of the non-negative ints
    in those inner lists.

    Precondition: the number of rows in L is the same as the number of
    columns.

    >>> get_negative_nonnegative_lists2([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    '''

    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            # CODE MISSING HERE
            val = L[row][col]
            if val < 0:
                neg.append(val)
            else:
                nonneg.append(val)
    return (neg, nonneg)


# incorrect. Answer ([-1, -4, 0], [3, 5, 2, 5, 4, 8])
def get_negative_nonnegative_lists3(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the
    inner lists of L and the second item is a list of the non-negative ints
    in those inner lists.

    Precondition: the number of rows in L is the same as the number of
    columns.

    >>> get_negative_nonnegative_lists3([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    '''

    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            # CODE MISSING HERE
            if L[row][col] > 0:
                nonneg.append(L[row][col])
            else:
                neg.append(L[row][col])
    return (neg, nonneg)

#13
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
        d[c] += 1 #same as d[c]= d[c]+1

    
