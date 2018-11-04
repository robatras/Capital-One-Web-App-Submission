import math
import matplotlib.pyplot as plt  
import pandas as pd  

import geopy.distance

#lat1, lon1 = origin
#lat2, lon2 = destination
radius = 3959 # miles



list_avg =[]

df = pd.read_csv("metro-bike-share-trip-data.csv", sep=',')

site_coords = (38.898556, -77.037852)
for index, row in df.iterrows():
    place2_coords = (row.Latitude, row.Longitude)
    x = geopy.distance.vincenty(site_coords, place2_coords).km
    print(x)