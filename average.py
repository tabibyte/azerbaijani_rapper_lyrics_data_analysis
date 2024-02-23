# Your list of percentages
percentages = [
    1,10000000,10000,1000000000,100000000,100000000
]

# Step 1: Sort the list
percentages_sorted = sorted(percentages)

# Step 2: Calculate Q1, Q3, and IQR
Q1_index = int(0.25 * len(percentages_sorted))
Q3_index = int(0.75 * len(percentages_sorted))

Q1 = percentages_sorted[Q1_index]
Q3 = percentages_sorted[Q3_index]

IQR = Q3 - Q1

# Step 3: Identify outliers
lower_threshold = Q1 - 1.5 * IQR
upper_threshold = Q3 + 1.5 * IQR

outliers = [x for x in percentages_sorted if x < lower_threshold or x > upper_threshold]

print("Outliers:", outliers)
