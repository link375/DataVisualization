import matplotlib.pyplot as plt

#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

# colormap

# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)


plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)
# save an image of your plot
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()

# Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set the range for each axis
plt.axis([0, 1100, 0, 1100000])


# sEt size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

