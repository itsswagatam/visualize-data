import matplotlib.pyplot as plt
import numpy as np

# Sample Data
x = np.arange(1, 11)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.random.randint(1, 10, size=10)

# Create a figure with multiple subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Line Plot
axs[0].plot(x, y1, marker='o', linestyle='-', color='b', label='sin(x)')
axs[0].plot(x, y2, marker='s', linestyle='--', color='r', label='cos(x)')
axs[0].set_title("Line Plot")
axs[0].set_xlabel("X-axis")
axs[0].set_ylabel("Y-axis")
axs[0].legend()
axs[0].grid(True)

# Bar Chart
axs[1].bar(x, y3, color='g', alpha=0.7)
axs[1].set_title("Bar Chart")
axs[1].set_xlabel("Categories")
axs[1].set_ylabel("Values")

# Scatter Plot
axs[2].scatter(x, y3, color='m', marker='D', edgecolor='black')
axs[2].set_title("Scatter Plot")
axs[2].set_xlabel("X-axis")
axs[2].set_ylabel("Y-axis")
axs[2].grid(True)

# Show the plots
plt.tight_layout()
plt.show()
