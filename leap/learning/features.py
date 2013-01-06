import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir) 

from lib import Leap
import utils

def getVariance(nums):
    if len(nums) == 0:
        return 0
    count = len(nums)
    ev = sum(nums) / count
    variance = sum(map(lambda x: (x-ev)**2, nums)) / count
    return variance
def get_positions(frame):
    hands = frame.hands()
    positions = []
    for hand in hands:
        for finger in hand.fingers():
            positions.append(finger.tip().position)
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
    avg_fingers = (sum([getNumFingers(frame) for frame in frames]) / len(frames))**2
    print avg_fingers
    return avg_fingers, avg_fingers, avg_fingers, avg_fingers

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
