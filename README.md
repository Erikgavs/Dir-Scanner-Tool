# Dir-Scanner-Tool
dir_scanner es un pequeño script que usa 3 herramientas (gobuster, dirsearch y dirb) para escanear y buscar directorios ocultos en páginas web, bastante útil para dejarla de fondo mientras realizamos otras tareas 

## Guia de dir_scanner.py y dir_scanner.sh
El script está tanto en python como en bash, para evitar cualquier problema y que sea compatible en la mayoría de los casos
Muy importante tener las herramientas Gobuster, dirsearch y dirb instaladas, de no ser así, el script no funcionará corrrectamente

---

## dir_scanner.py
Para usarlo tendremos que tener python3 instalado
```bash
python3 dir_scanner.py
```

## dir_scanner.sh
Para usarlo tendremos que otorgarle permisos de ejecucción y ya podremos usarlo
```bash
chmod +x ./dir_scanner.sh
./dir_scanner.sh
```
