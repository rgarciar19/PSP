import subprocess
import psutil

proceso=subprocess.Popen(["notepad.exe"],
                            stdin=subprocess.PIPE, 
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE,
                           ) 
process=psutil.Process(proceso.pid)
print (process.nice())
process.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
print (process.nice())