from lib import Leap
import time
from utils import *

class TempoListener(Leap.Listener):
    def __init__(self,callback, controller):
        super(TempoListener,self).__init__()

        self.average_velocity = Leap.Vector(0,0,0)
        self.angle_history = []
        self.velocity_history = []

        self.changing = False

        self.last_change_time = None
        self.bpm = 0

        self.callback = callback
        self.controller = controller

        #settings
        self.default_alpha = .3 #for the kalman filters
        self.threshold_angle = .7
        self.threshold_speed = .1


    def value(self):
        return self.bpm

    def register_change(self,alpha = None,debug = False):
        if not alpha:
            alpha = self.default_alpha

        if self.last_change_time:
            delta = time.time() - self.last_change_time
            if delta > self.threshold_speed:
                self.bpm = (1-alpha)*self.bpm + alpha*(30/delta)
                self.callback(self.controller, self.bpm)
                if debug:
                    print "BPM:",self.bpm

        self.last_change_time = time.time()

    def update_velocity(self,velocity,alpha = None):
        if not alpha:
            alpha = self.default_alpha

        n = norm(self.average_velocity)*norm(velocity)
        if n>=0.01:
            angle = dot(self.average_velocity,velocity)/(n)
            if angle<self.threshold_angle:
                if not self.changing:
                    self.register_change()
                self.changing = True
            else:
                self.changing = False
            self.angle_history.append(angle)

        self.average_velocity = add(mul(self.average_velocity,(1-alpha)),mul(velocity,alpha))
        self.velocity_history.append(norm(self.average_velocity))

    def onInit(self, controller):
        print "Initialized"
    def onConnect(self, controller):
        print "Connected"
    def onDisconnect(self, controller):
        print "Disconnected"
    def onFrame(self,controller):
        frame = controller.frame()

        hands = frame.hands()
        for hand in hands:
            for finger in hand.fingers():
                if finger.isTool():
                    posistion = finger.tip().position
                    velocity = finger.velocity()

                    self.update_velocity(velocity)

                    return
