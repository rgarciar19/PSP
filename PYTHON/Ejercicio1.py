import psutil
import subprocess
import time
proceso=subprocess.Popen(["calc.exe"])
proceso=psutil.Process(proceso.pid)
procesoPadre=psutil.Process(proceso.ppid())

time.sleep(5)

for proc in psutil.process_iter():
    processName=proc.name()
    if processName =="CalculatorApp.exe" :
        proc.terminate()        


