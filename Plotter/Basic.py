import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def avatarheatmap(df,nofgrid=6):

    # 3d mode, 2d mode, number of grids

    def remap(x, nofgrid):
        return np.floor((x - -9) * (nofgrid - 1) / (9 - -9) + 1)

    htmp = np.zeros((nofgrid,nofgrid))

    remapped = df.applymap(remap)
    heatmap = plt.hist2d(remapped.iloc[:,0],remapped.iloc[:,1],bins=[np.arange(0,nofgrid+1,1),np.arange(0,nofgrid+1,1)])
    # grouped = remapped.groupby([0, 1]).size()
    # newdf = grouped.to_frame(name='Instances').reset_index()

    # location = np.reshape(newdf['Instances'],(nofgrid,nofgrid)) # problematic when there are 0 counts.
    # sns.heatmap(location)
    plt.show()
    return heatmap


def hist(data_cal, duration_start=1, duration_end=data_cal.index[-1]):
    """
    This function plots histogram
    :param data_cal: DataFrame output from forUsers.py or others
    :param duration_start: start point you want to analyze
    :param duration_end: end point you want to analyze
    :return: plotting
    """
    sns.set()
    x = duration_start:data_cal.index[-1]
    y = data_cal[duration_start:data_cal.index[-1]]
    plt.plot(x, y)

# 2 dimension in AVATAR
def scatter(dataname, ):
    xline = np.linspace(-20, 20, 21)
    yline = np.linspace(-20, 20, 21)
    zline = np.linspace(-5, 40, )
    plt.scatter(x, y, z, )
