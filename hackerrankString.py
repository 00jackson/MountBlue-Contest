# We say that a string contains the word hackerrank if a subsequence of its characters spell the word hackerrank. Remeber that a subsequence maintains the order of characters selected from a sequence.
# more formally, let p[0], p[1], ..., p[9] be the respective indices of h, a, c, k, e, r, r, a, n, k in string s. If p[0] < p[1] < p[2] < ... < p[9] is true, then s contains hackerrank.
# for each query, print YES on a new line if the string contains hackerrank, otherwise, print NO.

def hackerrankInString(s):
    target = 'hackerrank'
    n = len(target)
    i = 0
    for char in s:
        if char == target[i]:
            i += 1
            if i == n:
                return 'YES'
    return 'NO'


s = list(input())
result = hackerrankInString(s)
print(result)
