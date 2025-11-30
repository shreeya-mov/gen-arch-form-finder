#!/usr/bin/env python3
print("Script starting...")

try:
    print("Importing GA...")
    from ga.genetic_algorithm import GeneticAlgorithm
    print("GA imported successfully")
    
    print("Creating GA instance...")
    ga = GeneticAlgorithm(pop_size=30, mutation_rate=0.05)
    print("GA instance created")
    
    print("Running evolution...")
    ga.evolve(generations=40)
    print("Evolution complete!")
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
