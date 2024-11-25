import random

# Constants
target = "HELLO"
GENES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
POPULATION_SIZE = 50
GENERATIONS = 100

def create_individual():
    return ''.join(random.choice(GENES) for _ in range(len(target)))

def calculate_fitness(individual):
    return sum(1 for i, j in zip(individual, target) if i == j)

def tournament_selection(population, fitnesses, tournament_size=3):
    tournament_indices = random.sample(range(len(population)), tournament_size)
    tournament_fitnesses = [fitnesses[i] for i in tournament_indices]
    winner_index = tournament_indices[tournament_fitnesses.index(max(tournament_fitnesses))]
    return population[winner_index]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1)-1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(individual, mutation_rate=0.1):
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.choice(GENES)
    return ''.join(individual)

def evolve():
    # Create initial population
    population = [create_individual() for _ in range(POPULATION_SIZE)]
    
    for generation in range(GENERATIONS):
        # Calculate fitness for current population
        fitnesses = [calculate_fitness(individual) for individual in population]
        
        # Find best individual in current generation
        best_fitness = max(fitnesses)
        best_individual = population[fitnesses.index(best_fitness)]
        print(f"Generation {generation}: Best Individual = {best_individual}, Fitness = {best_fitness}/{len(target)}")
        
        # Check if we've found the target
        if best_fitness == len(target):
            print(f"Target found in generation {generation}!")
            return
        
        # Create new generation
        new_population = []
        for _ in range(POPULATION_SIZE):
            # Select parents
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            while parent2 == parent1:
                parent2 = tournament_selection(population, fitnesses)
            
            # Create and mutate child
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        
        # Replace old population with new population
        population = new_population
    
    print("Maximum generations reached without finding target.")

# Run the algorithm
evolve()