import matplotlib.pyplot as plt
import pandas as pd
import csv

readcsv = pd.read_csv(r"C:\Users\rajaa\Desktop\Github Repo\Python-Examples\Python\Matplotlib\age.csv")
ages = readcsv['Age']

plt.style.use('fivethirtyeight')

# ages = [18,15,11,14,21,24,34,38,33,42,45,48,49,54,60]
bins = [10,20,30,40,50,60]
plt.hist(ages,bins=bins,edgecolor='black')


plt.title("Age of respondent")
plt.legend(loc=(0.05,0.07))
plt.tight_layout()
plt.show()