#Testing each Mutation Rate just to see wich one is the best one
import Basics
import time
import matplotlib.pyplot as plt
# Constants
target = "HELLOWORLD"
GENES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
GENERATIONS = 100
PopulationMin = 10
PopulationMax = 100
tournament_size=3
POPULATION_SIZE = 50  # Using a moderate population size
TOURNAMENT_SIZE = 3   # Using a moderate tournament size

def evolve_Mutation(mutation_rate):
    start_time = time.time()
    found_solution = False
    
    # Create initial population
    population = [Basics.create_individual(GENES,target) for _ in range(POPULATION_SIZE)]
    
    best_fitness_history = []
    avg_fitness_history = []
    diversity_history = []  # Track population diversity
    
    for generation in range(GENERATIONS):
        # Calculate fitness for current population
        fitnesses = [Basics.calculate_fitness(individual,target) for individual in population]
        
        # Calculate statistics
        best_fitness = max(fitnesses)
        avg_fitness = sum(fitnesses) / len(fitnesses)
        diversity = len(set(population))  # Number of unique individuals
        
        best_fitness_history.append(best_fitness)
        avg_fitness_history.append(avg_fitness)
        diversity_history.append(diversity)
        
        best_individual = population[fitnesses.index(best_fitness)]
        
        if generation % 5 == 0:  # Print every 5th generation
            print(f"Mutation Rate: {mutation_rate:.3f}, Gen {generation}: "
                  f"Best = {best_individual}, Fitness = {best_fitness}/{len(target)}, "
                  f"Avg Fitness = {avg_fitness:.2f}, Diversity = {diversity}")
        
        if best_fitness == len(target):
            end_time = time.time()
            print(f"\nSuccess! Target found in generation {generation}")
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            found_solution = True
            return {
                'generations': generation,
                'time': end_time - start_time,
                'found_solution': True,
                'final_fitness': best_fitness,
                'best_fitness_history': best_fitness_history,
                'avg_fitness_history': avg_fitness_history,
                'diversity_history': diversity_history
            }
        
        # Create new generation
        new_population = []
        for _ in range(POPULATION_SIZE):
            parent1 = Basics.tournament_selection(population, fitnesses)
            parent2 = Basics.tournament_selection(population, fitnesses)
            while parent2 == parent1:
                parent2 = Basics.tournament_selection(population, fitnesses)
            
            child = Basics.crossover(parent1, parent2)
            child = Basics.mutate(GENES,child, mutation_rate)
            new_population.append(child)
        
        population = new_population
    
    end_time = time.time()
    return {
        'generations': GENERATIONS,
        'time': end_time - start_time,
        'found_solution': False,
        'final_fitness': best_fitness,
        'best_fitness_history': best_fitness_history,
        'avg_fitness_history': avg_fitness_history,
        'diversity_history': diversity_history
    }


# Test different mutation rates
mutation_rates = [0.01, 0.05, 0.1, 0.2, 0.3]
results = {}

print("\nTesting different mutation rates")
print("=" * 50)

for rate in mutation_rates:
    print(f"\nTesting mutation rate: {rate}")
    print("-" * 30)
    results[rate] = evolve_Mutation(rate)

# Analyze and display results
print("\nResults Summary:")
print("=" * 70)
print("\nMutation Rate | Generations | Found Solution | Final Fitness | Avg Diversity | Time (s)")
print("-" * 80)

for rate, result in results.items():
    avg_diversity = sum(result['diversity_history']) / len(result['diversity_history'])
    print(f"{rate:^12.3f} | {result['generations']:^10} | "
          f"{str(result['found_solution']):^13} | {result['final_fitness']:^12} | "
          f"{avg_diversity:^13.1f} | {result['time']:^8.2f}")

# Find best mutation rate
best_rate = min(results.items(), key=lambda x: (
    not x[1]['found_solution'],
    x[1]['generations'],
    -sum(x[1]['diversity_history'])/len(x[1]['diversity_history'])  # Higher diversity is better
))

print("\nBest Mutation Rate:")
print("=" * 70)
rate = best_rate[0]
result = best_rate[1]
print(f"Mutation Rate: {rate}")
print(f"Generations needed: {result['generations']}")
print(f"Time taken: {result['time']:.2f} seconds")
print(f"Found solution: {result['found_solution']}")
print(f"Final fitness: {result['final_fitness']}/{len(target)}")
print(f"Average diversity: {sum(result['diversity_history'])/len(result['diversity_history']):.1f}")

# Write on file the best Mutation rate to see wich one is the most optimise  
f = open("./best_Rate.txt", "a")
writted = str(rate)+";"
f.write(writted)
f.close()
