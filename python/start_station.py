
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



plt.title("Test",fontname="Times New Roman",fontweight="bold")
df = pd.read_csv("metro-bike-share-trip-data.csv")

col= "Starting Station ID"
df[col] = df[col].fillna("0").astype(int)

sns.set_style("darkgrid")
ax = df[col].value_counts().head().plot(kind='bar',  color=sns.color_palette("husl", 8), legend=False)
ax.set_title("Most Popular Starting Stations", size = 20)
ax.set_xlabel("Starting Station ID Numbers", size = 15)
ax.set_ylabel("Number of times used", size = 15)
ttl = ax.title
ttl.set_position([.5, 1.0])



plt.savefig("popular_starting_stations.png")
