
def plot(x):
    import plotly
    from plotly.graph_objs import Scatter

    plotly.offline.plot([
        Scatter({
            'x': x
        })
    ])

def initialize_environment(environment):
    environment.add_function(plot)