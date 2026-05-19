# Z-Test for Single Mean

sample_mean = float(input("Enter sample mean: "))
pop_mean = float(input("Enter population mean: "))
std = float(input("Enter population standard deviation: "))
n = int(input("Enter sample size: "))

# Z Formula
z = (sample_mean - pop_mean) / (std / (n ** 0.5))

print("\nZ Statistic =", z)

# Decision Rule
if z > 1.96 or z < -1.96:
    print("Reject Null Hypothesis")
else:
    print("Accept Null Hypothesis")