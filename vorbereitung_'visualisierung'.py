


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/home/ysf/Downloads/layer_data.csv")
df = pd.DataFrame(data)

#1. Wie viel Anteil hat jedes Layer an der Gesamtzeit ? (alt)

df.groupby(['node type','layerIndex']).sum().unstack().plot(kind='bar',y='avg_ms', stacked=True)

#2. Wenn man alle Layer eines node types zusammenzählt: Welcher node type hat die längste Latenz ?

k = df.groupby("node type")['avg_ms'].sum()
k.plot(title = 'sum Latenz',ylabel ='avg_ms',kind = 'bar',stacked = True , logy = True )

#3. Wie lange ist die kürzeste/längste/durchschnittliche Latenz für die Summen nach node type ?

df.boxplot(by ='node type', column =['avg_ms'], grid = True, figsize=(15 , 15) )
plt.yscale("log")

