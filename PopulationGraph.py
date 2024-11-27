#Testing each Population just to see wich one is the best one

import Basics
import time
import matplotlib.pyplot as plt
# Constants
target = "HELLOWORLORLD"
GENES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
GENERATIONS = 100
PopulationMin = 10
PopulationMax = 100
tournament_size=3
mutation_rate=0.1

def evolvePop(population_size):
    start_time = time.time()
    found_solution = False

    # Create initial population
    population = [Basics.create_individual(GENES,target) for _ in range(population_size)]

    generations_needed = 0
    for generation in range(GENERATIONS):
        # Calculate fitness for current population
        fitnesses = [Basics.calculate_fitness(individual,target) for individual in population]

        # Find best individual in current generation
        best_fitness = max(fitnesses)
        best_individual = population[fitnesses.index(best_fitness)]
        #print(f"Generation {generation}: Best Individual = {best_individual}, Fitness = {best_fitness}/{len(target)}")

        # Check if we've found the target
        if best_fitness == len(target):
            end_time = time.time()
            print(f"\nSuccess! Target found in generation {generation}")
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            found_solution = True
            generations_needed = generation
            break

        # Create new generation
        new_population = []
        for _ in range(population_size):
            # Select parents
            parent1 = Basics.tournament_selection(population, fitnesses,tournament_size)
            parent2 = Basics.tournament_selection(population, fitnesses,tournament_size)
            while parent2 == parent1:
                parent2 = Basics.tournament_selection(population, fitnesses,tournament_size)

            # Create and mutate child
            child = Basics.crossover(parent1, parent2)
            child = Basics.mutate(GENES,child,mutation_rate)
            new_population.append(child)

        population = new_population

    if not found_solution:
        end_time = time.time()
        print(f"\nFailed to find solution in {GENERATIONS} generations")
        print(f"Time taken: {end_time - start_time:.2f} seconds")
        generations_needed = GENERATIONS
    return generations_needed

# test for population sizes
population_sizes = []
number = 10
for number in range(PopulationMin,PopulationMax,1):
    population_sizes.append(number)

print(population_sizes)

results = {}
for size in population_sizes:
    print(f"\nTesting population size: {size}")
    print("=" * 50)
    generations_needed = evolvePop(size)
    results[size] = generations_needed
    print("-" * 50)

# Visualization
plt.figure(figsize=(8, 6))
plt.plot(population_sizes, [results[size] for size in population_sizes], marker='o')
plt.xlabel('Population Size')
plt.ylabel('Generations Needed')
plt.title('Population Size vs. Generations')
plt.grid()
plt.show()


