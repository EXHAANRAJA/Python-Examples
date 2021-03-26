from matplotlib import colors
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size
import numpy as np

plt.style.use("bmh")

year = [2010, 2012, 2014, 2016, 2018, 2020, 2021]

pakpop = [179.4, 187.3, 195.3, 203.6, 204.73, 208.57, 212.48]
indpop = [197.4, 204.3, 209.3, 209.6, 208.73, 215.57, 218.48]
banpop = [198.4, 201.3, 204.3, 207.6, 208.73, 211.57, 215.48]

xindexes = np.arange(len(year))
width = 0.25


# Build a BarChart Chart
plt.bar(xindexes - width, pakpop, color='green',
        alpha=1, label="pakistan poluation", width=width)
plt.bar(xindexes, indpop, color='blue', alpha=1,
        label="India poluation", width=width)
plt.bar(xindexes+width, banpop, color='black', alpha=1,
        label="Bangladesh poluation", width=width)

plt.xticks(ticks=xindexes, labels=year)

plt.grid()
plt.legend()

# Setting Label in x & y cordinate
plt.xlabel("Year Wise Data")
plt.ylabel("Population in Million")
plt.title("Population Projection Between Top Asian Countries")

plt.savefig("Scatter.png")

plt.show()
# print(plt.style.available)
