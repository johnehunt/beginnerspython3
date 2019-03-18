# Pie chart, where the slices will be ordered and plotted counter-clockwise:

import matplotlib.pyplot as pyplot

labels = 'Java', 'Scala', 'Python', 'C#'
sizes = [30, 15, 45, 10]

# only "explode" the 3rd slice (i.e. 'Python')
explode = (0, 0, 0.1, 0)

fig1, ax1 = pyplot.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

pyplot.show()
