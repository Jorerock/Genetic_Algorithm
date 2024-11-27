
import random

def create_individual(GENES,target):
    return ''.join(random.choice(GENES) for _ in range(len(target)))

def calculate_fitness(individual,target):
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

def mutate(GENES,individual, mutation_rate=0.1):
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.choice(GENES)
    return ''.join(individual)
