#include <gtest/gtest.h>
#include "../include/grafo_disperso.hpp"
#include <fstream>
#include <filesystem>

namespace fs = std::filesystem;

class GrafoTest : public ::testing::Test {
protected:
    std::string test_file = "test_graph.txt";

    void SetUp() override {
        std::ofstream out(test_file);
        out << "0 1\n";
        out << "0 2\n";
        out << "1 2\n";
        out << "2 3\n";
        out.close();
    }

    void TearDown() override {
        if (fs::exists(test_file)) {
            fs::remove(test_file);
        }
    }
};

TEST_F(GrafoTest, CargarDatosNoDirigido) {
    neuronet::GrafoDisperso g;
    g.cargarDatos(test_file, false);
    
    auto sizes = g.getSizes();
    EXPECT_EQ(sizes.first, 4); // 0, 1, 2, 3
    EXPECT_EQ(sizes.second, 8); // 4 aristas * 2 (no dirigido)
}

TEST_F(GrafoTest, BFS) {
    neuronet::GrafoDisperso g;
    g.cargarDatos(test_file, false);
    
    // BFS desde 0, depth 1 -> 0, 1, 2
    auto res = g.BFS(0, 1);
    EXPECT_EQ(res.first.size(), 3);
    
    // BFS desde 0, depth 2 -> 0, 1, 2, 3
    auto res2 = g.BFS(0, 2);
    EXPECT_EQ(res2.first.size(), 4);
}

TEST_F(GrafoTest, DFSComponentes) {
    neuronet::GrafoDisperso g;
    g.cargarDatos(test_file, false);
    EXPECT_EQ(g.DFS_componentes(), 1);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
