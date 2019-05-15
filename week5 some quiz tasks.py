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
