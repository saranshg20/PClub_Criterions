import numpy as np
from matplotlib import pyplot as plt

def lr_dataset_generator(slope, n, std_dev):
    x = abs(np.random.randn(n)*100)
    e = np.random.randn(n)*std_dev
    y = x*slope+e
    return x, y
    
    
def lr_dataset():
    x, y = lr_dataset_generator(10, 40000, 300)
    x_train = x[:int(0.8*len(x))]
    y_train = y[:int(0.8*len(x))]

    x_test = x[int(0.8*len(x)):]
    y_test = y[int(0.8*len(x)):]
    
    return x_train, y_train, x_test, y_test
