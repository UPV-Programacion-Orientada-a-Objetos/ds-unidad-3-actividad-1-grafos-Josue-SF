#pragma once
#include <string>
#include <vector>
#include <tuple>
#include <utility>

namespace neuronet {

class GrafoBase {
public:
    virtual ~GrafoBase() = default;

    // Carga datos desde un archivo edge-list
    virtual void cargarDatos(const std::string& path, bool dirigido) = 0;

    // Retorna (num_vertices, num_edges)
    virtual std::pair<int32_t, int64_t> getSizes() const = 0;

    // Retorna el nodo con mayor grado de salida
    virtual int32_t nodoMasCriticoSalida() const = 0;

    // Retorna el nodo con mayor grado de entrada
    virtual int32_t nodoMasCriticoEntrada() const = 0;

    // BFS desde start hasta max_depth. Retorna (nodos_visitados, aristas_subgrafo)
    // aristas_subgrafo es un vector de pares (u, v)
    virtual std::pair<std::vector<int32_t>, std::vector<std::pair<int32_t, int32_t>>> 
    BFS(int32_t start, int32_t max_depth) const = 0;

    // DFS para contar componentes conexas. Retorna mapa {component_id: count} o similar
    // Para simplificar, retornamos el número de componentes conexas
    virtual int32_t DFS_componentes() const = 0;
    
    // Obtener vecinos de un nodo (para validación/debug)
    virtual std::vector<int32_t> obtenerVecinos(int32_t u) const = 0;
};

} // namespace neuronet
