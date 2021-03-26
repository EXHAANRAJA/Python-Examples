from matplotlib import colors
import matplotlib.pyplot as plt


year = [2010, 2012, 2014, 2016, 2018, 2020, 2021]
pop = [179.4, 187.3, 195.3, 203.6, 204.73, 208.57, 212.48]

# Build a Line Chart
plt.scatter(x=year, y=pop, color='green', s=10, marker="*")
plt.grid()

# Setting Label in x & y cordinate
plt.xlabel("Year Wise Data")
plt.ylabel("Population in Million")
plt.title("Pakistan Population Projection")

plt.show()
