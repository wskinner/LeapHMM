from lib import Leap
import sys 

class StopTrackListener(Leap.Listener): 

    def __init__(self, callback, controller): 
        super(StopTrackListener, self).__init__()
        self.callback = callback 
        self.controller = controller
        
    def onInit(self, controller): 
        self.previousStops = []
        self.alpha = 0.3

    def onFrame(self, controller): 
        frame = controller.frame()
        hands = frame.hands()
        numHands = len(hands)

        if numHands == 1: 
            for hand in hands:
                numFingers = len(hand.fingers())
                if numFingers < 1 and hand.velocity().y > 500:
                    self.previousStops.append("one")
                    if len(self.previousStops) > 20:
                        self.callback(self.controller)
                else: 
                    self.previousStops = []

class LowerVolumeListener(Leap.Listener): 

    def __init__(self, callback, controller): 
        super(LowerVolumeListener, self).__init__()
        self.callback = callback 
        self.controller = controller

    def onInit(self, controller): 
        self.prev_vel = []
        self.alpha = 0.3
        self.previousVelocity = 0

    def onFrame(self, controller): 
        frame = controller.frame()
        hands = frame.hands()
        numHands = len(hands)

        if numHands >= 1: 
            for hand in hands:
                numFingers = len(hand.fingers()) 
                if numFingers > 1:
                    if hand.velocity() != None: 
                        self.previousVelocity = (1-self.alpha)*self.previousVelocity + self.alpha*hand.velocity().y
                    else: 
                        self.previousVelocity = 0
                    if self.shouldAppend(self.previousVelocity): 
                        self.prev_vel.append("")
                        if len(self.prev_vel) > 25:
                            self.callback(self.controller)
                    else: 
                        self.prev_vel = []
                        self.previosVelocity = 0

    def shouldAppend(self, vel): 
        return vel > 200

class RaiseVolumeListener(LowerVolumeListener): 

    def shouldAppend(self, vel): 
        return vel < -200


from utils import *

class StartTrackListener(Leap.Listener): 

    def __init__(self, callback, controller): 
        super(StartTrackListener, self).__init__()
        self.callback = callback 
        self.controller = controller

    def onInit(self, controller): 
        self.history = [0]
        self.alpha = 0.3
        self.theta = 2500
        self.threshold = 15
        self.previousCloseness = 0

    def onFrame(self, controller): 
        frame = controller.frame()
        hands = frame.hands()
        numHands = len(hands)

        if numHands > 1:
            palm1 = hands[0].palm()
            if palm1: 
                pos1 = palm1.position
            palm2 = hands[1].palm()
            if palm2: 
                pos2 = palm2.position
            if palm1 and palm2:
                closeness = collapse(subtract(pos1, pos2))
                k_closeness = (1-self.alpha)*closeness + self.alpha*self.history[-1]
                #print k_closeness, len(self.history)
                if k_closeness > self.theta:
                    self.history.append(k_closeness)
                    if len(self.history) > self.threshold:
                        self.callback(self.controller)
                        self.history = [0]
                else:
                    self.history = [0]
            else:
                self.history = [0]
        else:
            self.history = [0]

    def shouldAppend(self, vel): 
        return vel > 200

