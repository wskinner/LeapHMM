import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir) 

from leap.lib import Leap
import utils
import pickle
import time
import csv

def loadFeatures(gesture_name):
    i = 0
    features = []
    while True:
        try:
            with open('pickled'+gesture_name+str(i), 'r') as f:
                features.append(pickle.load(f))
            i += 1
        except:
            return features

def loadFeaturesCSV(gesture_name):
    gestures = []
    with open(gesture_name+'.csv', 'rb') as f:
        reader = csv.reader(f)
        current_g = []
        for i,line in enumerate(reader):
            if i == 0:
                prev_num = int(line[0])
            if int(line[0]) > prev_num:
                prev_num = int(line[0])
                gestures.append(current_g)
                current_g = []
            current_g.append(map(float,line[1:]))
        gestures.append(current_g)
    return gestures

def dumpFeatures(gesture_list, gesture_name):
    """
    Store the features in pickled format.
    """
    i = 0
    for g in gesture_list:
        positions = [getFingerPositions(frame)[0] for frame in g if getFingerPositions(frame)]
        features = [(pos.x,pos.y,pos.z) for pos in positions if pos]
        with open('pickled'+gesture_name+str(i), 'w') as f:
            pickle.dump(features, f)
        i += 1

def dumpFeaturesCSV(gesture_list, gesture_name):
    """
    Store the features in CSV format.
    """
    with open(gesture_name+'.csv', 'wba') as f:
        writer = csv.writer(f)
        for i,g in enumerate(gesture_list):
            positions = [getFingerPositions(frame)[0] for frame in g if getFingerPositions(frame)]
            features = [(pos.x,pos.y,pos.z) for pos in positions if pos]
            for feat in features:
               writer.writerow([i]+list(feat))

def getVariance(nums):
    if len(nums) == 0:
        return 0
    count = len(nums)
    ev = sum(nums) / count
    variance = sum(map(lambda x: (x-ev)**2, nums)) / count
    return variance

def getFingerPositions(frame, hand_num=1, finger_num=1):
    positions = []
    for hand in frame.hands():
        if hand_num == 0:
            break
        for finger in hand.fingers():
            if finger_num == 0: 
                break
            positions.append(finger.tip().position)
            finger_num -= 1
        hand_num -= 1

    if positions: 
        return positions

def getNumFingers(frame):
    hands = frame.hands()
    return sum([len(hand.fingers())*1.0 for hand in hands])

def getNumHands(frame):
    hands = frame.hands()
    return len(hands)*1.0

def avgFingers(frames):
    """
        Return the square of the average number of fingers 
    """
    avg_fingers = sum([getNumFingers(frame) for frame in frames])  / len(frames)
    avg_fingers = avg_fingers ** 8
    return [avg_fingers for i in range(10)]

def fingerVariance(frames):
    """
        Return the variance of the finger positions
    """
    xs = []
    ys = []
    zs = []
    for frame in frames:
        xs.extend([pos.x for pos in get_positions(frame)])
        ys.extend([pos.y for pos in get_positions(frame)])
        zs.extend([pos.z for pos in get_positions(frame)])
    return [getVariance(xs), getVariance(ys), getVariance(zs)]

def handVariance(frames):
    """
        Return the variance of the values
    """
    # Return ((x's, y's, z's), sum, count) for all the values 
    xs = []
    ys = []
    zs = []

    for frame in frame:
        hands = frame.hands()
        if frame.hands():
            for hand in frame.hands():
                palm = hand.palm()
                if palm:
                    pos = palm.position
                    xs.append(pos.x)
                    ys.append(pos.y)
                    zs.append(pos.z)
    xvar = getVariance(xs)
    yvar = getVariance(ys)
    zvar = getVariance(zs)
    return [xvar, yvar, zvar]

def length(frames,amount_used=.1):
    """
        Returns the average distance each finger moves in the gesture
    """

    num_frames = len(frames)
    num_used = int(amount_used*num_frames)

    firsts = [[] for i in range(num_used)]
    lasts = [[] for i in range(num_used)]

    for f,first in zip(frames[0:num_used],firsts):
        positions = get_positions(f)
        for position in positions:
            first.append(position)
    for f,last in zip(frames[-num_used:],lasts):
        positions = get_positions(f)
        for position in positions:
            last.append(position)

    lengths = [utils.norm(utils.subtract(utils.average_position(first),utils.average_position(last))) for first,last in zip(firsts,lasts)]

    return lengths

def average_position(frames):
    values = []
    for frame in frames:
        for hand in frame.hands():
            for finger in hand.fingers():
                values.append(finger.tip().position)
    average_value = utils.average_position(values)
    return [average_value.x,average_value.y,average_value.z]

def average_velocity(frames):
    values = []
    for frame in frames:
        for hand in frame.hands():
            for finger in hand.fingers():
                values.append(finger.velocity())
    average_value = utils.average_position(values)
    return [average_value.x,average_value.y,average_value.z]


def list_3d(size):
    return [[[0 for i in range(size)] for j in range(size)] for k in range(size)]

def velocity_histogram(frames,bins = 4,range=(-1.,1.)):
    length = range[1]-range[0]
    bin_size = length/bins

    def hround(v):
        return min(bins-1,int((v-range[0])/bin_size))

    l = list_3d(bins)
    for frame in frames:
        for hand in frame.hands():
            for finger in hand.fingers():
                v = finger.velocity()
                vector = Leap.Vector(v.x,v.y,v.z)
                x = v.x/utils.norm(vector)
                y = v.y/utils.norm(vector)
                z = v.z/utils.norm(vector)
                l[hround(x)][hround(y)][hround(z)] += 1
    return l

def hand_velocity_histogram(frames,bins = 4,range=(-1.,1.)):
    length = range[1]-range[0]
    bin_size = length/bins

    def hround(v):
        return min(bins-1,int((v-range[0])/bin_size))

    l = list_3d(bins)
    for frame in frames:
        for hand in frame.hands():
            v = hand.velocity()
            if v:
                x = v.x/utils.norm(v)
                y = v.y/utils.norm(v)
                z = v.z/utils.norm(v)
                l[hround(x)][hround(y)][hround(z)] += 1
    return l

def palm_normal_histogram(frames,bins = 4,range=(-1.,1.)):
    length = range[1]-range[0]
    bin_size = length/bins

    def hround(v):
        return min(bins-1,int((v-range[0])/bin_size))

    l = list_3d(bins)
    for frame in frames:
        for hand in frame.hands():
            palm = hand.palm()
            if palm:
                v = palm.direction
                x = v.x/utils.norm(v)
                y = v.y/utils.norm(v)
                z = v.z/utils.norm(v)
                l[hround(x)][hround(y)][hround(z)] += 1
    return l

def position_histogram(frames,bins = 4,range=(-1.,1.)):
    length = range[1]-range[0]
    bin_size = length/bins

    def hround(v):
        return min(bins-1,int((v-range[0])/bin_size))

    l = list_3d(bins)
    positions = []
    for frame in frames:
        for hand in frame.hands():
            for finger in hand.fingers():
                p = finger.tip().position
                positions.append(p)
    average_p = utils.ave_v(positions)
    for index,position in enumerate(positions):
        positions[index] = utils.subtract(position,average_p)
        v = positions[index]
        x = v.x/utils.norm(v)
        y = v.y/utils.norm(v)
        z = v.z/utils.norm(v)
        l[hround(x)][hround(y)][hround(z)] += 1
    return l

def palm_position_histogram(frames,bins = 4,range=(-1.,1.)):
    length = range[1]-range[0]
    bin_size = length/bins

    def hround(v):
        return min(bins-1,int((v-range[0])/bin_size))

    l = list_3d(bins)
    positions = []
    for frame in frames:
        for hand in frame.hands():
            palm = hand.palm()
            if palm:
                p = palm.position
                positions.append(p)
    average_p = utils.ave_v(positions)
    for index,position in enumerate(positions):
        positions[index] = utils.subtract(position,average_p)
        v = positions[index]
        x = v.x/utils.norm(v)
        y = v.y/utils.norm(v)
        z = v.z/utils.norm(v)
        l[hround(x)][hround(y)][hround(z)] += 1
    return l
