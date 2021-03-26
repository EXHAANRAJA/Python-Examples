from matplotlib import colors
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size


year = [2010, 2012, 2014, 2016, 2018, 2020, 2021]
pop = [179.4, 187.3, 195.3, 203.6, 204.73, 208.57, 212.48]

year1 = [2010, 2012, 2014, 2016, 2018, 2020, 2021]
pop1 = [197.4, 204.3, 209.3, 209.6, 208.73, 215.57, 218.48]

# Build a Line Chart
plt.scatter(x=year, y=pop, color='green', marker="*",
            alpha=1, s=100, label="pakistan poluation")

plt.scatter(x=year1, y=pop1, color='red', marker="+",
            alpha=1, s=100, label="Indian poluation")

plt.grid()
plt.legend()

# Setting Label in x & y cordinate
plt.xlabel("Year Wise Data")
plt.ylabel("Population in Million")
plt.title("Population Projection Between Pakistan vs India")

plt.show()
