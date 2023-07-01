# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play.
# She tabulates the number of times she breaks her season record for most points and least points in a game.
# Points scored in the first game establish her record for the season, and she begins counting from there.

def breakingRecords(scores):
    # Write your code here
    max_score = scores[0]
    min_score = scores[0]
    max_count = min_count = 0
    for i in range(1, len(scores)):
        if scores[i] > max_score:
            max_score = scores[i]
            max_count += 1
        elif scores[i] < min_score:
            min_score = scores[i]
            min_count += 1
    return max_count, min_count


# Sample input
n = 9
scores = [10, 5, 8, 9, 7, 12, 4, 6]

# Call the function and store the results
max_count, min_count = breakingRecords(scores)

# Print the results
print("Max count:", max_count)
print("Min count:", min_count)
