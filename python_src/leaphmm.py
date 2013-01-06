import numpy as np
import csv
from sklearn.hmm import GaussianHMM
import matplotlib.pyplot as plt

from leaphmm import *
from training import train
from features import loadFeaturesCSV as loadFeatures

debug = True


class Gesture:
    """
    Matches one type of gesture, and provides methods to gain information
    about the current status of the gesture. I.e. has it been matched, 
    if so what is the confidence level, and so on.
    """

    def __init__(self, hmm, name, **kwargs):
        self.model = hmm
        self.name = name

    def matched(self):
        """
        Return a 2-tuple of (boolean, confidence)
        """
        pass

    def confidence(self):
        """
        What is the probability of the current best-guess sequence?
        """
        pass

    def update(self, observation):
        """
        Update the model with a new observation. This should be a vector of 
        features, for example the 3D coordinates of the hand being tracked.
        """
        pass

    def train(self):
        if debug:
            print 'Training %s' % self.name
        self.model.fit(getObservations(self.name), params='mc', init_params='')


class Recognizer:
    """
    Matches any number of gestures, which are internally represented as
    Gestures. At every new observation, the Recognizer passes the
    observation to each Gesture and, and then checks to see if any gesture
    has been successfully observed with a high enough level of confidence.
    """

    def __init__(self, gestures, threshold=0.75, **kwargs):
        self.gestures = gestures
        self.threshold = threshold

    def observe(self, feature_v):
        """
        Update all the Gestures with the new observation.
        """
        for g in self.gestures:
            g.update(feature_v)

    def predict(self):
        """
        Return either a 2-tuple of (gesture, confidence) if the
        confidence threshold has been reached, or None.
        """
        best = max([(g.name, g.confidence()) for g in self.gestures],
                key=lambda x: x[1])
        return best

    def train(self):
        for gesture in self.gestures:
            gesture.train()


############################################################
# Initialization parameters for N-component HMMs 

# The number of states to use
N = 8
# The number of states which will not be initialized in a left-right
# way
M = 4

def initializeRight():
    gestures = []
    #################### Gesture Definitions ####################
    ### Right swipe

    # Bias the start state to the leftmost states
    pi = [0.0 for i in xrange(N)]
    pi[0] = 0.6; pi[1] = 0.2; pi[2] = 0.1;
    for i in xrange(3, N):
        pi[i] = 0.1/(N-3)
    start_prob = np.array(pi)
    if debug:
        print 'Start state probabilities'
        print start_prob
        print ''

    # Initialize the transition matrix to have the left-right property
    A = [[0.0 for i in xrange(N)] for i in xrange(N)]
    for i in xrange(N):
        if i ==  N-1:
            A[i][i] = 1.0
        else:
            A[i][i] = 0.5
            A[i][i+1] = 0.5
    for i in xrange(N, N):
        for j in xrange(N):
            A[i][j] = 1.0/N
    trans_mat = np.array(A)
    for row in trans_mat:
        if sum(row) != 1.0:
            raise ValueError('Row %s of transistion matrix does not sum to 1.0' % row)
    if debug:
        print 'Transition Matrix'
        print trans_mat

    # Means
    means = getMeans('rswipe')
    if debug:
        print 'Means'
        print means

    # Covariances
    covars = .5 * np.tile(np.identity(2), (N, 1, 1))
    if debug:
        print 'Covariances'
        print covars

    # Model
    model = GaussianHMM(N, 'full', start_prob, trans_mat)
    model._set_means(means)
    model._set_covars(covars)

    # gestures.append(Gesture(GaussianHMM(N, 'full'), 'rswipe'))
    return Gesture(model, 'rswipe')

def initializeLeft():
    gestures = []
    #################### Gesture Definitions ####################
    ### Right swipe

    # Bias the start state to the leftmost states
    pi = [0.0 for i in xrange(N)]
    pi[0] = 0.6; pi[1] = 0.2; pi[2] = 0.1;
    for i in xrange(3, N):
        pi[i] = 0.1/(N-3)
    start_prob = np.array(pi)
    if debug:
        print 'Start state probabilities'
        print start_prob
        print ''

    # Initialize the transition matrix to have the left-right property
    A = [[0.0 for i in xrange(N)] for i in xrange(N)]
    for i in xrange(N):
        if i ==  N-1:
            A[i][i] = 1.0
        else:
            A[i][i] = 0.5
            A[i][i+1] = 0.5
    for i in xrange(N, N):
        for j in xrange(N):
            A[i][j] = 1.0/N
    trans_mat = np.array(A)
    for row in trans_mat:
        if sum(row) != 1.0:
            raise ValueError('Row %s of transistion matrix does not sum to 1.0' % row)
    if debug:
        print 'Transition Matrix'
        print trans_mat

    # Means
    means = getMeans('lswipe')
    if debug:
        print 'Means'
        print means

    # Covariances
    covars = .5 * np.tile(np.identity(2), (N, 1, 1))
    if debug:
        print 'Covariances'
        print covars

    # Model
    model = GaussianHMM(N, 'full', start_prob, trans_mat)
    model._set_means(means)
    model._set_covars(covars)

    # gestures.append(Gesture(GaussianHMM(N, 'full'), 'rswipe'))

    return Gesture(model, 'lswipe')

def getMeans(gesture_name):
    samples = getObservations(gesture_name)
    means = [(0.0, 0.0) for i in xrange(N)]
    for i,s in enumerate(samples):
        stride = len(s)/(N)
        index = 0
        for j in xrange(N):
            means[j] += s[index]
            index += stride
    means = np.array(map(lambda x: (x[0]/len(samples), x[1]/len(samples)), means))
    return means

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
                current_obs.append(np.array(map(float,line[1:])))
    return observations


    
######################################################
# Training data looks like:
# 
# 1, p1, p2, p3, ...
# 2, p1, p2, p3, ...
#    .
#    .
#    .

if __name__ == '__main__':
    gestures = []
    gestures.append(initializeLeft())
    gestures.append(initializeRight())
    recognizer = Recognizer(gestures)
    recognizer.train()
    print recognizer.gestures[0].model.transmat_

    if debug:
        print loadFeatures('rswipe')

    print 'right'
    print 'THESE SHOULD END AT 7'
    for obs in loadFeatures('rswipe'):
        print recognizer.gestures[1].model.predict(obs)
    print 'THESE SHOULD BREAK'
    for obs in loadFeatures('lswipe'):
        print recognizer.gestures[1].model.predict(obs)
        
    print 'left'
    print 'THESE SHOULD END AT 7'
    for obs in loadFeatures('lswipe'):
        print recognizer.gestures[0].model.predict(obs)
    print 'THESE SHOULD BREAK'
    for obs in loadFeatures('rswipe'):
        print recognizer.gestures[0].model.predict(obs)

    means = recognizer.gestures[0].model._means_      
    X, Z = recognizer.gestures[0].model.sample(500)

    # Plot the sampled data
    plt.plot(X[:, 0], X[:, 1], "-o", label="observations", ms=6,
            mfc="orange", alpha=0.7)

    # Indicate the component numbers
    for i, m in enumerate(means):
        plt.text(m[0], m[1], 'Component %i' % (i + 1),
                size=17, horizontalalignment='center',
                bbox=dict(alpha=.7, facecolor='w'))
    plt.legend(loc='best')
    plt.show()
    

