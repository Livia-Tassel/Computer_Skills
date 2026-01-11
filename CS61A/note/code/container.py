nested_list = [[1, 2], [], 
               [[3, False, None],
                [4, lambda: 5]]]

# slicing
odds = [3, 5, 7, 9, 11]
[odds[i] for i in range(1, 3)] # [5, 7]
odds[1:3] # [5, 7]
odds[:3]  # [3, 5, 7]
odds[1:]  # [5, 7, 9, 11]
odds[:]   # [3, 5, 7, 9, 11]

# sum(interable[, start])
sum([2, 3, 4]) # 9
sum([2, 3], 4) # 9
sum([[2, 3], [4]])     # unsupported type for +: 'int' and 'list'
sum([[2, 3], [4]], []) # [] + [2, 3] + [4] = [2, 3, 4]

# max(interable[, key = func])
max(range(5)) # 4
max(range(10), key=lambda x: 7-(x-4)*(x-2)) # 3

# all(interable)
all([x < 5 for x in range(5)]) # True
all([x < 4 for x in range(5)]) # False

# string
"你好"
'hello'
"""
hello world!\n
this is livia!
"""

# dictionaries
num = {'I': 1, 'V': 5, 'X':10}
num['I'] # 1
list(num) # ['I', 'V', 'X']
list(num.values()) # [1, 5, 10]
{x * x: x for x in range(5) if x > 2} # {9: 3, 16: 4}

match = lambda k, v: v % k == 0
def index(keys, values, match):
    """
    >>> index([2, 3], [1, 2, 3, 4, 5, 6], match)
        {2: [2, 4, 6], 3: [3, 6]}
    """
    return {k: [v for v in values if match(k, v)] for k in keys}