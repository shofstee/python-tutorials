from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

num_sides = 6
num_dice = 2
num_rolls = 1000

dice = [Die(num_sides) for i in range(1, num_dice + 1)]

# Populate all rolls using a for loop
# frequencies = {}
# for i in range(num_dice, num_dice * num_sides + 1):
#    frequencies.update({i: 0})

# Populate all rolls using listcomprehension
frequencies = dict([(i, 0) for i in range(num_dice, num_dice * num_sides + 1)])

for roll in range(0, num_rolls):
    val = 0
    for die in dice:
        val += die.roll()

    frequency = frequencies.get(val) + 1;
    frequencies = frequencies | {val: frequency}

print(frequencies)

x_values = frequencies.keys()
data = [Bar(x=list(frequencies.keys()), y=list(frequencies.values()))]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Results of rolling {num_dice} D{num_sides} {num_rolls} times.', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='/tmp/dice.html')

