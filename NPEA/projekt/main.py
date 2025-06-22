import numpy as np
import random
import re


def load_data(path):
    """
     Load data from a file:
    The first line contains the maximum knapsack capacity,
    possibly with a prefix (e.g., "capacity: 6404180").
    Each subsequent line contains two integers: item weight and item value,
    separated by a comma or whitespace.

    Returns:
        w_max (int)           - maximum capacity of the knapsack,
        weights (np.ndarray)  - array of item weights,
        values (np.ndarray)   - array of item values.
    """
    weights = []
    values = []
    with open(path, 'r') as f:
        first = f.readline().strip()
        match = re.search(r"\d+", first)
        if not match:
            raise ValueError(f"Unable to parse max capacity from: {first}")
        w_max = int(match.group())
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = re.split(r"[,\s]+", line)
            if len(parts) < 2:
                continue
            try:
                w = int(parts[0]); v = int(parts[1])
            except ValueError:
                continue
            weights.append(w)
            values.append(v)
    return w_max, np.array(weights), np.array(values)


def fitness(chromosome, weights, values, w_max):
    """
    Fitness function:
    Compute total weight and total value of the chromosome;
    if total weight exceeds w_max, return 0.
    """
    total_w = np.dot(chromosome, weights)
    total_v = np.dot(chromosome, values)
    return total_v if total_w <= w_max else 0


def tournament_selection(population, fitnesses, k=3):
    """
    Tournament selection for parents:
    Randomly pick k individuals and select the one with highest fitness.
    Repeat until the new parent pool has the same size as the population.
    """
    selected = []
    pop_size = len(population)
    for _ in range(pop_size):
        contenders = random.sample(range(pop_size), k)
        best = max(contenders, key=lambda i: fitnesses[i])
        selected.append(population[best].copy())
    return selected


def one_point_crossover(p1, p2):
    point = random.randrange(1, len(p1))
    c1 = np.concatenate([p1[:point], p2[point:]])
    c2 = np.concatenate([p2[:point], p1[point:]])
    return c1, c2


def two_point_crossover(p1, p2):
    n = len(p1)
    i, j = sorted(random.sample(range(1, n), 2))
    c1 = np.concatenate([p1[:i], p2[i:j], p1[j:]])
    c2 = np.concatenate([p2[:i], p1[i:j], p2[j:]])
    return c1, c2


def mutate(chromosome, pm):
    """ Mutation operator (bit flip):
    For each gene, with probability pm flip 0 -> 1 or 1 -> 0."""
    for idx in range(len(chromosome)):
        if random.random() < pm:
            chromosome[idx] = 1 - chromosome[idx]
    return chromosome


# Генетический алгоритм
"""
    Run the genetic algorithm for the 0/1 knapsack problem.

    Parameters:
        weights, values (np.ndarray): item weights and values
        w_max (int): knapsack capacity
        pop_size (int): population size
        generations (int): number of generations to evolve
        cx_prob (float): probability of crossover
        mut_prob (float): probability of mutation per gene
        tour_k (int): tournament size for selection
        crossover_type (str): 'one_point' or 'two_point'

    Returns:
        best_chrom (np.ndarray): best solution found (binary vector)
        best_fit (int): fitness (total value) of best solution
        history (dict): record of best and average fitness per generation
    """
def run_ga(weights, values, w_max,
           pop_size=50, generations=20,
           cx_prob=0.8, mut_prob=0.02,
           tour_k=3, crossover_type='one_point'):

    # Initialize population
    population = [np.random.randint(0, 2, size=len(weights)) for _ in range(pop_size)]
    best_chrom, best_fit = None, 0 #лучшая найденная хромосома и ее фитнес
    history = {'best': [], 'avg': []} # словарь с историей лучшего и среднего фитнеса по поколениям

    for gen in range(generations):
        print(f"\n=== Generation {gen+1} ===")

        # Evaluate fitness
        fits = [fitness(ind, weights, values, w_max) for ind in population]
        print(f"Population fitness: {fits}")

        # Update global best solution
        idx = np.argmax(fits)
        if fits[idx] > best_fit:
            best_fit = fits[idx]
            best_chrom = population[idx].copy()
        print(f"Best fitness in this iteration: {fits[idx]}, chromosome: {population[idx]}")
        print(f"Current global best fitness: {best_fit}")

        #сохранение статистики
        avg_fit = sum(fits) / pop_size
        history['best'].append(best_fit)
        history['avg'].append(avg_fit)
        print(f"Average fitness: {avg_fit}")

        # Parent selection
        selected = tournament_selection(population, fits, k=tour_k)
        print(f"Selected parents (first 5): {selected[:5]}")

        # Crossover and mutation
        new_pop = []
        for i in range(0, pop_size, 2):
            parent1, parent2 = selected[i], selected[i+1]

            if random.random() < cx_prob:
                if crossover_type == 'one_point':
                    child1, child2 = one_point_crossover(parent1, parent2)
                    print(f"One-point crossover of pairs {i}//{i+1}: point = ..., children = {child1}, {child2}")
                else:
                    child1, child2 = two_point_crossover(parent1, parent2)
                    print(f"Two-point crossover of pairs {i}//{i+1}: segment = ..., children = {child1}, {child2}")
            else:
                #No crossover: children are copies of parents
                child1, child2 = parent1.copy(), parent2.copy()
                print(f"No crossover occurred for the pairs {i}//{i+1}, offspring = parents")
            # мутация
            mutated1 = mutate(child1, mut_prob)
            mutated2 = mutate(child2, mut_prob)
            print(f"The mutation of descendants: before={child1}, after={mutated1}")
            print(f"Мутация потомков: before={child2}, after={mutated2}\n")
            new_pop.extend([mutated1, mutated2])

        population = new_pop
    return best_chrom, best_fit, history





if __name__ == '__main__':

    w_max, weights, values = load_data('data_knapsack01.txt')
    # Подбираем параметры
    pop_size = 50 # 10-100
    generations = 50 #oko 100 norm
    cx_prob = 0.8 #0.6 - 0.9
    mut_prob = 0.04 #1-5%
    tour_k = 3
    crossover_type = 'one_point'

    best, bf, hist = run_ga(
        weights, values, w_max,
        pop_size=pop_size,
        generations=generations,
        cx_prob=cx_prob,
        mut_prob=mut_prob,
        tour_k=tour_k,
        crossover_type=crossover_type
    )
    total_w = np.dot(best, weights)

    # Output the final solution
    print("=== Final result ===")
    print(f"Maximum capacity: {w_max}")
    print(f"Best value (fit): {bf}")
    print(f"Total weight of selected items: {total_w}")
    print(f"Binary chromosome: {best}")

    # Decode and output details
    selected_indices = [i for i, gene in enumerate(best) if gene == 1]
    print("Selected items (index, weight, value):")
    for idx in selected_indices:
        print(f"  No.{idx}: weight = {weights[idx]}, value = {values[idx]}")
    print(f"Total number of selected items: {len(selected_indices)}")



"""
  # Experiment series for crossover comparison
    def experiment(runs):
        stats = {'one_point': [], 'two_point': []}
        for cx in ['one_point', 'two_point']:
            for run in range(runs):
                random.seed(run)
                np.random.seed(run)
                _, fitness_val, _ = run_ga(weights, values, w_max,
                                           pop_size=50, generations=20,
                                           cx_prob=0.8, mut_prob=0.02,
                                           tour_k=3, crossover_type=cx)
                stats[cx].append(fitness_val)
        for cx, vals in stats.items():
            arr = np.array(vals)
            print(f"Method {cx}: mean={arr.mean():.1f}, max={arr.max()}, std={arr.std():.1f}")

    print("\n=== 30-run Experiment Comparison ===")
    experiment(30)
"""
