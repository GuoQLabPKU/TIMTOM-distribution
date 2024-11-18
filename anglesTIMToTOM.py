from nemotoc.py_transform.tom_calcPairTransForm import tom_calcPairTransForm
from nemotoc.py_transform.tom_eulerconvert_xmipp import tom_eulerconvert_xmipp
import pandas as pd
import numpy as np

import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from nemotoc.py_io.tom_extractData import tom_extractData
from nemotoc.py_transform.tom_eulerconvert_xmipp import tom_eulerconvert_xmipp
from nemotoc.py_transform.tom_pointrotate import tom_pointrotate
from tom_plot_vectorField import tom_rotVectByAng
           
data_dir = './'

#read the data 
small = pd.read_csv(data_dir + 'small_angles.csv')
big = pd.read_csv(data_dir + 'big_angles.csv',sep = "\t")
big.columns = ['particles','0','psi','rot','tilt']
phiList = []
psiList = []
thetaList = []
#covert the data euler angles 
for i in range(small.shape[0]):
    smallp = small['particles'].values[i]
    bigp = big['particles'].values[i]
    assert smallp == bigp
    
    smallRELAngle = small.loc[i,['rot','tilt','psi']].values
    bigRELAngle = big.loc[i,['rot','tilt','psi']].values
    
    _,smallMatAngle = tom_eulerconvert_xmipp(smallRELAngle[0], smallRELAngle[1],smallRELAngle[2])
    _,bigMatAngle = tom_eulerconvert_xmipp(bigRELAngle[0], bigRELAngle[1], bigRELAngle[2])
    
    #calculate the relative angle of small to big
    _, angTr, _, _  = tom_calcPairTransForm(np.array([0,0,0]), bigMatAngle, np.array([0,0,0]), smallMatAngle, dMetric = 'exact')
    
    #save the results 
    phi,psi,theta = angTr
    phiList.append(phi)
    psiList.append(psi)
    thetaList.append(theta)

#save the result from vis 
allRelAngle = pd.DataFrame({'phi':phiList,'psi':psiList,'theta':thetaList})

#vis 
#vectsRot = tom_rotVectByAng(np.array([0,0,1]), allRelAngle.values, display = 'vector')

#covet tin to relion readable format 
rotlist = [] 
tiltlist = []
psilist = []
for i in range(allRelAngle.shape[0]):
    _, relionAngle = tom_eulerconvert_xmipp(allRelAngle['phi'].values[i], allRelAngle['psi'].values[i], allRelAngle['theta'].values[i], flag = 'tom2xmipp')
    rotlist.append(relionAngle[0])
    tiltlist.append(relionAngle[1])
    psilist.append(relionAngle[2])
    
allRelAngleRELION = pd.DataFrame({'rot':rotlist,'tilt':tiltlist,'psi':psilist})   
#save the data into RLEION or MATALB forrmat 
allRelAngleRELION.to_csv('./allResAngleRELION.csv',sep = "\t",index=False)





    
    




