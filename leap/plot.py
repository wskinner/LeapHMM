import matplotlib.pyplot as plt

def plotModel(model, X):
    # Plot the sampled data
    plt.plot(X[:, 0], X[:, 1], "-o", label="observations", ms=6,
            mfc="orange", alpha=0.7)

    # Indicate the component numbers
    for i, m in enumerate(model.means_):
        plt.text(m[0], m[1], 'Component %i' % (i + 1),
                size=17, horizontalalignment='center',
                bbox=dict(alpha=.7, facecolor='w'))
    plt.legend(loc='best')
    plt.show()
