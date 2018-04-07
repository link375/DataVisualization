import matplotlib.pyplot as plt

# x value
input_values = [1, 2, 3, 4, 5]
# y value
squares = [1, 4, 9, 16, 25]

# X / Y coordinates
plt.plot(input_values, squares, linewidth=5)

# Set chart title and labesl axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()
