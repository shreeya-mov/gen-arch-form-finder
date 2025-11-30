# Try both relative and absolute imports, whichever works
try:
    from .stability import stability_score
    from .aesthetics import symmetry_score, curvature_smoothness
except ImportError:
    from fitness.stability import stability_score
    from fitness.aesthetics import symmetry_score, curvature_smoothness

def fitness(shape, w_stability=0.4, w_symmetry=0.3, w_smoothness=0.3):
    s = stability_score(shape)
    sym = symmetry_score(shape)
    smooth = curvature_smoothness(shape)

    return (
        w_stability * s
        + w_symmetry * sym
        + w_smoothness * smooth
    )
