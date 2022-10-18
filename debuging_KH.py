import pandas as pd
from itertools import product

dataname = load()

def pawStep(dataname, bodypart=['RH','RF', 'LH', 'LF']):
    cor = ['x', 'y', 'z']
    separator = '_'
    bodypartlist = [separator.join(label) for label in list(product(bodypart, cor))]
    paw_position = pd.DataFrame(index=range(len(data.index)), columns = bodypartlist)
    for i in range(0, len(data))
    if cor_z[i]>-1 and cor_z[i]<1.5
        paw_position[0, i] = cor_x[i]
        paw_position[1, i] = cor_y[i]


def calAngle(dataname, joint=('nose', 'head', 'torso'), xyz=('x', 'y', 'z')):
    cor = xyz
    separator = '_'
    bodypartlist = [separator.join(label) for label in list(product(joint, xyz))]
    firstVector_x = [dataname[bodypartlist[0]]-dataname(bodypartlist[3])]
    firstVector_y = [dataname(bodypartlist[1])-dataname(bodypartlist[4])]
    firstVector_z = [dataname(bodypartlist[2])-dataname(bodypartlist[5])]
    secondVector_x = []
    secondVector_y = []
    secondVector_z = []

    return angle



def cal_vel(data, joint='head', xyz=('x', 'y')):
    """
    this function calculates velocity at each frame from AVATAR csv file
    :param data: raw data, csv file from AVATAR
    :param joint: (tuples) joint you want to calculate
    :param xyz: (tuples) coordinates you want to calculate
    :return: moving distance at each frame(velocity) of the joint+xyz
    """
    data_diff_sq = data.diff(axis=0) ** 2

    cols = []  # joints plotted
    velocity = pd.DataFrame()
    if type(joint) == str:
        for ii in xyz:
            cols.append(joint + '_' + ii)
        # (dx^2+dy^2)^(1/2)
        velocity[joint + '-' + ''.join(xyz)] = data_diff_sq[cols].sum(axis=1, skipna=False) ** (1 / 2)
    else:
        for i in joint:
            for ii in xyz:
                cols.append(i + '_' + ii)
            # (dx^2+dy^2)^(1/2)
            velocity[i + '-' + ''.join(xyz)] = data_diff_sq[cols].sum(axis=1, skipna=False) ** (1 / 2)

    return velocity


def cal_accel(data, joint='head', xyz=('x', 'y')):
    """
    this function calculates acceleration at each frame from AVATAR csv file
    :param data: raw data, csv file from AVATAR
    :param joint: (tuples) joint you want to calculate
    :param xyz: (tuples) coordinates you want to calculate
    :return: acceleration at each frame of the joint+xyz
    """
    data_ddiff_sq = data.diff(axis=0).diff(axis=0) ** 2

    cols = []  # joints plotted
    accel = pd.DataFrame()
    if type(joint) == str:
        for ii in xyz:
            cols.append(joint + '_' + ii)
        # (ddx^2+ddy^2)^(1/2)
        accel[joint + '-' + ''.join(xyz)] = data_ddiff_sq[cols].sum(axis=1, skipna=False) ** (1 / 2)
    else:
        for i in joint:
            for ii in xyz:
                cols.append(i + '_' + ii)
            # (ddx^2+ddy^2)^(1/2)
            accel[i + '-' + ''.join(xyz)] = data_ddiff_sq[cols].sum(axis=1, skipna=False) ** (1 / 2)

    return accel

def pawstep(Dataname, bodypart='RH'):
    cor_x = Dataname.loc[:, bodypart+'_x']
    cor_y = Dataname.loc[:, bodypart+'_y']
    cor_z = Dataname.loc[:, bodypart+'_z']
    paw_position = pd.dataframe(len(Dataname), 2)
    for i in range(0, len(Dataname))
    if cor_z[i] > -1 and cor_z[i] < 1.5
        paw_position[0, i] = cor_x[i]
        paw_position[1, i] = cor_y[i]