import pandas as pd
import math
import numpy
# from Loader import avatarscvloader

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