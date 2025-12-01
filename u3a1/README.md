# Neuronet Graph Engine

Motor de grafos de alto rendimiento en C++ con bindings de Python y GUI Streamlit.

## Requisitos
- Python 3.8+
- Compilador C++ compatible con C++17 (MSVC en Windows, GCC/Clang en Linux)
- Librerías Python: `streamlit`, `networkx`, `matplotlib`, `cython`, `pytest`

## Estructura
- `include/`: Headers C++
- `src/`: Código fuente C++
- `neuronet/`: Paquete Python y bindings Cython
- `tests/`: Tests unitarios
- `examples/`: Datos de ejemplo

## Compilación e Instalación

1.  Crear entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

2.  Instalar dependencias:
    ```bash
    pip install streamlit networkx matplotlib cython pytest scipy
    ```

3.  Compilar la extensión C++ (inplace):
    ```bash
    python setup.py build_ext --inplace
    ```

## Ejecución

### GUI Streamlit
```bash
streamlit run neuronet/gui.py
```

### Tests
```bash
pytest tests/test_wrapper.py
```

## Uso de la API

```python
from neuronet.grafo_cy import PyGrafo

g = PyGrafo()
g.cargar_datos("examples/small_graph.txt", dirigido=False)

# Métricas
v, e = g.get_sizes()
print(f"V: {v}, E: {e}")

# BFS
visitados, aristas = g.bfs(start=0, max_depth=2)
```
