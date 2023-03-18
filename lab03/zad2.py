import pygad
import random
import numpy as np

maze = np.array([
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
[1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
[1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
[1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
[1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
[1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
[1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

# 0 - dół, 1 - góra, 2 - prawo, 3 - lewo
gene_space = [0, 1, 2, 3]
chromosome_length = 100

start = (1, 1)
exit = (10, 10)
max_steps = 30

def create_population(population_size, chromosome_length, gene_space):
    population = []
    for i in range(population_size):
        chromosome = []
        for j in range(chromosome_length):
            gene = random.choice(gene_space)
            chromosome.append(gene)
        population.append(chromosome)
    return population

initial_population = create_population(200, chromosome_length, gene_space)

import numpy as np

def fitness(solution, solution_idx):
    x, y = 1, 1
    maze_copy = np.pad(maze, (1, 1), mode='constant', constant_values=True)
    fitness_score = 0
    visited = np.zeros_like(maze, dtype=bool)

    for gene in solution:
        if gene == 0:  # idź w dół
            if maze_copy[x+1, y] != 1:
                x += 1
        elif gene == 1:  # idź w górę
            if maze_copy[x-1, y] != 1:
                x -= 1
        elif gene == 2:  # idź w prawo
            if maze_copy[x, y+1] != 1:
                y += 1
        elif gene == 3:  # idź w lewo
            if maze_copy[x, y-1] != 1:
                y -= 1

        # Sprawdzenie, czy nie odwiedzamy już tego samego pola
        if visited[x-1, y-1]:
            fitness_score -= 1
        else:
            visited[x-1, y-1] = True
            fitness_score += 20

        # Sprawdzenie, czy osiągnęliśmy cel
        if x == 10 and y == 10:
            fitness_score += 500
            break

        # Zaznaczenie, że odwiedziliśmy aktualne pole
        maze_copy[x, y] = True

        # Odejmowanie od fitness_score w zależności od odległości od celu
        fitness_score -= abs(maze.shape[0]-x) + abs(maze.shape[1]-y)

    return fitness_score

keep_parents = 50

# Tworzenie instancji klasy pygad.GA
ga_instance = pygad.GA(
    num_generations=1000,
    num_parents_mating=100,
    initial_population=initial_population,
    gene_space=gene_space,
    mutation_num_genes=8, 
    mutation_percent_genes=10,
    keep_parents=keep_parents,
    mutation_type="random",
    sol_per_pop=500, 
    fitness_func=fitness
    )

ga_instance.run()

best_solution = ga_instance.best_solution()
best_solution_fitness = best_solution[1]
best_solution = best_solution[0]

print("Best solution:", best_solution)
print("Best solution fitness:", best_solution_fitness)

