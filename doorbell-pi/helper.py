import time
import datetime
import numpy as np


def get_timestamp():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d__%H_%M_%S')


def average(values):
    return np.mean(values)


def signal_detected(values, threshold=0.9):
    return average(values) < threshold
