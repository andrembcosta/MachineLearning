#this function takes a DataFrame (pandas) and plots 2d scatter of all features
#vs target (assuming that the target is the last column of the DataFrame)

import math
import matplotlib.pyplot as plt
import pandas as pandas

def plotFeatureAnalysis(dataFrame):

    from matplotlib import ticker
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True)
    formatter.set_powerlimits((-1,1))
    plt.rcParams.update({'axes.labelsize': 16})

    size = len(dataFrame.columns)
    n = int(math.ceil(math.sqrt(size)))

    fig, axes = plt.subplots(nrows=n, ncols=n, figsize=(14, 10))
    fig.tight_layout(pad=3.0)

    plotIndex=0

    for column in dataFrame:
        if plotIndex == size - 1:
            break
        ax=axes[plotIndex/n, plotIndex % n]
        dataFrame.plot(kind='scatter', x=column, y=dataFrame.columns[-1],ax=ax)
        ax.yaxis.set_major_formatter(formatter)
        plotIndex = plotIndex + 1

    title = 'Plot to identify correlation between all the features and target(price)'
    fig.suptitle(title, fontsize=18, y=1)
    fig.savefig(title+'.png', bbox_inches='tight')
    plt.show()

def plotAllFeatures(dataFrame):

    size = len(dataFrame.columns)
    n = int(math.ceil(math.sqrt(size)))


    from matplotlib import ticker
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True)
    formatter.set_powerlimits((-1,1))
    plt.rcParams.update({'axes.labelsize': 16})

    # fig, axes = plt.subplots(nrows=n, ncols=n)
    # fig.tight_layout()
    plotIndex=0
    figureIndex=0

    for columnA in dataFrame.columns[:-1]:
        plotIndex=0
        plt.figure(figureIndex)
        fig, axes = plt.subplots(nrows=n-1, ncols=n, figsize=(14, 10))
        fig.tight_layout(pad=3.0)
        for columnB in dataFrame.columns[:-1]:
            if columnB == columnA:
                continue
            ax=axes[plotIndex/n, plotIndex % n]
            dataFrame.plot(kind='scatter', x=columnA, y=columnB, ax=ax)
            ax.yaxis.set_major_formatter(formatter)
            plotIndex = plotIndex + 1
        title = 'Plot to identify correlation between features. All features vs ' + columnA
        fig.suptitle(title, fontsize=18, y=1)
        figureIndex = figureIndex + 1
        fig.savefig(title+'.png', bbox_inches='tight')


    #plt.show()
