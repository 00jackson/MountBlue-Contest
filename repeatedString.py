# there is a string s, of lowercase english that is repeated infinitely many times. Given an integer n, find and print the number of letter a's in the first n letters of the infinite string.

def repeatedString(s, n):
    total = 0
    for i in s:
        if i == 'a':
            total += 1
    total = n // len(s) * total

    for i in s[:n % len(s)]:
        if i == 'a':
            total += 1

    return total


s = list(input())
n = int(input())
result = repeatedString(s, n)
print(result)
