import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
from matplotlib import cm

#my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(df)))
#plt.rcParams["font.family"] = "DejaVu Sans"
plt.title("Test",fontname="Times New Roman",fontweight="bold")

x = [{i:random.randint(1,5)} for i in range(30)]

df = pd.read_csv("metro-bike-share-trip-data.csv")
my_colors = [(x/10.0, x/20.0, 0.75) for x in range(len(df))] # <-- Quick gradient example along the Red/Green dimensions.

sns.color_palette("Set2", 10)
col= "Ending Station ID"
df[col] = df[col].fillna("0").astype(int)
my_list = []
my_list.append(list((df[col].mode())))
color = cm.inferno_r(np.linspace(.4,.8, 30))
my_list.append(((df[col].value_counts()[df[col].value_counts() == df[col].value_counts().max()]).tolist()))
ax = df[col].value_counts().head().plot(kind='bar',  color=sns.color_palette("husl", 8), legend=False)
ax.set_title("Most Popular Starting Stations", size = 20)

ax.set_xlabel("Starting Station ID Numbers", size = 15)
ax.set_ylabel("Number of times used", size = 15)
ttl = ax.title
ttl.set_position([.5, 1.05])


ax.patch.set_facecolor('white')
plt.savefig("demo.png")




