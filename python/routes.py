import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import cm
from pylab import rcParams

plt.rcParams["font.family"] = "DejaVu Sans"
rcParams['figure.figsize'] = 1, 1
df = pd.read_csv("metro-bike-share-trip-data.csv", sep=',')


fig, ax = plt.subplots(figsize=(8,7))
sns.set_style("white")

sns.set_palette("husl")
col= "Trip Route Category"
ax = df[col].value_counts().plot(kind='barh', fontsize = 10, legend = False)
ax.set_title("Trip Routes Types", size = 20)
ax.set_xlabel("Number of people", size = 10)
plt.savefig("routes.png")
