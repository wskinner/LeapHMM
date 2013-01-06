############################################################
# Initialization parameters for N-component HMMs 

import numpy as np
from sklearn import GaussianHMM
from leaphmm import *

debug = True

# The number of states to use
N = 14 
# The number of states which will not be initialized in a left-right
# way
M = 4

def initialize():
    gestures = []
    #################### Gesture Definitions ####################
    ### Right swipe

    # Bias the start state to the leftmost states
    pi = [0.0 for i in xrange(N)]
    pi[0] = 0.7; pi[1] = 0.2; pi[2] = 0.1
    start_prob = np.array(pi)
    if debug:
        print 'Start state probabilities'
        print start_prob

    # Initialize the transition matrix to have the left-right property
    A = [[0.0 for i in xrange(N)] for i in xrange(N)]
    for i in xrange(N-M):
        if i ==  N-1:
            A[i][i] = 1.0
        else:
            A[i][i] = 0.5
            A[i][i+1] = 0.5
    trans_mat = np.array(A)
    if debug:
        print 'Transition Matrix'
        print trans_mat

    gestures.append(GaussianHMM(N, 'full', start_prob, trans_mat), 
                    'rswipe')


    ### Left swipe


    return Recognizer(gestures)

