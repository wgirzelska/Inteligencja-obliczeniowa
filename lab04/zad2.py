import matplotlib.pyplot as plt
import random
from aco import AntColony
import time

COORDS = (
    (20, 52),
    (43, 50),
    (20, 84),
    (70, 65),
    (29, 90),
    (87, 83),
    (73, 23),
    (45, 69),
    (82, 92)
)

COORDS2 = (
    (20, 52),
    (43, 50),
    (20, 84),
    (70, 65),
    (29, 90),
    (87, 83),
    (73, 23)
)

plt.style.use("dark_background")

def plot_nodes(w=12, h=8):
    for x, y in COORDS:
        plt.plot(x, y, "g.", markersize=15)
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])

def plot_all_edges():
    paths = ((a, b) for a in COORDS for b in COORDS)

    for a, b in paths:
        plt.plot((a[0], b[0]), (a[1], b[1]))


plot_nodes()

start_time = time.time()

colony = AntColony(COORDS, ant_count=400, alpha=0.8, beta=1.0, 
                    pheromone_evaporation_rate=0.50, pheromone_constant=1000.0,
                    iterations=400)

optimal_nodes = colony.get_path()

elapsed_time = time.time() - start_time
print(f"Elapsed time: {elapsed_time:.5f} seconds")

for i in range(len(optimal_nodes) - 1):
    plt.plot(
        (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
        (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
    )

plt.show()