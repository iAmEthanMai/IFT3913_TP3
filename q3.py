import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Question 3
#code pour NOCom vs DCP seulement

#read csv file and store in dataframe
df = pd.read_csv('/Users/ethanmai/Downloads/jfreechart-stats.csv')


NOCom = df[' NOCom']
DCP = df[' DCP']


#get NoCom > 10 and NoCom < 10
NOCom1 = NOCom[NOCom > 10]
NOCom2 = NOCom[NOCom < 10]

#get DCP associated to NOCom1 and DCP associated to NOCom2
DCP1 = DCP[:len(NOCom1)]
DCP2 = DCP[len(NOCom1):]

#plot  NOCom and DCP 
plt.scatter(NOCom, NCLOC , color='red', marker='o', s=10)
#plot NOCom = 10
plt.axvline(10, color='blue', linestyle='dashed', linewidth=1)


#average NCLOC for NOCom > 10
avg1 = DCP1.mean()
#average NCLOC for NOCom < 10
avg2 = DCP2.mean()

print(avg1,avg2)


#regression line
m, b = np.polyfit(NOCom, NCLOC, 1)
plt.plot(NOCom, m*NOCom + b, color='blue')

#label the plot
plt.title("DCP vs NOCom")
plt.xlabel("NOCom")
plt.ylabel("DCP")

#show plot
plt.show()
