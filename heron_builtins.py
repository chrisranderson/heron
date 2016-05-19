
def plot(x):
    import plotly
    from plotly.graph_objs import Scatter

    plotly.offline.plot([
        Scatter({
            'x': x
        })
    ])

def python(x):
    return eval(x)

def initialize_environment(environment):
    environment.add_function(plot)
    environment.add_function(python)
    return environment