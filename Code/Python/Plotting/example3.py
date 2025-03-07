import numpy as np
import matplotlib.pyplot as plt 

def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

# which you would then use as:

if __name__ == '__main__':
    data1, data2 = np.random.randn(2, 100)
    fig, ax = plt.subplots(1, 1)
    my_plotter(ax, data1, data2, {'marker': 'x'})

    plt.show()

