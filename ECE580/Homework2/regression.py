#Regression analysis

import pandas as pandas
import matplotlib.pyplot as plt
from sklearn import linear_model

#this function takes a pandas dataFrame and perform a standard linear regression
#of the n-1 first columns with the last columns as the target variable
#if one wants to use only a few columns of the dataFrame or wants to square
#a column, this needs to be done prior to calling the function (by creating
#another dataFrame)
def linearRegression(dataFrame, title, xlabel, ylabel):

    model = linear_model.LinearRegression()
    dataFrame.dropna(inplace=True)
    X = dataFrame.iloc[:,:-1].values.reshape(-1, len(dataFrame.columns)-1)
    y = dataFrame.iloc[:,-1]
    model = model.fit(X, y)
    y_pred = model.predict(X)
    print('Coefficients: \n', model.coef_)
    print('This model score is:')
    print(model.score(X,y))

    #Print
    fig = plt.figure()
    plt.scatter(y_pred, y)
    plt.plot(y_pred, y_pred)
    fig.suptitle(title, fontsize=18, y=1)
    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontsize=18)
    #fig.savefig(title+'.png', bbox_inches='tight')
    
