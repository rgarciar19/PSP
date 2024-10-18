import subprocess
numeros=[1,2,3,4]

proceso=subprocess.Popen(["python","maximo.py"],
                            stdin=subprocess.PIPE, 
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE,
                           ) 
salida,error=proceso.communicate(b"1\n2\n3\n1\nfin\n")
#salida,error=proceso.communicate(input=numeros)
print(salida.decode())
