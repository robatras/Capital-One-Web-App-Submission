
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from math import sin, cos, sqrt, atan2, radians

df = pd.read_csv("metro-bike-share-trip-data.csv", sep=',')
fig, ax = plt.subplots(figsize=(8,6))

R = 3959.0 #radius of earth in miles

col = "Distance Traveled (miles)"
def distance(each_col):
    #haversine formula
    if each_col.isnull().any(): 
        return 0 
    else:
        starting_stat_lat = each_col["Starting Station Latitude"]
        starting_stat_long = each_col["Starting Station Longitude"]
     
        
        ending_stat_lat = each_col["Ending Station Latitude"]
        ending_stat_long = each_col["Ending Station Longitude"]
         
        lat1 = radians(starting_stat_lat)
        lon1 = radians(starting_stat_long)
        lat2 = radians(ending_stat_lat)
        lon2 = radians(ending_stat_long)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return distance

#creates data frame: Distance Traveled (miles)
#Goes through each row and finds distance between start and end and adds it to the dataframe
df[col] = df.apply(distance, axis=1)
#removes the extreme datapoints. Before, there was a max that was 7809 miles.
non_extreme = df[
        (df[col] > df[col].quantile(0.05)) & (df[col] <= df[col].quantile(0.95))]
print(non_extreme[col].describe())
sns.distplot(non_extreme[col], color="coral" )
ax.set_title("Histogram of Distance Traveled", size = 20)
plt.savefig("avg_distance.png")



