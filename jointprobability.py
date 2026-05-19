# Joint Probability Mass Function

rows = int(input("Enter number of X values: "))
cols = int(input("Enter number of Y values: "))

pmf = []

print("Enter joint probabilities:")

for i in range(rows):
    row = []

    for j in range(cols):
        value = float(input(f"P(X{i}, Y{j}) = "))
        row.append(value)

    pmf.append(row)

print("\nJoint PMF Table:")

for row in pmf:
    print(row)

# Total Probability Check
sum_prob = 0

for i in range(rows):
    for j in range(cols):
        sum_prob += pmf[i][j]

print("\nTotal Probability =", sum_prob)