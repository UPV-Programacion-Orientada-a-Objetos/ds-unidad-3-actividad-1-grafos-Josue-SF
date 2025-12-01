# distutils: language = c++

from libcpp.vector cimport vector
from libcpp.utility cimport pair
from libcpp.string cimport string
from libcpp cimport bool

cdef extern from "../include/grafo_base.hpp" namespace "neuronet":
    pass

cdef extern from "../include/grafo_disperso.hpp" namespace "neuronet":
    cdef cppclass GrafoDisperso:
        GrafoDisperso() except +
        void cargarDatos(const string& path, bool dirigido) except +
        pair[int, long long] getSizes() const
        int nodoMasCriticoSalida() const
        int nodoMasCriticoEntrada() const
        pair[vector[int], vector[pair[int, int]]] BFS(int start, int max_depth) const except +
        int DFS_componentes() const
        vector[int] obtenerVecinos(int u) const except +
