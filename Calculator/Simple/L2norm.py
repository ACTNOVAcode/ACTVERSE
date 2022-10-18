import numpy as np
import ctypes
import math

#CK
def bodylength(dataframe):
    """
    Calculates the body length in the current frame;

    :param dataframe: must include columns with names 'Nose_x','Anus_x','Nose_y','Anus_y','Nose_z','Anus_z'
    :return: the body length of the animal in the current frame
    """
    workingframe = np.diff(dataframe.loc[:,['Nose_x','Anus_x','Nose_y','Anus_y','Nose_z','Anus_z']],axis=1)
    length = np.linalg.norm(workingframe[:,0::2],ord=2,axis=1)
    return length


def movement(dataframe):
    """
    Calculates the movement per frame;
    Can specify column names and calculate movement of certain body part;
    can input whole csv to findout freezing score

    :param dataframe: dataframe loaded by loader package
    :return: movement between frames
    """
    # try:
    #     #     (type(coi) == list) & (type(foi) == list)
    #     # except KeyError(key):
    #     #     raise KeyError('Columns and frames of interest must be a list')
    #     # wanted to check whether the coi and foi where list beforehand; does not print; instead raised KeyError, but cannot catch that either


    workingframe = dataframe
    difference = np.diff(workingframe,axis=0)
    distance = np.linalg.norm(difference,axis=1)
    return distance


# JS
def vel(centerpoint):
    """
    This function calculates velocity at each frame from AVATAR csv file
    :param centerpoint: DataFrame users want to calculate (must have specific columns from output of 'load' function)
    :return: moving distance at each frame(velocity) of the cols. (format: Series)
    """
    if len(centerpoint.columns) > 3:   # Data point should be less than 3D.
        ctypes.windll.user32.MessageBoxW(0, u"Data columns could not have more than 3.", u"Error", 0)

    data_diff_sq = centerpoint.diff(axis=0) ** 2   # (frame(N+1)-frame(N))^2
    velocity = data_diff_sq.sum(axis=1, skipna=False) ** (1 / 2)  # (dx^2+dy^2)^(1/2)
    return velocity


def accel(centerpoint):
    """
    This function calculates acceleration at each frame from AVATAR csv file
    :param centerpoint: DataFrame users want to calculate (must have specific columns from output of 'load' function)
    :return: acceleration at each frame of the cols. (format: Series)
    """
    if len(centerpoint.columns) > 3:   # Data point should be less than 3D.
        ctypes.windll.user32.MessageBoxW(0, u"Data columns could not have more than 3.", u"Error", 0)

    data_ddiff_sq = centerpoint.diff(axis=0).diff(axis=0) ** 2     # (frame_diff(N+1)-frame_diff(N))^2
    acceleration = data_ddiff_sq.sum(axis=1, skipna=False) ** (1 / 2)  # (dx^2+dy^2)^(1/2)
    return acceleration


def centerFrameBool(centerpoint, radius=3):
    """
    This function(for AVATAR) returns frames when a mouse enters the center zone
    :param centerpoint: (x,y columns) DataFrame users want to calculate (must have specific columns)
    :param radius: if radius=3, center zone would be (-3,-3)~(3,3) for x, y axis
    :return: boolean results whether a mouse enters into the center zone
    """
    centerpoint_x = centerpoint.iloc[:, 0]    # x coordinates of the data
    centerpoint_y = centerpoint.iloc[:, 1]    # y coordinates of the data
    center_frame = (abs(centerpoint_x) < radius) & (abs(centerpoint_y) < radius)
    return center_frame


def centerIndex(center_frame, radius=3):
    """
    This function(for AVATAR) returns indices that contain True values in center_frame
    :param center_frame: boolean results whether a mouse enters into the center zone
    :param radius: if radius=3, center zone would be (-3,-3)~(3,3) for x, y axis
    :return: list of indices of dataframe(center_frame that is the output of function centerFrameBool)
    """
    center_index = center_frame.index[center_frame].tolist()
    return center_index


def walkFrameBool(velocity, vel_thres=0.2, moving_windows=7):
    velocity_conv = velocity.rolling(moving_windows, center=True).mean()




# KH

# First_data = avatarcsvloader('H14.mat.csv_new')

##1코 2머리 3항문 4몸통 5오른발 6왼발 7오른손 8왼손 9꼬리
#xyz 순

# nose = First_data.iloc[:, 0:2]
# head = First_data.iloc[:, 3:5]
# ass = First_data.iloc[:, 6:8]
# body = First_data.iloc[:, 9:11]
# left_hindlimb = First_data.iloc[:, 12:14]
# right_hindlimb = First_data.iloc[:, 15:17]
# left_forelimb = First_data.iloc[:, 18:20]
# right_forelimb = First_data.iloc[:, 21:23]
# tail = First_data.iloc[:, 24:26]

# 각 body part 의 velocity 계산 일반 velocity 의 경우 Torso 이용
def velocity(Dataname, frame_rate='30', bodypart='Torso'):
    # bodypart 의 이름은 column_index 참조
    cor_x = Dataname.loc[:, bodypart+'_x']
    cor_y = Dataname.loc[:, bodypart+'_y']
    cor_z = Dataname.loc[:, bodypart+'_z']
    distance_x = math.pow(numpy.diff(cor_x))
    distance_y = math.pow(numpy.diff(cor_y))
    distance_z = math.pow(numpy.diff(cor_z))
    output = math.sqrt(distance_x+distance_y+distance_z)/frame_rate
    return output

#angular velocity _ Rotation counting 을 위한 기초 function
def ang_velocity(Dataname, frame_rate='30', ):
#원점 고정하기
def fixation_Ass(Dataname):
    dislocation_x = Dataname[:, 'Ass_x']
    dislocation_y = Dataname[:, 'Ass_y']
    dislocation_z = Dataname[:, 'Ass_z']
    for i in range(0, 8)
        Dataname[:, 3*i] = Dataname[:, 3*i] - dislocation_x
        Dataname[:, 1+3*i] = Dataname[:, 1+3*i] - dislocation_y
        Dataname[:, 2+3*i] = Dataname[:, 2+3*i] - dislocation_z
        i = i + 1
    return Dataname
#Torso-ass vector 로 fix
def fixation_trunk(Dataname, bodypart):
    fixVec = Torso-ass


#RH, RF, LH, LF 가 바닥에 닿는 시점(*z 값 범위 설정 필요)들의 x,y 좌표 visualize frame by frame.




#lotation counting + rotation behavior 의 특징을 찾는 function도 좋을듯.
#def lotation_counting():

#limb Trajectory
#원점 고정 후 trajectory ?
def trajectory(Dataname, bodypart):
    cor_x = Dataname.loc[:, bodypart + '_x']
    cor_y = Dataname.loc[:, bodypart + '_y']
    cor_z = Dataname.loc[:, bodypart + '_z']



#Right Forelimb and hindlimb
# z=0 일때 혹은 0~? 사이에 있을때 point. XY plane 에서