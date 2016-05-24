from __future__ import division
import numpy as np
import scipy.stats
from math import *

def plot(x, title=''):

    print('Importing plot library...')
    import plotly.offline as plotter
    from plotly.graph_objs import Histogram, Scatter

    print('Generating plot...')
    plotter.plot([
        Histogram({
            'x': x
        })
    ])

# distributions
def uniform_continuous(start, end, x=None):
    if x is None:
        return np.random.uniform(start, end)
    else:
        if x < start or x > end:
            return 0.000000000000000001 # todo
        else:
            return 1 / (end - start)

sqrt2pi = sqrt(2*pi)
def normal(mean, variance, x=None):
    if x is None:
        return np.random.normal(mean, variance)
    else:
        # return scipy.stats.norm(mean, variance).pdf(x)
        return (1/(sqrt(variance) * sqrt2pi))*exp(-((x-mean)**2)/(2*variance))
def python(x):
    return eval(x)

def initialize_environment(environment):
    environment.add_function(plot)
    environment.add_function(uniform_continuous)
    environment.add_function(normal)
    environment.add_function(python)
    return environment