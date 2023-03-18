import numpy as np
import pygad
import math
import matplotlib.pyplot as plt

num_genes = 6
gene_space = [{"low": 0, "high": 1}] * num_genes
num_solutions = 50
keep_parents = 2
initial_population = np.random.rand(num_solutions, num_genes)
mutation_type = "random"
num_parents_mating = 4

# fitness function
def fitness(solution, solution_idx):
    x, y, z, u, v, w = solution
    result = math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w)
    return result

# pygad
ga_instance = pygad.GA(initial_population=initial_population, 
                       fitness_func=fitness, 
                       gene_space=gene_space,
                       num_generations=50,
                       mutation_percent_genes=1,
                       num_parents_mating=num_parents_mating, 
                       mutation_num_genes=2,
                       keep_parents=keep_parents,
                       mutation_type=mutation_type,
                       sol_per_pop=50,
                       init_range_low=0,
                       init_range_high=1
                       )
ga_instance.run()

best_solution = ga_instance.best_solution()
best_solution_fitness = best_solution[1]
best_solution = best_solution[0]

print("Best solution:", best_solution)
print("Best solution fitness:", best_solution_fitness)

plt.plot(ga_instance.best_solutions_fitness)
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.title("Best Fitness per Generation")
plt.show()
