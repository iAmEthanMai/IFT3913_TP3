import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Question 1
#code pour DCP seulement (meme logique pour NCLOC et NOCom)

#read csv file and store in dataframe
df = pd.read_csv('/Users/ethanmai/Downloads/jfreechart-stats.csv')

data = df[' DCP']
median = data.median()
q1 = data.quantile(0.25)
q3 = data.quantile(0.75)

#max and min values
max_ = data.max()
min_ = data.min()

plt.boxplot(data)
#show the median of the data
plt.axhline(median, color='r', linestyle='dashed', linewidth=1)
#show the first quartile of the data
plt.axhline(q1, color='r', linestyle='dashed', linewidth=1)
#show the third quartile of the data
plt.axhline(q3, color='r', linestyle='dashed', linewidth=1)

#labels
plt.title('Boxplot of DCP')
plt.ylabel('DCP')
