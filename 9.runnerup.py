scores = [900, 987, 430, 569, 1000]

highest = second_highest = float("-inf")

for score in scores:
    if score > highest:
        second_highest = highest
        highest = score
    elif score > second_highest and score != highest:
        second_highest = score

print("Second-highest score:", second_highest)
