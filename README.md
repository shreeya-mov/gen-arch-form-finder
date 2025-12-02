# MorphoGen: Evolving Architectural Silhouettes With Genetic Algorithms

Term project for CSCI6550 - Artificial Intelligence	

AI-driven genetic algorithm that evolves architectural forms using parametric shape encodings, fitness functions, and evolutionary optimization.

Project Description: This project uses a genetic algorithm to evolve architectural silhouettes defined by parametric control points.
Each silhouette is evaluated on stability, symmetry, and curvature smoothness, which are three principles foundational to aesthetic and structural design.

Over generations, the algorithm converges to forms exhibiting balanced proportions and smooth curvature profiles, demonstrating how AI can assist early-stage conceptual design.

## Run Locally

Clone the project

```bash
  git clone https://github.com/shreeya-mov/gen-arch-form-finder.git
```

Go to the project directory

```bash
  cd project-directory
```

Install dependencies

```bash
  pip install -r requirements.txt 
```

run main.py

```bash
 python3 main.py
 python3 make_gif.py
```

See the output/graphs/visualizations on localhost website 

Process Flow: Random Shape → Evaluate → Select → Crossover → Mutate → New Generation 

Evolution of Architectural Silhouettes

![evolution](https://github.com/user-attachments/assets/c9f9d727-f749-4e8a-a937-912f0f914194)

The animation above shows the best-performing architectural silhouette in each generation.
The genetic algorithm gradually increases stability, symmetry, and curvature smoothness,
leading to more refined forms over time.

