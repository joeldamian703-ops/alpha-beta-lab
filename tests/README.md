# Laboratorio Minimax y Poda Alfa-Beta

Curso: Sistemas Inteligentes  
Estudiante: Cesar Joel Sirlopu Damian

## Objetivo

Implementar Minimax y Poda Alfa-Beta y comparar la cantidad
de hojas evaluadas sin modificar el valor final obtenido.

## Instalación en Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Ejecutar el programa

```powershell
.\.venv\Scripts\python.exe -m src.main
```

## Ejecutar pruebas con cobertura

```powershell
.\.venv\Scripts\python.exe -m pytest -v --cov=src --cov-report=term-missing --cov-report=xml --cov-fail-under=100
```

## Resultados

| Árbol | Valor de ambos algoritmos | Hojas Minimax | Hojas Alfa-Beta | Ramas podadas | Reducción de hojas |
|---|---:|---:|---:|---:|---:|
| Pequeño | 3 | 4 | 3 | 1 | 25 % |
| Mediano | 7 | 12 | 8 | 3 | 33.33 % |
| Ordenado | 8 | 12 | 8 | 2 | 33.33 % |

Se aprobaron 12 pruebas con 100 % de cobertura de líneas.
La cobertura no garantiza la ausencia de errores.

El contador nodes_evaluated registra hojas evaluadas.
branches_pruned cuenta ramas hijas omitidas en los cortes,
no todas las hojas o nodos contenidos en esas ramas.

Los resultados esperados de la guía se corrigieron a 3, 7 y 8,
respetando sus árboles y la alternancia de MAX y MIN.

## Preguntas de análisis

### 1. ¿Por qué Alfa-Beta obtiene el mismo resultado que Minimax?

Porque solo omite ramas que, según los límites obtenidos,
no pueden cambiar el valor final. Ambos utilizan las mismas
reglas de maximización y minimización.

### 2. ¿Qué representa alpha?

Es el mejor límite inferior conocido para MAX durante
la búsqueda. MAX puede asegurar al menos ese valor.

### 3. ¿Qué representa beta?

Es el mejor límite superior conocido para MIN durante
la búsqueda. MIN puede asegurar un resultado no mayor
que ese valor.

### 4. ¿Cuándo Alfa-Beta ahorra más trabajo?

Cuando se exploran primero las mejores opciones:
valores altos para MAX y bajos para MIN. Esto permite
establecer límites útiles antes y realizar más podas.

### 5. ¿Por qué influye el orden de exploración?

Porque determina cuándo se descubren los límites alpha
y beta. Un orden desfavorable puede producir pocas podas
y hacer que Alfa-Beta explore tantas hojas como Minimax.

Los árboles mediano y ordenado del experimento son distintos.
Por eso, sus resultados no aíslan el efecto del orden;
para hacerlo habría que reordenar un mismo árbol.

### 6. ¿Qué ocurre si el rival no juega racionalmente?

Minimax mantiene una estrategia frente a un rival óptimo.
Si el rival comete errores, el resultado puede ser mejor
que el valor previsto, pero el algoritmo no modela
la probabilidad de esos errores.

### 7. ¿Cómo se relaciona con motores de ajedrez?

Permite explorar movimientos y respuestas del rival.
Como el árbol completo es enorme, se limita la profundidad
y se evalúan posiciones intermedias mediante una función
de evaluación.

### 8. ¿Qué limitaciones tiene frente a redes neuronales
o aprendizaje por refuerzo?

La búsqueda crece rápidamente con la profundidad y necesita
reglas y una evaluación del juego. No aprende por sí sola
a partir de experiencias. Las redes neuronales y el
aprendizaje por refuerzo pueden aprender evaluaciones
o estrategias y también combinarse con la búsqueda.

## Integración continua

El workflow .github/workflows/ci.yml ejecuta las pruebas
y verifica la cobertura en GitHub Actions al hacer push
o pull request hacia main o develop.