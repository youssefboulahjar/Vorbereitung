

#1. Wie viel Anteil hat jedes Layer an der Gesamtzeit ? (alt)


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("layer_data.csv")
df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 2])
Z = list(df.iloc[:, 1])

dic = {}
for i in range(len(Y)):
	if Z[i] in dic.keys():
		dic[Z[i]] += Y[i]
	else:
		dic[Z[i]] = Y[i]

for k in dic.keys():
	plt.bar(["Layer_Type"], dic[k], label=k, log = True)
 
plt.title("Anteil layers an der Gesamtzeit ")
plt.ylabel("avg_ms")
plt.show()

#1. Wie viel Anteil hat jedes Layer an der Gesamtzeit ? (neu)"""

#k = df.groupby(['node type']).sum().drop(columns=['layerIndex']).unstack()
#k.plot(stacked = True,kind='bar', logy = True)
#df.groupby(['node type'])['avg_ms'].sum().plot(stacked = True,kind='bar', logy = True)
df.groupby(['node type','layerIndex']).sum().unstack().plot(kind='bar',y='avg_ms', stacked=True)
k


#2. Wenn man alle Layer eines node types zusammenzählt: Welcher node type hat die längste Latenz ?


k = df.groupby("node type")['avg_ms'].sum()
k.plot(title = 'sum Latenz',ylabel ='avg_ms',kind = 'bar',stacked = True , logy = True )

#3. Wie lange ist die kürzeste/längste/durchschnittliche Latenz für die Summen nach node type ?

df.boxplot(by ='node type', column =['avg_ms'], grid = True, figsize=(15 , 15) )
plt.yscale("log")
