import numpy as np

# Definición de la función Langerman-5
def langerman5(x):
    c = np.array([0.806, 0.517, 1.5, 0.908, 0.965])
    A = np.array([
        [9.681, 0.667, 4.783, 9.095, 3.517, 9.325, 6.544, 0.211, 5.122, 2.020],
        [9.400, 2.041, 3.788, 7.931, 2.882, 2.672, 3.568, 1.284, 7.033, 7.374],
        [8.025, 9.152, 5.114, 7.621, 4.564, 4.711, 2.996, 6.126, 0.734, 4.982],
        [2.196, 0.415, 5.649, 6.979, 9.510, 9.166, 6.304, 6.054, 9.377, 1.426],
        [8.074, 8.777, 3.467, 1.863, 6.708, 6.349, 4.534, 0.276, 7.633, 1.567]
    ])

    result = 0
    for i in range(5):
        result += (
            c[i]
            * np.exp(-(np.sum((x - A[i, :]) ** 2)) / np.pi)
            * np.cos(np.pi * np.sum((x - A[i, :]) ** 2))
        )
    return -result

# Función para calcular el gradiente numérico
def numerical_gradient(f, x, epsilon=1e-8):
    grad = np.zeros_like(x)
    for i in range(len(x)):
        x0 = np.copy(x)
        x1 = np.copy(x)
        x0[i] -= epsilon
        x1[i] += epsilon
        grad[i] = (f(x1) - f(x0)) / (2 * epsilon)
    return grad

# Algoritmo de Descenso de Gradiente
def gradient_descent(f, x0, learning_rate=0.01, max_iter=1000, tolerance=1e-6):
    x = np.copy(x0)
    for i in range(max_iter):
        grad = numerical_gradient(f, x)
        x_new = x - learning_rate * grad

        # Verificar convergencia
        if np.linalg.norm(x_new - x) < tolerance:
            break
        x = x_new
        print(f"Iteración {i + 1}: x = {x}, f(x) = {f(x)}")
    return x, f(x)

# Inicialización
x0 = np.random.uniform(0, 10, 10)  # Punto de inicio aleatorio
minimo, valor_minimo = gradient_descent(langerman5, x0)

print(f"Mínimo encontrado por Descenso de Gradiente: {valor_minimo}")
print(f"Coordenadas del mínimo: {minimo}")

