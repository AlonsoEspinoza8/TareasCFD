import sys
print("Hello World!")
print(sys.executable)


import matplotlib.pyplot as plt
import numpy as np

print("Hello World!")

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])

# Create a line plot
plt.plot(x, y)

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Plot")

# Show the plot
plt.show()