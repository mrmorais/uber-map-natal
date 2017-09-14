# coding=utf-8
import pandas as pd
import numpy as np
from config.neighborhoods import Neighborhoods

dataFrame = pd.read_csv('data/uber_map.csv')

for nbhood in Neighborhoods:
    estimates_sum = 0
    num_requests = 0
    for request in dataFrame[nbhood['name']]:
        if (not np.isnan(request)):
            estimates_sum = estimates_sum + request
            num_requests = num_requests + 1
    avg = 0
    if (num_requests > 0):
        avg = estimates_sum / num_requests
    print nbhood['name'],":",avg