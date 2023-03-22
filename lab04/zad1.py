import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import numpy as np
import math
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt

options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}

def endurance(arr):
    return -(math.exp(-2*(arr[1]-math.sin(arr[0]))**2)+math.sin(arr[2]*arr[3])+math.cos(arr[4]*arr[5]))

def f(x):
    n_particles = x.shape[0]
    f = np.zeros(n_particles)
    for i in range(n_particles):
        f[i] = endurance(x[i])
    return f

x_max = np.ones(6)
x_min = np.zeros(6)
my_bounds = (x_min, x_max)

bounds=my_bounds

optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6, options=options, bounds=bounds)
optimizer.optimize(f, iters=1000)

cost_history = optimizer.cost_history

plot_cost_history(cost_history)
plt.show()
