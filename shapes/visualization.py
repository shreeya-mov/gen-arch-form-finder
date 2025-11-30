import matplotlib.pyplot as plt

def plot_shape(shape):
    x, y = shape.control_points[:,0], shape.control_points[:,1]
    plt.plot(x, y, marker="o")
    plt.title("Architectural Form (Control Points)")
    plt.show()
