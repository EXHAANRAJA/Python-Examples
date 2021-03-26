import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

year = [2010, 2012, 2014, 2016, 2018, 2020, 2021]
pop = [179.4, 187.3, 195.3, 203.6, 204.73, 208.57, 212.48]

year1 = [2010, 2012, 2014, 2016, 2018, 2020, 2021]
pop1 = [197.4, 204.3, 209.3, 209.6, 208.73, 215.57, 218.48]

# Build a Line Chart
plt.plot(year, pop, color='k', linestyle='--',
         alpha=1, marker='.', label="pakistan poluation")
plt.plot(year1, pop1, color='b', linestyle='-',
         alpha=1, marker='o', label="Indian poluation")

# Setting Label in x & y cordinate
plt.xlabel("Year Wise Data")
plt.ylabel("Population in Million")
plt.title("Pakistan Population Projection")

plt.legend()
plt.tight_layout()
plt.show()
