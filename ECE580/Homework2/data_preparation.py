#script to clean the dataset

#step 1: read the .data file (comma-separated) with pandas

import pandas as pandas
import matplotlib.pyplot as plt
from feature_analysis import plotFeatureAnalysis
from feature_analysis import plotAllFeatures

pandas.set_option('display.max_rows', None)

car_data = pandas.read_csv("imports-85.data", header = None)

#Total number of data points (cars) = 205
#Total number of features = 25

#step 2: rename the columns of continuous data

columnsDictionary = {9:"wheel-base", 10:"length", 11:"width", 12:"height",\
13:"curb-weight", 16:"engine-size", 18:"bore", 19:"stroke", 20:"compression-ratio",\
21:"horsepower", 22:"peak-rpm", 23:"city-mpg", 24:"highway-mpg", 25:"price"};

car_data = car_data.rename(columnsDictionary, axis = 'columns')

#no change in the size of the data set

#step 3: remove the non-continuous data from the table

columnsOfInterest = list(columnsDictionary.values())

car_data = car_data[columnsOfInterest]

#removed 12 features

#step 4: remove all data points with missing data
#print(car_data)
toDrop = list()
for index, row in car_data.iterrows():
    if ('?' in row.values):
        toDrop.append(index)

print(toDrop)
car_data.drop(car_data.index[toDrop], inplace=True)
car_data.reset_index(drop=True, inplace=True)
car_data = car_data.apply(pandas.to_numeric)
print(car_data)

plotFeatureAnalysis(car_data)
plotAllFeatures(car_data)

#removed 10 data points

#Total number of data points (cars) remaining = 195
#Total number of features = 13
