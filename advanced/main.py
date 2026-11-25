expected = [
    44, 61, 90, 14, 29, 31, 49, 14, 80, 17, 23, 15, 66, 59, 94, 93, 54, 43, 11, 30, 81, 52, 7, 9, 8, 29, 56, 25, 8, 41, 12, 75, 92, 74, 9, 35, 8, 65, 10, 94, 34, 90, 47, 10, 12, 39, 21, 8, 71, 64, 85, 99, 58, 19, 58, 64, 78, 11, 70, 26, 62, 89, 55, 24, 68, 10, 64, 6, 18, 66, 79, 74, 77, 45, 68, 52, 13, 93, 6, 12, 52, 23, 3, 79, 5, 35, 73, 2, 31, 66, 7, 85, 94, 49, 68, 6, 62, 29, 93, 86, 50, 5, 10, 57, 6, 16, 57, 93, 65, 41, 73, 46, 24, 3, 50, 4, 59, 22, 66, 18, 26, 74, 62, 2, 58, 92, 17, 32, 49, 1, 1, 53, 62, 24, 92, 10, 81, 20, 16, 74, 78, 25, 79, 82, 88, 34, 94, 55, 97, 30, 49, 76, 99, 89, 20, 73, 28, 93, 91, 78, 90, 61, 20, 86, 16, 92, 33, 33, 94, 17, 71, 88, 2, 72, 56, 11, 38, 88, 9, 79, 98, 66, 32, 58, 42, 76, 13, 55, 24, 9, 40, 88, 38, 33, 92, 96, 65, 58, 25, 29
]

received = [
    41, 67, 89, 6, 40, 40, 55, 4, 80, 26, 24, 21, 60, 59, 85, 98, 49, 53, 22, 28, 86, 47, 12, 21, 17, 39, 48, 33, 19, 50, 11, 86, 84, 62, 14, 41, 1, 71, 10, 83, 34, 82, 58, 8, 8, 46, 31, 4, 83, 58, 87, 100, 53, 21, 56, 53, 73, 22, 70, 14, 50, 101, 63, 20, 59, 3, 61, 5, 18, 58, 85, 68, 89, 55, 65, 50, 14, 104, 2, 1, 47, 27, 6, 88, 6, 43, 77, 13, 43, 66, 11, 93, 94, 53, 68, 6, 53, 36, 101, 81, 40, 12, 3, 63, 16, 14, 66, 103, 76, 50, 83, 35, 24, 9, 43, 11, 70, 21, 64, 13, 26, 72, 57, 10, 50, 84, 21, 27, 53, 7, 4, 58, 61, 19, 82, 3, 90, 10, 13, 67, 73, 27, 83, 80, 80, 32, 88, 61, 109, 30, 54, 70, 103, 92, 18, 80, 18, 96, 91, 76, 79, 67, 14, 76, 5, 83, 45, 35, 93, 18, 82, 78, 6, 61, 56, 15, 26, 88, 13, 81, 92, 59, 22, 54, 35, 76, 20, 56, 24, 15, 34, 77, 38, 34, 83, 86, 70, 48, 30, 29
]


drift = []
for expected_num, received_num in zip(expected, received):
    drift.append(received_num - expected_num)

while True:
    while True:
        try:
            user_excellent = input("What is the threshold for the drift to be excellent? ")
            user_excellent = int(user_excellent)
            break
        except ValueError:
            print("Please enter an integer. ")

    while True:
        try:
            user_acceptable = input("What is the threshold for the drift to be acceptable? ")
            user_acceptable = int(user_acceptable)
            break
        except ValueError:
            print("Please enter an integer. ")

    if user_acceptable >= user_excellent:
        break
    else:
        print("The acceptable threshold has to be larger than the excellent threshold.")


amount_acceptable = 0
amount_excellent = 0
amount_poor = 0
amount_negative = 0
amount_positive = 0

for i in range(len(expected)):
    print(f"Expected: {expected[i]}")
    print(f"Received: {received[i]}")
    if drift[i] > 0:
        print(f"Positive Drift of {abs(drift[i])}")
        amount_positive += 1
    elif drift[i] < 0:
        print(f"Negative Drift of {abs(drift[i])}")
        amount_negative += 1
    else:
        print("No Drift detected")
    if abs(drift[i]) <= user_excellent:
        print("This drift is at the excellent level")
        amount_excellent += 1
    elif abs(drift[i]) <= user_acceptable:
        print("This drift is at the acceptable level")
        amount_acceptable += 1
    else:
        print("This drift is at the poor level")
        amount_poor += 1

total_drift = 0
for i in range(len(drift)):
    total_drift = total_drift + abs(drift[i])

print(f"The total drift is {total_drift}")

avg_drift = total_drift / len(drift)

print(f"The average drift is {avg_drift}")

print(f"There were {amount_poor} signal drifts in the poor range, {amount_acceptable} in the acceptable range, and {amount_excellent} in the excellent range. ")
print(f"There were {amount_positive} positive drifts and {amount_negative} negative drifts.")