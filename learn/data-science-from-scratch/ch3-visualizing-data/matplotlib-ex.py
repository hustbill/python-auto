# name: matplotlib-ex.py
# by Hua Zhang,  Feb 25, 2017
# http://matplotlib.org/
# visualizing data tool, for simple bar charts, line charts, and scatterplots

# using matplotlib.pyplot module
from matplotlib import pyplot as plt

#years = [ x for x in range(1950, 2010)]

#print years

years = [1950,	1960,	1970,	1980,	1990,	2000,	2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# add a title
plt.title("Nominal GDP")

# add a label to the y-axis
plt.ylabel("Billions of $")
plt.show()
