from ga.genetic_algorithm import GeneticAlgorithm

if __name__ == "__main__":
    print("main.py is running")
    print("Starting Genetic Algorithm Evolution")
    ga = GeneticAlgorithm(pop_size=10, mutation_rate=0.1)
    ga.evolve(generations=5)
