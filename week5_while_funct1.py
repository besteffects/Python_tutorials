def last_vowel(s):
    """(str) -> str
    s->input string
    i -> index of string
    Return the last vowel in s if one exists; otherwise, return None.
    >>> last_vowel("cauliflower")
    "e"
    >>> last_vowel("pfft")
    None
    Notice that the loop condition evaluates to True when i is at least 0, and that in each
    iteration subtracts 1 from i.So i can't start at 0,
    because if it did then the loop body would execute exactly once.
    So i must start at either len(s) or len(s) - 1. The first time through the loop, s[i] is examined;
    if i is len(s), then it is an invalid index and this would cause an error.
    If i is len(s) - 1, then s[i] is valid: it evaluates to the last character in s.
    """
    i =len(s)-1
    while i >= 0:
         if s[i] in 'aeiouAEIOU':
             return s[i]
         i = i - 1
    return None
