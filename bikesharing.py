import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import cm
from pylab import rcParams

plt.rcParams["font.family"] = "DejaVu Sans"
rcParams['figure.figsize'] = 1, 1
df = pd.read_csv("metro-bike-share-trip-data.csv", sep=',')

plt.style.use('ggplot')
plt.figure(1, figsize=(10,10))
sns.color_palette("Set2", 10)
color = cm.inferno_r(np.linspace(.4,.8, 30))
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
sns.set_palette("husl")
col= "Passholder Type"
ax = df[col].value_counts().plot(kind='pie', autopct='%1.1f%%', fontsize = 20, legend = True)
ax.set_title("Passholder Types", size = 20)
plt.legend(bbox_to_anchor=(0.95, .9), loc=2, borderaxespad=0)
plt.savefig("passholdertypes1.png")
