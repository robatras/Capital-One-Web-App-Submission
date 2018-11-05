#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
@author: rbatra
"""
fig, ax = plt.subplots(figsize=(6,6))


df = pd.read_csv("metro-bike-share-trip-data.csv", sep=',')
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['End Time'] = pd.to_datetime(df['End Time'])
sns.color_palette("Set2", 10)
sns.set_style("whitegrid")

count_list = []
months = [1,2,3,4,5,6,7,8,9,10,11,12]

for each_month in months:
  # Count number of rides is respective month
 count_list.append(len(df[df['Start Time'].dt.month == each_month])) 


plt.title("Number of Rides per Month", size = 20)
plt.xlabel('Month')
plt.ylabel('Count')

sns.lineplot(months, count_list, color="coral", label="line")
plt.savefig("numberRidesperMonth.png")
