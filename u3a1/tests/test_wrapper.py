import pytest
import os
from neuronet.grafo_cy import PyGrafo

TEST_FILE = "test_graph_py.txt"

@pytest.fixture
def graph_file():
    with open(TEST_FILE, "w") as f:
        f.write("0 1\n0 2\n1 2\n2 3\n")
    yield TEST_FILE
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_cargar_datos(graph_file):
    g = PyGrafo()
    g.cargar_datos(graph_file, False)
    v, e = g.get_sizes()
    assert v == 4
    assert e == 8

def test_bfs(graph_file):
    g = PyGrafo()
    g.cargar_datos(graph_file, False)
    visitados, aristas = g.bfs(0, 1)
    assert len(visitados) == 3 # 0, 1, 2
    assert 0 in visitados
    assert 1 in visitados
    assert 2 in visitados

def test_componentes(graph_file):
    g = PyGrafo()
    g.cargar_datos(graph_file, False)
    assert g.dfs_componentes() == 1
