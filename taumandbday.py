# taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum: one is black and the other is white. To make her happy, Taum has to buy b black gifts and w white gifts.
# the cost of each black gift is bc units.
# the cost of each white gift is wc units.
# the cost to convert a black gift into white gift or vice versa is z units.
# Determine the minimum cost of diksha's gifts.


def taumBday(b, w, bc, wc, z):
    return min(b*bc, b*(wc+z)) + min(w*(bc+z), w*wc)


b = int(input())
w = int(input())
bc = int(input())
wc = int(input())
wz = int(input())
z = int(input())
result = taumBday(b, w, bc, wc, z)
print(result)
