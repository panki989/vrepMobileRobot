# -*- coding: utf-8 -*-
"""
Spyder Editor
Created on Thu Oct 15 17:45:09 2019
@author: Pankaj Chaurasia

"""

import vrep
import sys
import numpy as np
import matplotlib.pyplot as mlp

vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5)
if clientID!=-1:
    print ('Connected to remote API server')
else:
    print ('Connection not successfull')
    sys.exit('Couldn\'t connect !!!')
    
errorCode, left_motor_handle = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', vrep.simx_opmode_oneshot_wait)
errorCode, right_motor_handle = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', vrep.simx_opmode_oneshot_wait)

#errorCode = vrep.simxSetJointTargetVelocity(clientID, left_motor_handle, 0.2, vrep.simx_opmode_streaming)
#errorCode = vrep.simxSetJointTargetVelocity(clientID, right_motor_handle, 0.2, vrep.simx_opmode_streaming)

errorCode, cam_handle = vrep.simxGetObjectHandle(clientID, 'cam1', vrep.simx_opmode_oneshot_wait)
errorCode, resolution, image = vrep.simxGetVisionSensorImage(clientID, cam_handle, 0, vrep.simx_opmode_streaming)
errorCode, resolution, image = vrep.simxGetVisionSensorImage(clientID, cam_handle, 0, vrep.simx_opmode_blocking)

im = np.array(image, dtype = np.uint8)
print (im.shape)
im.resize([resolution[0], resolution[1], 3])
print (im.shape)
mlp.imshow(im, origin='lower')
