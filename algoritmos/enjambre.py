import numpy as np
from pyswarm import pso
from largerman5 import langerman5
import matplotlib.pyplot as plt
import time

lb = [0] * 10  # Límite inferior para cada dimensión
ub = [10] * 10  # Límite superior para cada dimensión


# Inicializar la list a para guardar los valores de la función
best_values = []
duration = time.time()
# Ejecutar el algoritmo PSO
xopt, fopt = pso(
    langerman5,
    lb,
    ub,
    swarmsize=100,
    maxiter=800,
    debug=True,
    minstep=1e-12,
    minfunc=1e-12,
)


print("Mejor solución encontrada:", xopt)
print("Valor de la función en la mejor solución:", fopt)

duration = time.time() - duration
print(f"Duración: {duration:.2f} segundos")
