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

#5. What is the sum of the odd numbers from 1523 through 10503,
#inclusive Hint: write a while loop to accumulate the sum and print it.
#Then copy and paste that sum. For maximum learning, do it with a
# for loop as well, using range.
#decision with range()
def oddnumberssum(start, end):
    """
    oddnumberssum(1523, 10504)
    27004383
    """ 
    total=0
    for i in range (start, end, 2):
        total=total+i
    return total

def oddnumberssum_while(start, end):
    """
    oddnumberssum_while(1523, 10503)
    27004383
    """ 
    total = 0
    while start <= end:
        total = total+start
        start = start+2
    print (total)

# 6. The while loop stops as soon as an even number is found,
# and the sum of all the previous numbers is returned.
# The four functions below use a for loop to try to accomplish the same task,
# although they keep iterating through all of the numbers in L regardless of
# whether the numbers are even or odd. Only one of them returns the same value
# as function while_version. Which one is it?

def while_version(L):
    """ (list of number) -> number
    """
    i = 0
    total = 0
    while i < len(L) and L[i] % 2 != 0:
         total = total + L[i]
         i = i + 1
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
    >>> cap_song_repetition(['Lola','Venus','Lola','Lola','LetItBe','Lola','ABC','Cecilia','Lola','Lola'], 'Lola')
    >>>['Venus', 'LetItBe', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
    '''
    while playlist.count(song) > 3:
        playlist.pop(playlist.index(song))
    return playlist

#Only 2 occurences will be returned
def cap_song_repetition_remove(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.
    >>> cap_song_repetition_remove(['Lola','Venus','Lola','Lola','LetItBe','Lola','ABC','Cecilia','Lola','Lola'], 'Lola')
    >>>['Venus', 'LetItBe', 'ABC', 'Cecilia', 'Lola', 'Lola']
    '''
    while playlist.count(song) >= 3:
        playlist.remove(song)
    return playlist

#this will return exception ValueError: list.remove(x): x not in list
def cap_song_repetition_remove_incorrect1 (playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.
    >>> cap_song_repetition_remove(['Lola','Venus','Lola','Lola','LetItBe','Lola','ABC','Cecilia','Lola','Lola'], 'Lola')
    '''
    while playlist.count(song) > 3:
        playlist.remove(playlist.index(song))
    return playlist

# 3 occurences returned
def cap_song_repetition_remove_case2(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    >>> cap_song_repetition_remove_incorrect1(['Lola','Venus','Lola','Lola','LetItBe','Lola','ABC','Cecilia','Lola','Lola'], 'Lola')
    >>> ['Venus', 'LetItBe', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
    '''
    while playlist.count(song) > 3:
        playlist.remove(song)
    return playlist

    
   # What is printed by the program?
   # Answer: 
   # None (because there is no return statement)
   # [3,4,5]
def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1
values = [1, 2, 3]
print(increment_items(values, 2))
print(values)

values = []
for num in range(3, 10, 3):
    values.append(num)
print(values)
