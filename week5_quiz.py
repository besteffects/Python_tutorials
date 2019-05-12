def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
          result = result + s[i]
          i = i + 1

    return result

def example(L):
    """ (list) -> list
    """
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result

def compress_list(L):
    """ (list of str) -> list of str

    Return a new list with adjacent pairs of string elements
    from L concatenated together, starting with indices 0 and 1,
    2 and 3,and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    """ 
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        
        # MISSING CODE next
        i=i+2
    return compressed_list


"""
What is the sum of the odd numbers from 1523 through 10503,
inclusive? Hint: write a while loop to accumulate the sum and
print it. Then copy and paste that sum.
For maximum learning, do it with a for loop as well, using range.
>>> oddnumber_sum(10503)
"""
def oddnumber_sum(final_number):
    added_number=1523
    total=0
    while added_number <=final_number:
        total=total+added_number
        added_number=added_number+2
    print(total)

def oddnumber_sum_range(final_number):
    total=0
    for i in range(1523, final_number, 2):
        total=total+i
    print(total)
    # final_number is 10504 for this case


"""
The while loop stops as soon as an even number is found, and the sum
of all the previous numbers is returned.
The four functions below use a for loop to try to accomplish
the same task, although they keep iterating through all of the numbers
in L regardless of whether the numbers are even or odd.
Only one of them returns the same value as function while_version. Which one is it?
>>>List1=[1,3,5,2,6,8,12,1,3]
>>>while_version(List1)
>>>9
"""
    
def while_version(L):
    """ (list of number) -> number
    """
    i = 0
    total = 0
    while i < len(L) and L[i] % 2 != 0:
         total = total + L[i]
         i = i + 1
    return total


def for_version_incorrect1(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        found_even = True

    return total
# result 13

def for_version_incorrect2(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
            found_even = True

    return total

def for_version_incorrect3(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        elif not found_even:
            found_even = True

    return total

def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True
 
    return total

def cap_song_repetition(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.
    >>> songs = ['Lola','Venus','Lola','Lola','LetItBe','Lola','ABC','Cecilia','Lola','Lola']
    >>> cap_song_repetition(songs, Lola)
    '''
    while playlist.count(song) >= 3:
        playlist.remove(song)
        # to finish

def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1

values = [1, 2, 3]
print(increment_items(values, 2))
print(values)
#result None [3,4,5]

#values = []
#for num in range(3, 9, 3):
 #   values.append(num)
#print(values)

#values = []
#for num in range(1, 3):
#    values.append(num * 3)
#print(values)

values = []
for num in range(1, 4):
    values.append(num * 3)
print(values)

values = []
for num in range(3, 10, 3):
    values.append(num)
print(values)
