#script to clean the dataset

#step 1: read the .data file (comma-separated) with pandas

import pandas as pandas
import matplotlib.pyplot as plt
from feature_analysis import plotFeatureAnalysis
from feature_analysis import plotAllFeatures

#pandas.set_option('display.max_rows', None)

car_data = pandas.read_csv("imports-85.data", header = None, na_values = "?")

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

car_data.dropna(subset=['price'], inplace=True)
car_data.reset_index(drop=True, inplace=True)
car_data = car_data.apply(pandas.to_numeric)
print(car_data)

#removed 10 data points

#Total number of data points (cars) remaining = 195
#Total number of features = 13

#plotFeatureAnalysis(car_data)
#plotAllFeatures(car_data)

#select variables for Model
#columnsModel1 = ["curb-weight", "engine-size", "city-mpg", "price"]
columnsModel1 = ["curb-weight", "engine-size", "city-mpg", "price"]
columnsModel2 = ["curb-weight",  "horsepower", "city-mpg", "price"]
columnsModel3 = ["curb-weight", "engine-size", "highway-mpg", "price"]

dataModel1 = car_data[columnsModel1]
dataModel2 = car_data[columnsModel2]
dataModel3 = car_data[columnsModel3]
print(dataModel1)

#modify data

dataModel1['curb-weight'] = dataModel1['curb-weight'] ** 2
dataModel2['curb-weight'] = dataModel2['curb-weight'] ** 2
dataModel3['curb-weight'] = dataModel3['curb-weight'] ** 2
#dataModel1['city-mpg'] = 1 / dataModel1['city-mpg']
dataModel2['city-mpg'] = 1 / dataModel2['city-mpg']
dataModel3['highway-mpg'] = 1 / dataModel3['highway-mpg']

#perform regressions

from regression import linearRegression

linearRegression(dataModel1,'model 1', 'predicted price ($)', 'actual price ($)')
linearRegression(dataModel2,'model 2', 'predicted price ($)', 'actual price ($)')
linearRegression(dataModel3,'model 3', 'predicted price ($)', 'actual price ($)')
