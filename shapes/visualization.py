import os
import matplotlib.pyplot as plt
import numpy as np

def plot_shape(shape, title="Architectural Silhouette", save_path=None, show=False):
    """
    Plot a 2D building silhouette from a ShapeEncoding (control points).
    Creates an architectural form that looks like a building profile.
    """
    cp = shape.control_points
    
    # Sort points by x-coordinate to create a proper building silhouette
    sorted_indices = np.argsort(cp[:, 0])
    x = cp[sorted_indices, 0]
    y = cp[sorted_indices, 1]
    
    # Normalize to reasonable building proportions
    y_min = np.min(y)
    y_max = np.max(y)
    y_normalized = (y - y_min) / (y_max - y_min + 0.01) * 10  # Scale to 0-10 range (building height)
    
    # Create building profile - close the shape at ground level
    x_building = np.concatenate([x, [np.max(x), np.min(x)]])
    y_building = np.concatenate([y_normalized, [0, 0]])
    
    fig, ax = plt.subplots(figsize=(6, 8), facecolor='white')
    
    # Draw the building silhouette
    ax.fill(x_building, y_building, color='#2c3e50', alpha=0.8, edgecolor='#34495e', linewidth=2)
    
    # Add some window details for architectural realism
    x_range = np.max(x) - np.min(x)
    y_range = np.max(y_normalized) - 0
    
    if x_range > 0 and y_range > 0:
        # Add window pattern
        n_windows_x = max(3, int(x_range / 0.5))
        n_windows_y = max(3, int(y_range / 0.5))
        
        window_width = x_range / (n_windows_x + 1)
        window_height = y_range / (n_windows_y + 1)
        
        for i in range(1, n_windows_x):
            for j in range(n_windows_y):
                window_x = np.min(x) + i * window_width
                window_y = (j + 0.3) * window_height
                # Only draw windows where they fit within the building
                if 0 <= window_y <= y_range:
                    rect = plt.Rectangle((window_x - window_width * 0.2, window_y), 
                                        window_width * 0.4, window_height * 0.4,
                                        facecolor='#f39c12', alpha=0.7, edgecolor='#e67e22', linewidth=0.5)
                    ax.add_patch(rect)
    
    # Draw a ground line
    ax.plot([np.min(x) - 0.5, np.max(x) + 0.5], [0, 0], 'k-', linewidth=3, alpha=0.3)
    
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('Width', fontsize=10)
    ax.set_ylabel('Height', fontsize=10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2, linestyle='--')
    ax.set_facecolor('#ecf0f1')
    
    plt.tight_layout()

    if save_path is not None:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, bbox_inches="tight", dpi=150, facecolor='white')

    if show:
        plt.show()
    else:
        plt.close()
