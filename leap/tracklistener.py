from lib import Leap
from utils import *

class TrackUpListener(Leap.Listener): 
    """
    A two hand right swipe
    """

    def __init__(self, callback, controller): 
        super(TrackUpListener, self).__init__()
        self.callback = callback 
        self.controller = controller

    def onInit(self, controller): 
        self.history = [(0,0)]
        self.alpha = 0.3
        self.threshold = 10

    def onFrame(self, controller): 
        frame = controller.frame()
        hands = frame.hands()
        numHands = len(hands)

        if numHands > 1:
            hand1 = hands[0]
            hand2= hands[1]
            palm1 = hand1.palm()
            if palm1: 
                pos1 = palm1.position

            palm2 = hand2.palm()
            if palm2: 
                pos2 = palm2.position
            if palm1 and palm2:
                v1, v2 = self.kalmanFilter((hand1.velocity().x, hand2.velocity().x))
                #print '2 hands'
                #print 'velocity', v1, v2
                if self.shouldAppend(v1) and self.shouldAppend(v2):
                    self.history.append((v1, v2))
                    if len(self.history) > self.threshold:
                        self.callback(self.controller)
                        self.history = [(0,0)]
                else:
                    self.history = [(0,0)]
            else:
                self.history = [(0,0)]
    
    def kalmanFilter(self, velocities):
        v1 = (1-self.alpha)*self.history[-1][0] + self.alpha*velocities[0]
        v2 = (1-self.alpha)*self.history[-1][1] + self.alpha*velocities[1]
        return v1, v2

    def shouldAppend(self, vel): 
        return vel < 200

from lib import Leap
from utils import *

class TrackDownListener(Leap.Listener): 
    """
    A two hand right swipe
    """

    def __init__(self, callback, controller): 
        super(TrackDownListener, self).__init__()
        self.callback = callback 
        self.controller = controller

    def onInit(self, controller): 
        self.history = [(0,0)]
        self.alpha = 0.3
        self.threshold = 8

    def onFrame(self, controller): 
        frame = controller.frame()
        hands = frame.hands()
        numHands = len(hands)

        if numHands > 1:
            hand1 = hands[0]
            hand2= hands[1]
            palm1 = hand1.palm()
            if palm1: 
                pos1 = palm1.position

            palm2 = hand2.palm()
            if palm2: 
                pos2 = palm2.position
            if palm1 and palm2:
                v1, v2 = self.kalmanFilter((hand1.velocity().x, hand2.velocity().x))
                #print '2 hands'
                #print 'velocity', v1, v2
                if self.shouldAppend(v1) and self.shouldAppend(v2):
                    self.history.append((v1, v2))
                    if len(self.history) > self.threshold:
                        self.callback(self.controller)
                        self.history = [(0,0)]
                else:
                    self.history = [(0,0)]
            else:
                self.history = [(0,0)]
    
    def kalmanFilter(self, velocities):
        v1 = (1-self.alpha)*self.history[-1][0] + self.alpha*velocities[0]
        v2 = (1-self.alpha)*self.history[-1][1] + self.alpha*velocities[1]
        return v1, v2

    def shouldAppend(self, vel): 
        #print vel, len(self.history)
        return vel > 400

