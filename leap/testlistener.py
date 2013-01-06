from lib import Leap
from utils import *

class TestListener(Leap.Listener): 

    def __init__(self, callback, controller): 
        super(TestListener, self).__init__()
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
        if numHands > 0:
            hand = hands[0]
            fingers = len(hands[0].fingers())
        else:
            hand = None
            fingers = 0
        #print numHands, 'hands, ', fingers, 'fingers, '

        if numHands > 1:
            palm1 = hands[0].palm()
            if palm1: pos1 = palm1.position
            palm2 = hands[1].palm()
            if palm2: pos2 = palm2.position
            if palm1 and palm2:
                handDist = collapse(subtract(pos1, pos2))
                print 'hand distance', handDist

        if hand and hand.velocity():
            xvel = hand.velocity().x
            yvel = hand.velocity().y
            zvel = hand.velocity().z
            #print 'xVel', xvel, 'yVel', yvel, 'zVel', zvel, 'palm', palmvec


        if numHands > 1: 
            for hand in hands:
                numFingers = len(hand.fingers()) 
                if numFingers > 1:
                    if hand.velocity() != None: 
                        self.previousVelocity = (1-self.alpha)*self.previousVelocity + self.alpha*hand.velocity().z
                    else: 
                        self.previousVelocity = 0
                    if self.shouldAppend(self.previousVelocity): 
                        self.prev_vel.append("")
                        if len(self.prev_vel) > 10:
                            self.prev_vel = []
                            self.callback(self.controller)
                    else: 
                        self.prev_vel = []
                        self.previosVelocity = 0

    def shouldAppend(self, vel): 
        return vel > 200

