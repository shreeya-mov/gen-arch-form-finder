import numpy as np
from .individual import Individual

class GeneticAlgorithm:
    def __init__(self, pop_size=20, mutation_rate=0.1):
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.population = [Individual() for _ in range(pop_size)]

    def evolve(self, generations=30):
        for g in range(generations):
            print(f"\n=== Generation {g} ===")

            # 1. Evaluate population
            scores = [ind.evaluate() for ind in self.population]
            avg_score = float(np.mean(scores))
            best_score = float(np.max(scores))

            print(f"Average fitness: {avg_score:.4f}")
            print(f"Best fitness:    {best_score:.4f}")

            # 2. Select top 50%
            idx = np.argsort(scores)[-self.pop_size // 2:]
            parents = [self.population[i] for i in idx]

            # 3. Reproduce new population
            new_pop = []
            for i in range(self.pop_size):
                p1, p2 = np.random.choice(parents, 2)
                child_encoding = p1.encoding.crossover(p2.encoding)
                child_encoding.mutate(self.mutation_rate)
                new_pop.append(Individual(child_encoding))

            self.population = new_pop

        print("\n=== Evolution complete ===")
