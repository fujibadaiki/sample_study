
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output

print(check_output(["ls", "./input"]).decode("utf8"))

data = pd.read_csv('./input/pokemon.csv')


print(data.head())

print(data['Type 1'].value_counts(dropna =False))  

print(data.describe())

#data.plot(column='Attack',by = 'Legendary')

#plot.show()

'''
#correlation map
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt= '.1f', ax=ax)

data.head(10)

data.columns
'''