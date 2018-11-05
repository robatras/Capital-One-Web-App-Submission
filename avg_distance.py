import pandas as pd  
import geopy.distance
from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 3956.0



df = pd.read_csv("metro-bike-share-trip-data.csv", sep=',')


starting_stat_lat = df["Starting Station Latitude"].mean()
starting_stat_long = df["Starting Station Longitude"].mean()
coords_1 = (starting_stat_lat, starting_stat_long)
print (coords_1)
ending_stat_lat = df["Ending Station Latitude"].mean()
ending_stat_long = df["Ending Station Longitude"].mean()

coords_2 = (ending_stat_lat, ending_stat_long)
print (coords_2)
avg_distance = (geopy.distance.vincenty(coords_1, coords_2).miles)

print (avg_distance)
#outputs: 0.9137436799130995

lat1 = radians(starting_stat_lat)
lon1 = radians(starting_stat_long)
lat2 = radians(ending_stat_lat)
lon2 = radians(ending_stat_long)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c
print (distance)