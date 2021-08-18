import numpy as np
from matplotlib import pyplot as plt

def lr_dataset_generator(slope, n, std_dev):
    x = abs(np.random.randn(n)*100)
    e = np.random.randn(n)*std_dev
    y = x*slope+e
    return x, y
    
    
def lr_dataset():
    x, y = lr_dataset_generator(10, 100, 150)
    x_train = x[:80]
    y_train = y[:80]

    x_test = x[80:]
    y_test = y[80:]
    
    return x_train, y_train, x_test, y_test