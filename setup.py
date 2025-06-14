
# Comandos desde la terminal:

# pip install setuptools

# python setup.py sdist
from setuptools import setup  # , find_packages

setup(
    name="Paquete_Python",
    version="0.1",
    description="Mi primer paquete en Python",
    author="Nicolas",
    author_email="nlopezosornio@email.com",
    # packages=find_packages(),  # Busca automáticamente los paquetes
    packages=["Paquete_Python"],
)
