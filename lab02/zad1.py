import pygad
import numpy

#definicja listy przedmiotów
items = [["zegar", 100, 7],
["obraz-pejzaz", 300, 7],
["obraz-portret", 200, 6],
["radio", 40, 2],
["laptop", 500, 5],
["lampka nocna", 70, 6],
["srebrne sztućce", 100, 1],
["porcelana", 250, 3],
["figurka z brązu", 300, 10],
["skórzana torebka", 280, 3],
["odkurzacz", 300, 15]]

#definiujemy funkcję fitness
def fitness_func(solution, solution_idx):
    value = 0 #wartosc przedmiotow
    weight = 0 #waga przedmiotow
    for i in range(len(solution)):
        if solution[i] == 1: #jesli przedmiot i jest w plecaku
            value += items[i][1] #zwieksz wartosc
            weight += items[i][2] #zwieksz wage
        if weight > 25: #jesli waga jest wieksza niz 25kg, wartosc ujemna
            fitness = -1
        else:
            fitness = value #w przeciwnym wypadku zwroc wartosc jako fitness
        return fitness

fitness_function = fitness_func

#definiujemy parametry chromosomu
#geny to liczby: 0 lub 1
gene_space = [0, 1]

#ile chromsomów w populacji
#ile genow ma chromosom
sol_per_pop = 10
num_genes = len(items)

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 5
num_generations = 30
keep_parents = 2

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 8

#inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
ga_instance = pygad.GA(gene_space=gene_space,
num_generations=num_generations,
num_parents_mating=num_parents_mating,
fitness_func=fitness_function,
sol_per_pop=sol_per_pop,
num_genes=num_genes,
parent_selection_type=parent_selection_type,
keep_parents=keep_parents,
crossover_type=crossover_type,
mutation_type=mutation_type,
mutation_percent_genes=mutation_percent_genes)

#uruchomienie algorytmu
ga_instance.run()

#podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

#wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()