import numpy as np

def symmetry_score(shape):
    """
    Simple left-right symmetry heuristic.
    Lower variance in x-coordinates => more symmetric => higher score.
    """
    cp = shape.control_points            # (N, 2)
    x_coords = cp[:, 0]                  # x positions
    return 1.0 / (1.0 + np.std(x_coords))

def curvature_smoothness(shape):
    """
    Measures smoothness by how much the direction between
    consecutive segments changes. Less change => smoother curves.
    """
    cp = shape.control_points
    diffs = np.diff(cp, axis=0)
    if len(diffs) < 2:
        return 1.0  # trivial case, treat as perfectly smooth

    second_diffs = np.diff(diffs, axis=0)
    curvature = np.linalg.norm(second_diffs, axis=1)
    return 1.0 / (1.0 + curvature.mean())
