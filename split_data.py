def parse(name, ratio=1):
    """
    Given the name of a csv file containing collected data,
    split the data into a training set and a held-out set
    for testing with a ratio of 1 test set per ratio training
    sets.
    """
    with open(name+'.csv', 'r') as f:
        with open(name+'_train.csv', 'w') as g:
            with open(name+'_test.csv', 'w') as h:
                for line in f:
                    l_num = int(line.split(',')[0])
                    if l_num % (ratio+1) == 0:
                        g.write(str(l_num/2) + ',' + ','.join(line.split(',')[1:]))
                    else:
                        h.write(str(l_num/2) + ',' + ','.join(line.split(',')[1:]))

if __name__ == '__main__':
    import sys
    parse(sys.argv[1])
