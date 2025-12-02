import os
from PIL import Image

def make_evolution_gif(
    input_dir="results/silhouettes",
    output_path="results/evolution.gif",
    duration=200,
):
    """
    Create a GIF from per-generation silhouette PNGs using PIL.
    """
    files = sorted(
        f for f in os.listdir(input_dir)
        if f.endswith(".png")
    )

    if not files:
        raise RuntimeError(f"No PNG files found in {input_dir}")

    images = []
    for fname in files:
        path = os.path.join(input_dir, fname)
        images.append(Image.open(path))

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:],
        duration=duration,
        loop=0
    )
    print(f"Saved GIF to {output_path}")

if __name__ == "__main__":
    make_evolution_gif()
