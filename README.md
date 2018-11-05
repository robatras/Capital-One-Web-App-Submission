# CapitalOne Challenge (Software Engineering Summit 2019)
#### built by Rohan Batra

Challenge: https://www.mindsumo.com/contests/bikeshare-data

Submission (deployment link): https://capitalonewebapp.herokuapp.com/


# Built With...
* HTML, CSS, Python, Flask, Bootstrap
# Objectives 

### Main Objectives
- **Data Visuals: Display or graph 3 metrics or trends from the data set that are interesting to you.
- **Which start/stop stations are most popular?
- ** What is the average distance traveled?
- **How many riders include bike sharing as a regular part of their commute?

# How objectives were completed

### **Visualize the data**: Graph some (any 3) interesting metrics, maps, or trends from the dataset.
Created 3 graphs with Chartjs:
* **Average Number of Reviews Per Host vs Year Since Host**
    * The longer a host has been a host, the more reviews they tend to have.
* **Review Score Rating vs Square Feet**
    * Bigger places doesn't necessarily mean better ratings
* **Average Price per Night vs Bedrooms**
    * On average, the more bedrooms there are, the higher the price. If you got a lot of bedrooms, it may be best to keep the price relatively high.

### **Price estimation**: Given the geo-location (latitude and longitude) of a new property, estimate the weekly average income the homeowner can make with Airbnb.
Look for places that are within 0.01 of the user's property's latitude and longitude, then took the average of the places' prices. Multiply by 7 to get estimated weekly income.

### **Bookings optimization**: Given the geo-location (latitude and longitude) of a property, what is the ideal price per night that will yield maximum bookings.
Look for places that are within 0.01 degrees of the user's property's latitude and longitude, then took the average of the places' prices.

### **Animate**: Add an animation to your visualization.
* Loading screen
* Notification that fades in and out at the bottom of the screen when there's an error related to the location service
* Hovering on a data point on each graph reveals a tooltip detailing the data.
