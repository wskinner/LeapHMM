from lib import Leap
import sys 
import learn
from features import getVariance, fingerVariance
from time import time

class LearnedListener(Leap.Listener): 

    def __init__(self, callback, controller): 
        super(LearnedListener, self).__init__()
        self.callback = callback 
        self.controller = controller
        
    def onInit(self, controller): 
        self.max_length = 500
        self.learner = learn.GestureLearner()
        self.learner.load_data()
        self.learner.learn()
        self.window = []
        self.total_frames = 0
        self.freq = 60
        self.max_confidence = 0.5
        self.last_update = time()

        self.delay = 2
        self.timeout = 0


    def onFrame(self, controller):
        if self.timeout > 0:
            self.timeout -= 1
            return
        if self.locked():
            self.window = []
            return
        self.total_frames += 1
        self.window.append(controller.frame())
        if len(self.window) > self.max_length:
            self.window.pop(0)
        
        if self.total_frames % self.freq == 0 and not self.emptyFrames(self.window):
            self.emptyFrames(self.window)
            prediction = self.learner.predict(self.window)
            self.callback(self.controller, prediction)
            self.window = []
            self.resetCountdown()

    def resetCountdown(self, wait=100):
        self.timeout = wait

    def emptyFrames(self, frames):
        variance = fingerVariance(frames)
        maxvar = max(variance)
        return maxvar < 300

    def locked(self):
        return time() - self.last_update < self.delay

    def lock(self):
        self.last_update = time()

