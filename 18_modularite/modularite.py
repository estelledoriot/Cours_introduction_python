import sys
from pathlib import Path


def show_argv_and_path():
    print(f"le répertoire courant est {Path.cwd()}")
    print(f"le point d'entrée du programme est {sys.argv[0]}")
    print("la variable sys.path contient")
    for i, path in enumerate(sys.path, 1):
        print(f"{i}-ème chemin dans sys.path {path}")


show_argv_and_path()
