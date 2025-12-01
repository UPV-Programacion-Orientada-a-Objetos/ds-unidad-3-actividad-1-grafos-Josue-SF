#pragma once
#include "grafo_base.hpp"
#include <vector>
#include <string>
#include <cstdint>

namespace neuronet {

class GrafoDisperso : public GrafoBase {
public:
    GrafoDisperso();
    ~GrafoDisperso() override = default;

    void cargarDatos(const std::string& path, bool dirigido) override;
    std::pair<int32_t, int64_t> getSizes() const override;
    int32_t nodoMasCriticoSalida() const override;
    int32_t nodoMasCriticoEntrada() const override;
    std::pair<std::vector<int32_t>, std::vector<std::pair<int32_t, int32_t>>> 
    BFS(int32_t start, int32_t max_depth) const override;
    int32_t DFS_componentes() const override;
    std::vector<int32_t> obtenerVecinos(int32_t u) const override;

private:
    // Estructura CSR
    std::vector<int32_t> col_idx;   // Índices de columna (destinos)
    std::vector<int32_t> row_ptr;   // Punteros a filas (offsets)
    
    int32_t num_vertices;
    int64_t num_edges;
    bool es_dirigido;

    // Métodos auxiliares
    void validarNodo(int32_t u) const;
};

} // namespace neuronet
