import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Question 2
#code pour NOCom vs DCP seulement

#read csv file and store in dataframe
df = pd.read_csv('/Users/ethanmai/Downloads/jfreechart-stats.csv')



NOCom = df[' NOCom']
DCP = df[' DCP']

#remove outliers in NOCom with IQR
q1 = NOCom.quantile(0.25)
q3 = NOCom.quantile(0.75)
iqr = q3 - q1
NOCom = NOCom[~((NOCom < (q1 - 1.5 * iqr)) |(NOCom > (q3 + 1.5 * iqr)))]

#remove outliers in DCP with IQR
q1 = DCP.quantile(0.25)
q3 = DCP.quantile(0.75)
iqr = q3 - q1
DCP = DCP[~((DCP < (q1 - 1.5 * iqr)) |(DCP > (q3 + 1.5 * iqr)))]

#remove the missing values
if len(DCP) > len(NOCom):
    DCP = DCP[:len(NOCom)]
else:
    NOCom = NOCom[:len(DCP)]


#plot the data
plt.scatter(NOCom, DCP, color='red', marker='o', s=10)
#calculate the correlation coefficient
corr = np.corrcoef(NOCom, DCP)
print(corr)

#plot the regression line
m, b = np.polyfit(NOCom, DCP, 1)
plt.plot(NOCom, m*NOCom + b, color='blue')

#add title
plt.title("NOCom vs DCP without outliers")
#add label
plt.xlabel("NOCom")
#add label
plt.ylabel("DCP")
plt.show()
