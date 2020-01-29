#this function takes a DataFrame (pandas) and plots 2d scatter of all features
#vs target (assuming that the target is the last column of the DataFrame)

import math
import matplotlib.pyplot as plt
import pandas as pandas

def plotFeatureAnalysis(dataFrame):

    size = len(dataFrame.columns)
    n = int(math.ceil(math.sqrt(size)))

    fig, axes = plt.subplots(nrows=n, ncols=n)
    fig.tight_layout()

    plotIndex=0

    for column in dataFrame:
        if plotIndex == size - 1:
            break
        dataFrame.plot(kind='scatter', x=column, y=dataFrame.columns[-1],ax=axes[plotIndex/n, plotIndex % n])
        plotIndex = plotIndex + 1

    plt.show()

def plotAllFeatures(dataFrame):

    size = len(dataFrame.columns)
    k = size*size
    n = int(math.ceil(math.sqrt(k)))

    print(n)

    fig, axes = plt.subplots(nrows=n, ncols=n)
    fig.tight_layout()

    plotIndex=0

    for columnA in dataFrame:
        for columnB in dataFrame:
            print(plotIndex)
            #if plotIndex == k - 1:
            #break
            dataFrame.plot(kind='scatter', x=columnA, y=columnB, ax=axes[plotIndex/n, plotIndex % n])
            plotIndex = plotIndex + 1


    plt.show()
