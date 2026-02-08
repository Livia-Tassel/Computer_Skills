digits = [1, 8, 2, 8]

def count(s, value):
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

pairs = [[1, 2], [2, 2], [1, 3], [2, 3]]

def count_pairs(pairs):
    same_count = 0
    for x, y in pairs:
        if x == y:
            same_count += 1
    return same_count

def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total

def cheer(n):
    for _ in range(n):
        print("Go Cheers!")
    return

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'o', 'm', 'n']
sub_letters = [letters[i] for i in range(5,8)]

odds = [1, 3, 5, 7, 9]
even = [x+1 for x in odds]
mod = [x for x in odds if 25 % x == 0]

def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]
