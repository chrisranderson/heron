from __future__ import division
import numpy as np
import scipy.stats

def plot(x):
    import plotly
    from plotly.graph_objs import Scatter

    plotly.offline.plot([
        Scatter({
            'x': x
        })
    ])

# distributions
def uniform_continuous(start, end, x=None):
    if x is None:
        return np.random.uniform(start, end)
    else:
        return 1 / (end - start) if (x <= end and x >= start) else 0

def normal(mean, variance, x=None):
    if x is None:
        return np.random.normal(mean, variance)
    else:
        return scipy.stats.norm(mean, variance).pdf(x)

def python(x):
    return eval(x)

def initialize_environment(environment):
    environment.add_function(plot)
    environment.add_function(uniform_continuous)
    environment.add_function(normal)
    environment.add_function(python)
    return environment