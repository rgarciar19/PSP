import subprocess
import os
# Verificar si el directorio existe, si no, crearlo
os.makedirs("C:\\dirSalida", exist_ok=True)
# Cambiar el directorio de trabajo (cwd) y redirigir la salida
with open("salida.txt", "w") as f: #Abre (o crea, si no existe) un archivo llamado salida.txten modo escritura (w). La variable f representa el archivo.

    process= subprocess.Popen(["cmd", "/C", "dir"], cwd="C:\\dirSalida", stdout=f)
    process.wait() # Esperar a que el proceso termine
