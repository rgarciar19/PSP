import psutil

try: 
    for proc in psutil.process_iter():
        processName=proc.name()
        processID= proc.pid
        print(processName, "---", processID)
    
    pidEliminar=input("Dime el PID del proceso el cual quieres cerrar")
    try:
        pidEliminar=int(pidEliminar)
        proceso = psutil.Process(pidEliminar)
        proceso.terminate()
        print("Se ha cerrado con éxito")
    except:
        print("Tienes que decirme un PID válido")    
except:
    print("error")
    
