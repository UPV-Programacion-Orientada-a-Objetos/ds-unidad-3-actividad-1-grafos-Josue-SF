# distutils: language = c++

from neuronet.grafo_cy cimport GrafoDisperso
from libcpp.string cimport string
from libcpp.vector cimport vector
from libcpp.utility cimport pair

cdef class PyGrafo:
    cdef GrafoDisperso* c_grafo

    def __cinit__(self):
        self.c_grafo = new GrafoDisperso()

    def __dealloc__(self):
        del self.c_grafo

    def cargar_datos(self, str path, bool dirigido=False):
        """Carga datos desde un archivo edge-list."""
        cdef string c_path = path.encode('utf-8')
        self.c_grafo.cargarDatos(c_path, dirigido)

    def get_sizes(self):
        """Retorna (num_vertices, num_edges)."""
        return self.c_grafo.getSizes()

    def nodo_mas_critico_salida(self):
        """Retorna el ID del nodo con mayor grado de salida."""
        return self.c_grafo.nodoMasCriticoSalida()

    def nodo_mas_critico_entrada(self):
        """Retorna el ID del nodo con mayor grado de entrada."""
        return self.c_grafo.nodoMasCriticoEntrada()

    def bfs(self, int start, int max_depth):
        """
        Ejecuta BFS desde start hasta max_depth.
        Retorna (lista_nodos_visitados, lista_aristas_subgrafo).
        """
        cdef pair[vector[int], vector[pair[int, int]]] result = self.c_grafo.BFS(start, max_depth)
        return result.first, result.second

    def dfs_componentes(self):
        """Retorna el número de componentes conexas."""
        return self.c_grafo.DFS_componentes()
        
    def obtener_vecinos(self, int u):
        """Retorna lista de vecinos de u."""
        return self.c_grafo.obtenerVecinos(u)
