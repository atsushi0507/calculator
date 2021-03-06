import math
import matplotlib.pyplot as plt
import numpy as np
import argparse

p = argparse.ArgumentParser()
p.add_argument("-y", "--yes", help="If this flag is used, the error is devided by N", action="store_true")
args = p.parse_args()
useN = args.yes

### Sample data
# Data range: 0 =< x, y =< 100
"""
x_data = [50, 60, 70, 80, 90]
y_data = [40, 70, 90, 60, 100]
"""
x = input("Input x values separated by comma: ")
y = input("Input y values separated by comma: ")

x_data = x.split(",")
y_data = y.split(",")

x_data = [float(x) for x in x_data]
y_data = [float(y) for y in y_data]

# Calculate mean x and y
n = len(x_data)
sum_x = 0
sum_y = 0
for i in range(len(x_data)):
    sum_x += x_data[i]
    sum_y += y_data[i]

mean_x = sum_x / n
mean_y = sum_y / n

# Calculate deviation of x and y for each point
dev_x = []
dev_y = []
sx2 = 0
sy2 = 0
for i in range(len(x_data)):
    dev_x.append(x_data[i] - mean_x)
    dev_y.append(y_data[i] - mean_y)
    sx2 += dev_x[i]*dev_x[i]
    sy2 += dev_y[i]*dev_y[i]

# Calculate variance of x
sx2 = sx2 / n
sy2 = sy2 / n

# Error
if (useN):
    error_y = math.sqrt(sy2 / (n))
else:
    error_y = math.sqrt(sy2 / (n-1))


# Calculate covariance
cov = 0
for i in range(len(x_data)):
    cov += (dev_x[i] * dev_y[i]) / n

# Calculate slope
a = cov / sx2

# Calculate intercept
b = mean_y - a * mean_x

# Print result
print(a, b)

### Plot
# Decorate plot
plt.xlim(0, 110)
plt.ylim(0, 110)
plt.xlabel("x")
plt.ylabel("y")
# Fit result
x = np.arange(0, 100, 0.1)
y = a * x + b
plt.plot(x, y, linestyle="dashed")
# Actual data point
plt.scatter(x_data, y_data, c="orange")
plt.errorbar(x_data, y_data, yerr = error_y, capsize=5, fmt='o', markersize=5, ecolor='black', markeredgecolor = "black", color='w')
# Add text to the plot
if (b > 0):
    label = "y={:.2f}x+{:.2f}".format(a,b)
else:
    label = "y={:.2f}x{:.2f}".format(a,b)
plt.text(80, 10, label)

# Save figure
plt.savefig("linearFit.png")
