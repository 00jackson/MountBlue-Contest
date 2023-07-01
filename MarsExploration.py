# Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string sdetermine how many letters of the SOS message have been changed by radiation.


def marsExploration(s):
    error = 0
    first, second, third = 0, 1, 2
    while third < len(s):
        if s[first] != 'S':
            error += 1
        if s[second] != 'O':
            error += 1
        if s[third] != 'S':
            error += 1
        first += 3
        second += 3
        third += 3
    return error


s = ['SOSSPSSQSSOR', 'SOSSOT', 'SOSSOSSOS',
     'SOSSOSSOSSOS', 'SOSOOSOSOSOSOSSOSOSOSOSOSOS']

result = marsExploration(s)
print(result)
