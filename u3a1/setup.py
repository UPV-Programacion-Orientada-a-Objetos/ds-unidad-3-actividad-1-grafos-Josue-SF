from setuptools import setup, Extension
from Cython.Build import cythonize
import os

# Definir la extensión
extensions = [
    Extension(
        name="neuronet.grafo_cy",
        sources=["neuronet/grafo_cy.pyx", "src/grafo_disperso.cpp"],
        include_dirs=["include"],
        language="c++",
        extra_compile_args=["/O2", "/std:c++17"] if os.name == 'nt' else ["-O3", "-march=native", "-std=c++17"],
    )
]

setup(
    name="neuronet",
    version="0.1.0",
    packages=["neuronet"],
    ext_modules=cythonize(extensions, language_level="3"),
    install_requires=[
        "streamlit",
        "networkx",
        "matplotlib",
        "scipy", # often needed by networkx for some layouts
        "cython"
    ],
    zip_safe=False,
)
