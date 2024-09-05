from largerman5 import langerman5
from scipy.optimize import minimize
import numpy as np

_SEED = 1
bounds = [(0, 10)] * 10
rng = np.random.default_rng(_SEED)
x0 = rng.uniform(0, 10, 10)
iterations = []

result = minimize(
    langerman5,
    x0,
    bounds=bounds,
    method="BFGS",
    options={
        "disp": True,  # Mostrar detalles del proceso
        "gtol": 1e-10,  # Gradiente de tolerancia para asegurar que haya iteraciones
        "maxiter": 1000,  # Número máximo de iteraciones para permitir más búsqueda
        "return_all": True,
    },
)
