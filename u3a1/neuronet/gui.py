import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import tempfile
import os
import sys

# Asegurar que podemos importar el módulo compilado si estamos en la raíz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from neuronet.grafo_cy import PyGrafo
except ImportError:
    st.error("No se pudo importar el módulo 'neuronet.grafo_cy'. Asegúrate de haber compilado la extensión (python setup.py build_ext --inplace).")
    st.stop()

st.set_page_config(page_title="Neuronet Graph Engine", layout="wide")

st.title("Neuronet Graph Engine")
st.markdown("Motor de grafos de alto rendimiento en C++ con visualización en Python.")

# Sidebar para carga de datos
st.sidebar.header("Configuración")
uploaded_file = st.sidebar.file_uploader("Cargar archivo edge-list", type=["txt", "csv"])
is_directed = st.sidebar.checkbox("Grafo Dirigido", value=False)

if 'grafo' not in st.session_state:
    st.session_state.grafo = None
if 'graph_loaded' not in st.session_state:
    st.session_state.graph_loaded = False

if uploaded_file is not None:
    # Guardar archivo temporalmente
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name

    if st.sidebar.button("Cargar Grafo"):
        with st.spinner("Cargando grafo..."):
            try:
                grafo = PyGrafo()
                grafo.cargar_datos(tmp_path, is_directed)
                st.session_state.grafo = grafo
                st.session_state.graph_loaded = True
                st.success("Grafo cargado exitosamente.")
            except Exception as e:
                st.error(f"Error al cargar el grafo: {e}")
            finally:
                # Limpiar archivo temporal
                try:
                    os.remove(tmp_path)
                except:
                    pass

if st.session_state.graph_loaded:
    grafo = st.session_state.grafo
    num_vertices, num_edges = grafo.get_sizes()
    
    # Métricas Generales
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Nodos", f"{num_vertices:,}")
    col2.metric("Aristas", f"{num_edges:,}")
    
    if st.button("Calcular Nodos Críticos"):
        with st.spinner("Calculando..."):
            max_out = grafo.nodo_mas_critico_salida()
            max_in = grafo.nodo_mas_critico_entrada()
            col3.metric("Max Grado Salida (ID)", max_out)
            col4.metric("Max Grado Entrada (ID)", max_in)
            
    st.divider()
    
    # Análisis BFS y Visualización
    st.header("Análisis de Subgrafos (BFS)")
    
    c1, c2 = st.columns(2)
    start_node = c1.number_input("Nodo Inicial", min_value=0, max_value=num_vertices-1, value=0)
    max_depth = c2.number_input("Profundidad Máxima", min_value=1, max_value=5, value=2)
    
    if st.button("Ejecutar BFS y Visualizar"):
        with st.spinner("Ejecutando BFS..."):
            visitados, aristas = grafo.bfs(start_node, max_depth)
            
            st.write(f"Nodos visitados: {len(visitados)}")
            st.write(f"Aristas en subgrafo: {len(aristas)}")
            
            if len(visitados) > 1000:
                st.warning("El subgrafo es demasiado grande para visualizar (>1000 nodos). Se mostrarán solo métricas.")
            else:
                # Visualizar con NetworkX
                G_vis = nx.DiGraph() if is_directed else nx.Graph()
                G_vis.add_edges_from(aristas)
                
                fig, ax = plt.subplots(figsize=(10, 6))
                pos = nx.spring_layout(G_vis, seed=42)
                
                # Dibujar nodos
                nx.draw_networkx_nodes(G_vis, pos, node_size=300, node_color='skyblue', alpha=0.8, ax=ax)
                # Dibujar aristas
                nx.draw_networkx_edges(G_vis, pos, width=1.0, alpha=0.5, arrowstyle='-|>', arrowsize=10, ax=ax)
                # Dibujar etiquetas si son pocos nodos
                if len(visitados) < 50:
                    nx.draw_networkx_labels(G_vis, pos, font_size=10, ax=ax)
                
                ax.set_title(f"Subgrafo BFS desde nodo {start_node} (d={max_depth})")
                ax.axis('off')
                st.pyplot(fig)

    st.divider()
    
    # Componentes Conexas
    if st.button("Contar Componentes Conexas (DFS)"):
        with st.spinner("Ejecutando DFS..."):
            num_comp = grafo.dfs_componentes()
            st.metric("Componentes Conexas", num_comp)

else:
    st.info("Por favor, carga un archivo edge-list para comenzar.")
