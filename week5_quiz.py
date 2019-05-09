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

    
