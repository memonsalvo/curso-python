from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/miguel/Desktop/curso-python/dia6/Prueba2.txt')

ruta_windows = PureWindowsPath(carpeta)
print(carpeta.read_text())