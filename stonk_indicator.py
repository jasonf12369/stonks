import json
import time as time_true
import pathlib
import pandas as pd
import numpy as np
from config import *
from td.client import TDClient
from td.utils import TDUtilities

class Trend0():
    def __init__(self, name, period, exponent, prices):
        self.Name = name
        self.period = period
        self.exponent = exponent

        self.Value = 0
        self.prices = prices

    def calc_trend(self):
        changes = np.array([])
        for i in range(len(self.prices) - 1):
            _return = (self.prices[i + 1] - self.prices[i] / self.prices[i])
            changes = np.append(changes, _return)
        return self.power_weighted_moving_average(changes)
    
    def power_weighted_moving_average(self, changes):
        return self.weighted_average(changes, self.exponential_weights(len(changes)))

    def exponential_weights(self, length):
        weights = np.array([])
        for i in range(length):
            w = i + 1
            weights = np.append(weights, w**self.exponent)
        return weights
    
    def weighted_average(self, changes, weights):
        products = []
        for i in range(len(changes)):
            products.append(changes[i] * weights[i])
        return sum(products) / sum(weights)