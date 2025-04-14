# SCRIPT DE ENUMERACIÓN WEB
# CREADO CON LA FINALIDAD DE ESCANEAR CON DIVERSAS HERRAMIENTAS UNA PÁGINA WEB EN BUSCA DE DIRECTORIOS OCULTOS
# HERRAMIENTAS EMPLEADAS GOBUSTER, DIRSEARCH Y DIRB 

import subprocess

webs = ["http://192.168.2.1"] # CAMBIAR 
wordlist = ["/usr/share/wordlists/dirb/common.txt"] # CAMBIAR A GUSTO DEL USUARIO

for web in webs:
    print(f"En proceso de enumeración de directorios web con Gobuster {webs}")
    subprocess.run (["gobuster", "dir", "-u", web, "-w", wordlist])
    
    print(f"En proceso de enumeración de directorios web con dirsearch{webs}")
    subprocess.run (["dirsearch", "-u", web])

    print(f"En proceso de enumeración de directorios web con dirb{webs}")
    subprocess.run (["dirb", web, wordlist])

