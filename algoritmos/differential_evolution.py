import time
from scipy.optimize import differential_evolution
from largerman5 import langerman5
from matplotlib import pyplot as plt

bounds = [(0, 10)] * 10
duration = time.time()
iter_solutions = []

ti = [0]


def callback(xk, convergence):
    ti.append(duration - ti[-1])
    iter_solutions.append((xk, langerman5(xk)))


result = differential_evolution(
    langerman5,
    bounds,
    strategy="best1bin",  # Estrategia comúnmente usada
    popsize=30,  # Aumenta el tamaño de la población para una mejor exploración
    mutation=(0.5, 1),  # Ajuste del factor de mutación
    recombination=0.7,  # Tasa de recombinación
    maxiter=5000,  # Aumenta el número de iteraciones para asegurar convergencia
    tol=1e-5,  # Tolerancia para detener el criterio
    seed=42,  # Fijar la semilla para la reproducibilidad,
    disp=True,
    callback=callback,
)

duration = time.time() - duration
print()
print(f"Mínimo encontrado: {result.fun}")
print(f"Coordenadas del mínimo: {result.x}")
print(f"Duración: {duration:.2f} segundos")
print(f"Iteraciones: {result.nit}")
print(f"Mensaje de finalización: {result.message}")


print(result)
# Gráfica de convergencia
plt.title("Convergencia de la función Langerman-5, DE")
plt.xlabel("Iteraciones")
plt.ylabel("f(x*) por iteraciones")
plt.plot([i[1] for i in iter_solutions])
plt.grid(visible=True)
plt.savefig("images/convergencia_de.png")
plt.show()

# plotear iteracion tiempo
plt.title("Tiempo por iteraciones")
plt.xlabel("Iteraciones")
plt.ylabel("Tiempo")
plt.plot(ti[1:])
plt.grid(visible=True)
plt.savefig("images/tiempo_por_iteraciones.png")
plt.show()


# plotear 3d iteracion valor tiempo

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("Iteraciones")
ax.set_ylabel("f(x*)")
ax.set_zlabel("Tiempo")
ax.plot(range(len(ti) - 1), [i[1] for i in iter_solutions], ti[1:])
plt.savefig("images/3d_plot.png")
plt.show()
