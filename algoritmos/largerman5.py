import numpy as np
import matplotlib.pyplot as plt


# Definición de la función Langerman-5
def langerman5(x):
    c = np.array([0.806, 0.517, 1.5, 0.908, 0.965])
    A = np.array(
        [
            [9.681, 0.667, 4.783, 9.095, 3.517, 9.325, 6.544, 0.211, 5.122, 2.020],
            [9.400, 2.041, 3.788, 7.931, 2.882, 2.672, 3.568, 1.284, 7.033, 7.374],
            [8.025, 9.152, 5.114, 7.621, 4.564, 4.711, 2.996, 6.126, 0.734, 4.982],
            [2.196, 0.415, 5.649, 6.979, 9.510, 9.166, 6.304, 6.054, 9.377, 1.426],
            [8.074, 8.777, 3.467, 1.863, 6.708, 6.349, 4.534, 0.276, 7.633, 1.567],
        ]
    )

    result = 0
    for i in range(5):
        result += (
            c[i]
            * np.exp(-(np.sum((x - A[i, :]) ** 2)) / np.pi)
            * np.cos(np.pi * np.sum((x - A[i, :]) ** 2))
        )
    return -result


def no_practical_example():
    # Crear una malla de puntos
    x = np.linspace(0, 10, 100)
    y = np.linspace(0, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)

    # Evaluar la función en la malla
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = langerman5(np.array([X[i, j], Y[i, j], 0, 0, 0, 0, 0, 0, 0, 0]))

    # Plotear los resultados
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, cmap="viridis")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Langerman-5")

    plt.savefig("images/langerman5.png")
    plt.show()


if __name__ == "__main__":
    no_practical_example()