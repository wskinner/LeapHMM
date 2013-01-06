import numpy as np
import csv
# gesture_name: file name

def train(gesture):
    for obs in getObservations(gesture.name):
        gesture.fit(obs, init_params='')

def getObservations(gesture_name):
    observations = []
    with open(gesture_name+'.csv', 'rb') as f:
        current_obs = []
        reader = csv.reader(f)
        for line in reader:
            if int(line[0]) > len(observations):
                observations.append(np.array(current_obs))
                current_obs = []
            else:
                current_obs.append(np.array(line[1:]))
    return observations
    
######################################################
# Training data looks like:
# 
# 1, p1, p2, p3, ...
# 2, p1, p2, p3, ...
#    .
#    .
#    .

