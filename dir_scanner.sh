# !/bin/bash
# SCRIPT DE ENUMERACIÓN WEB
# CREADO CON LA FINALIDAD DE ESCANEAR CON DIVERSAS HERRAMIENTAS UNA PÁGINA WEB EN BUSCA DE DIRECTORIOS OCULTOS
# HERRAMIENTAS EMPLEADAS GOBUSTER, DIRSEARCH Y DIRB 

webs=("http://192.168.0.0") # CAMBIAR 
wordlist="/usr/share/wordlists/dirb/common.txt" # CAMBIAR WORDLIST A GUSTO DEL USUARIO 

for web in "${webs[@]}"; do 
echo -e "\n Enumerando directorios con Gobuster. URL: $web"
gobuster dir -u "$web" -w "$wordlist"

echo -e "\n Enumerando directorios con dirsearch. URL: $web"
dirsearch -u "$web"

echo -e "\n Enumerando directorios con dirb. URL: $web"
dirb "$web" "$wordlist"

done