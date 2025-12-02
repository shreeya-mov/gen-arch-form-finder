import os
import numpy as np
from .individual import Individual
from shapes.visualization import plot_shape

class GeneticAlgorithm:
    def __init__(self, pop_size=20, mutation_rate=0.1):
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.population = [Individual() for _ in range(pop_size)]

        # analysis/plotting
        self.history_avg = []
        self.history_best = []
        self.best_per_generation = []
        self.global_best = None

    def evolve(self, generations=30, save_dir=None):
        # if save_dir is provided, save a silhoutte image of the best individual each generation
        if save_dir is not None:
            os.makedirs(save_dir, exist_ok=True)

            print(f"Saving generation images to: {save_dir}")
            
        for g in range(generations):
            print(f"\n=== Generation {g} ===")

            scores = [ind.evaluate() for ind in self.population]
            avg_score = float(np.mean(scores))
            best_score = float(np.max(scores))
            best_idx = int(np.argmax(scores))
            best_ind = self.population[best_idx]

            self.history_avg.append(avg_score)
            self.history_best.append(best_score)
            self.best_per_generation.append(best_ind)

            # Track global best across all generations
            if self.global_best is None or best_score > self.global_best.score:
                self.global_best = best_ind

            print(f"Average fitness: {avg_score:.4f}")
            print(f"Best fitness:    {best_score:.4f}\n")

            # Save silhouette for this generation
            if save_dir is not None:
                img_path = os.path.join(save_dir, f"gen_{g:03d}.png")
                plot_shape(
                    best_ind.encoding,
                    title=f"Generation {g}",
                    save_path=img_path,
                    show=False,
                )

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

        print("=== Evolution complete ===")
        return self.history_avg, self.history_best
