# Facultad de Matemática y Computación. Universidad de La Habana.

## Modelos de Optimización. [Función Langerman-5](./algoritmos/largerman5.py)

[Repositorio del Proyecto en GitHub](https://github.com/Val020213/Largerman-Function.git)

**Osvaldo R. Moreno Prieto - osvaldo0202013@gmail.com**

---

## Introducción

La función de Langerman es una función de prueba comúnmente utilizada en problemas de optimización para evaluar el rendimiento de algoritmos de optimización. Su expresión es la siguiente:

$$
f(\mathbf{x}) = - \sum_{i=1}^{m} c_i \exp \left( - \frac{1}{\pi} \sum_{j=1}^{D} (x_j - a_{ij})^2 \right) \cos \left( \pi \sum_{j=1}^{D} (x_j - a_{ij})^2 \right)
$$

donde:

- \(\mathbf{x}\) es un vector de \(D\) dimensiones.
- \(\mathbf{m}\) es el número de términos en la sumatoria (Langerman-5, m = 5).
- \(\mathbf{A}\) es una matriz de dimensión m x D (generalmente 10)
- \(\mathbf{C}\) es un vector columna de dimensión m.

La función de [Langerman](./algoritmos/largerman5.py) es especialmente útil para evaluar el rendimiento de algoritmos de optimización global debido a las siguientes características:

1. **Multimodal:** Tiene múltiples mínimos locales y globales, lo que desafía a los algoritmos a encontrar el mínimo global evitando quedarse atrapados en mínimos locales.
2. **No Separable:** La función objetivo o las restricciones no pueden descomponerse en sumas de funciones más simples que dependen de subconjuntos disjuntos de variables. Esto significa que las variables están interrelacionadas de manera compleja, y no se pueden optimizar de forma independiente.
3. **Escalabilidad:** Es escalable en términos de dimensión, permitiendo probar algoritmos en espacios de búsqueda de diferentes tamaños.
4. **Combinación de Componentes Exponenciales y Trigonométricos:** Incluye términos que crean un paisaje de optimización complejo con múltiples picos y valles.
5. **Dificultad Controlada por Parámetros:** Los parámetros pueden ajustarse para modificar la dificultad del problema, adaptándose a diferentes escenarios de prueba.

### Descripción del problema

El propósito del estudio es evaluar la eficacia de varios algoritmos en la búsqueda de soluciones, comparando su proximidad con la solución conocida, así como analizar su rendimiento en términos de cantidad de iteraciones y tiempo requerido para converger. Se conoce que la función [Langerman-5](./algoritmos/largerman5.py) (Continua, diferenciable, no separable, escalable y multimodal) con la siguiente restricción:

$$
0 \leq x_j \leq 10, \quad \text{donde} \; j \in [0, D-1], \quad \text{y} \; m = 5.
$$

La función tiene un mínimo global con un valor de:

f(x\*) = -1.4.

Usando la matriz \(A\) y el vector columna \(c\) siguientes:

$$
A = \begin{bmatrix}
9.681 & 0.667 & 4.783 & 9.095 & 3.517 & 9.325 & 6.544 & 0.211 & 5.122 & 2.020 \\
9.400 & 2.041 & 3.788 & 7.931 & 2.882 & 2.672 & 3.568 & 1.284 & 7.033 & 7.374 \\
8.025 & 9.152 & 5.114 & 7.621 & 4.564 & 4.711 & 2.996 & 6.126 & 0.734 & 4.982 \\
2.196 & 0.415 & 5.649 & 6.979 & 9.510 & 9.166 & 6.304 & 6.054 & 9.377 & 1.426 \\
8.074 & 8.777 & 3.467 & 1.863 & 6.708 & 6.349 & 4.534 & 0.276 & 7.633 & 1.567
\end{bmatrix}
$$

$$
c = \begin{bmatrix}
0.806 \\
0.517 \\
1.5 \\
0.908 \\
0.965
\end{bmatrix}
$$

Para el estudio usamos los siguientes algoritmos (implementados en la biblioteca `scipy`):

- [**Método BFGS:**](./algoritmos/bfgs.py) El método BFGS (Broyden-Fletcher-Goldfarb-Shanno) es un algoritmo de optimización que pertenece a la clase de los métodos de Quasi-Newton. Estos métodos buscan aproximar la matriz hessiana sin necesidad de calcularla explícitamente. En lugar de ello, construyen una aproximación mediante actualizaciones basadas en las evaluaciones de la función y su gradiente. El BFGS es uno de los métodos más eficientes en esta categoría debido a su convergencia superlineal. Este método es especialmente útil en problemas sin restricciones o con restricciones simples.

- [**Algoritmo de Enjambre de Partículas (PSO):**](./algoritmos/enjambre.py) El algoritmo de enjambre de partículas es un método de optimización basado en poblaciones que se inspira en el comportamiento colectivo de los enjambres naturales, como las bandadas de aves o los bancos de peces. Cada "partícula" en el enjambre representa una posible solución al problema de optimización, y las partículas se mueven por el espacio de búsqueda influenciadas tanto por su propia mejor posición como por las mejores posiciones encontradas por sus compañeras de enjambre. Este enfoque es particularmente efectivo para problemas multimodal debido a su capacidad para explorar globalmente el espacio de búsqueda mientras explota las mejores soluciones locales. Además, su simplicidad y flexibilidad lo hacen ideal para problemas complejos y de alta dimensionalidad.

- [**Evolución Diferencial con L-BFGS-B:**](./algoritmos/differential_evolution.py) La Evolución Diferencial es un algoritmo de optimización basado en poblaciones que utiliza operadores de mutación, cruce y selección para explorar el espacio de soluciones de manera estocástica. Este método es particularmente efectivo para problemas con múltiples óptimos locales y funciones objetivo complejas. Al combinar la Evolución Diferencial con el algoritmo L-BFGS-B (Limited-memory BFGS with Bound constraints), se logra una optimización más eficiente en presencia de restricciones de caja (bound constraints). El L-BFGS-B es una variante del método BFGS que maneja de manera efectiva las restricciones de límite, utilizando una representación de memoria limitada para aproximar la matriz hessiana, lo que lo hace adecuado para problemas de gran escala.
