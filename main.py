import os
import matplotlib.pyplot as plt
from ga.genetic_algorithm import GeneticAlgorithm
from shapes.visualization import plot_shape
import subprocess

if __name__ == "__main__":
    # Where to save results
    results_dir = "results"
    silhouettes_dir = os.path.join(results_dir, "silhouettes")
    top_forms_dir = os.path.join(results_dir, "top_forms")
    os.makedirs(results_dir, exist_ok=True)
    os.makedirs(top_forms_dir, exist_ok=True)

    # Run GA and save a silhouette per generation
    ga = GeneticAlgorithm(pop_size=30, mutation_rate=0.05)
    avg_hist, best_hist = ga.evolve(generations=40, save_dir=silhouettes_dir)

    # 1. Plot fitness over generations
    plt.figure()
    plt.plot(avg_hist, label="Average Fitness")
    plt.plot(best_hist, label="Best Fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Fitness Over Generations")
    plt.legend()
    fitness_plot_path = os.path.join(results_dir, "fitness_over_generations.png")
    plt.savefig(fitness_plot_path, bbox_inches="tight", dpi=300)
    plt.close()
    print(f"Saved fitness plot to {fitness_plot_path}")

    # 2. Save the global best silhouette as a high-res PNG
    if ga.global_best is not None:
        best_final_path = os.path.join(top_forms_dir, "best_final.png")
        plot_shape(
            ga.global_best.encoding,
            title="Best Evolved Architectural Silhouette",
            save_path=best_final_path,
            show=False,
        )
        print(f"Saved best final silhouette to {best_final_path}")

    # 3. Automatically create GIF from silhouettes
    try:
        subprocess.run(["/bin/python3", "make_gif.py"], check=True)
        print("Evolution GIF created and saved to results/evolution.gif")
    except Exception as e:
        print(f"Error creating GIF: {e}")
