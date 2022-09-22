import pandas

def avatarloader(filename, givenpath ='D:/raw/'):
    fullname = givenpath+filename+'.csv'
    column_index = ['Nose_x', 'Nose_y', 'Nose_z', 'Head_x', 'Head_y', 'Head_z', 'Ass_x', 'Ass_y', 'Ass_z', 'Torso_x', 'Torso_y', 'Torso_z',
                    'RH_x', 'RH_y', 'RH_z', 'LH_x', 'LH_y', 'LH_z', 'RF_x', 'RF_y', 'RF_z', 'LF_x', 'LF_y', 'LF_z', 'Tail_x', 'Tail_y', 'Tail_z']
    output = pandas.read_csv(fullname, names=column_index)
    return output
