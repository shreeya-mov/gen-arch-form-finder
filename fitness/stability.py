import numpy as np

def stability_score(shape):
    """
    Heuristic structural stability score.
    More compact shapes (points closer to their centroid) get higher scores.
    """
    cp = shape.control_points   # (N, 2) numpy array of control points
    center = cp.mean(axis=0)    # centroid of points
    spread = np.linalg.norm(cp - center, axis=1)  # distances from center

    # Smaller mean spread -> more compact -> higher score (bounded (0, 1])
    return 1.0 / (1.0 + spread.mean())

