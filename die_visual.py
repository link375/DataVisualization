import pygal
from die import Die

# Create a D6
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# Make some rolls, and store results in a list
results = []

for roll_num in range(1000):
    result = die_1.roll() * die_2.roll() * die_3.roll()
    results.append(result)

# analyze the results
frequencies = []
max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides

for value in range(3, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(results)
#print(frequencies)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
# hist.x_labels = ['1', '2', '3', '4', '5', '6']
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_labels = []
for value in range(max_results-2):
    hist.x_labels.append(value+3)

#hist.x_labels = list(len(range(1, max_results)))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')