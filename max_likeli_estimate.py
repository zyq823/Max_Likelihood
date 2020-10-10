import numpy as np

        
# the following code is for Question (a.ii)

def parse_dataset(filename):
    data_file = open(filename, 'r')  # Open File "to read"
    dataset = []  # List to hold Datapoint objects

    for index, line in enumerate(data_file):
        dataset.append(float(line.strip()))  # strip() removes '\n', and split(',') splits the line at tabs

    return dataset

data_set = parse_dataset('Q1_Data.csv')

def compMean(dataset):
    sum = 0
    for y in dataset:
        sum += y
    return sum / len(dataset)

dataMean = compMean(data_set)

def compVar(dataset, mean):
    var = 0
    for y in dataset:
        var += (y - mean)**2
    print(var / len(dataset))
    return var / len(dataset)

compVar(data_set, dataMean)

# the following code is for Question (b)