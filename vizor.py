#!/usr/bin/env python3
# ---- VIZOR: Herramienta para red team ---- #

import subprocess
import sys
import ipaddress
import hashlib

#Menú inicial
def menu_inicial():
    #Comprobar idioma  
    if(idioma == "ESP"):
        print("\033[95m-🌸🌸- MENÚ INICIAL VIZOR -🌸🌸-\033[0m")
        print("1. Usar nmap")
        print("2. Usar pingsweep")
        print("3. Calcular sha256 de un archivo")
    else:
        #NORUEGO
        print("\033[95m-🌸🌸- VIZOR HOVEDMENY -🌸🌸-\033[0m")
        print("1. Slitasje nmap")
        print("2. Slitasje pingsweep")
        print("3. Kalkulere sha256 fra en fil")
    
#Pedir input del usuario
def input_opcion():
    while(True):
        #Comprobar idioma
        if(idioma == "ESP"):
            opcion = int(input("Que herramienta quieres utilizar? (1,2,3): "))
        else:
            opcion = int(input("Hvilket verktøy vil du bruke? (1,2,3): "))

        #Comprobar input
        if(opcion == 1 or opcion == 2 or opcion == 3):
            return opcion
        
        if(idioma == "ESP"):
            print("Error: Input no válido")
        else:
            print("Feil: Ugyldig inndata")
    
#Elegir idioma
def elegir_idioma():
    print("\033[95m-🌸🌸- ELECCIÓN DE IDIOMA -🌸🌸-\033[0m")
    print("- ESP")
    print("- NO")

    while(True):
        idioma = input("En que idioma quieres visualizar la herramienta?: ").upper()

        #Comprobar input idioma
        if(idioma == "ESP" or idioma == "NO"):
            return idioma

        print("Error: Idioma no válido")

def usar_nmap():
    #Versión mínima y segura de nmap: ejecuta `nmap -p <puertos> <target>` y muestra la salida.
    #Comprobar el idioma y definir los inputs
    if idioma == "ESP":
        target = input("Introduce host o red a escanear (ej: 192.168.1.1 o 192.168.1.0/24): ").strip()
        ports = input("Introduce puertos (ej: 22,80 o 1-1024) [default 1-1024]: ").strip() or "1-1024"
        running_msg = f"[+] Ejecutando: nmap -p {ports} {target}"
        err_prefix = "Error al ejecutar nmap:"
    else:
        #Noruego
        target = input("Oppgi vert eller nettverk som skal skannes (f.eks. 192.168.1.1 eller 192.168.1.0/24): ").strip()
        ports = input("Oppgi porter (f.eks. 22,80 eller 1-1024) [standard 1-1024]: ").strip() or "1-1024"
        running_msg = f"[+] Kjører: nmap -p {ports} {target}"
        err_prefix = "Feil ved kjøring av nmap:"

    #Verificación de errores
    if not target:
        if idioma == "ESP":
            print("Error: target no puede estar vacío")
        else:
            print("Feil: mål kan ikke være tomt")
        return

    print(running_msg)
    try:
        proc = subprocess.run(["nmap", "-p", ports, target],
                              check=True,
                              text=True,
                              capture_output=True)
        # Imprimir salida estándar de nmap
        print(proc.stdout)

    except FileNotFoundError:
        # nmap no está instalado o no en PATH
        if idioma == "ESP":
            print("Error: nmap no encontrado. Instálalo con apt install nmap")
        else:
            print("Feil: nmap ikke funnet. Installer med apt install nmap")
    except subprocess.CalledProcessError as e:
        print(f"{err_prefix} (exit {e.returncode})")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)
    except Exception as e:
        print(f"{err_prefix} {e}")

#Ping sweep
def usar_pingsweep():
    #Versión mínima: acepta una única IP, hace 1 ping y muestra si responde.
    
    #Comprobar el idioma y definir los inputs
    if idioma == "ESP":
        prompt = "Introduce una IP (ej: 192.168.1.10): "
        empty_err = "Error: target no puede estar vacío"
        invalid_err = "Error: IP no válida"
        ping_not_found = "Error: comando ping no encontrado en el sistema"
        yes = "Host responde:"
        no = "No responde:"
    else:
        #Noruego
        prompt = "Oppgi en IP (f.eks. 192.168.1.10): "
        empty_err = "Feil: mål kan ikke være tomt"
        invalid_err = "Feil: ugyldig IP"
        ping_not_found = "Feil: ping-kommandoen ble ikke funnet på systemet"
        yes = "Vert svarer:"
        no = "Svarer ikke:"

    target = input(prompt).strip()
    if not target:
        print(empty_err)
        return

    # Validar IP simple
    try:
        ipaddress.ip_address(target)
    except Exception:
        print(invalid_err)
        return

    # Comando ping básico según plataforma
    if sys.platform.startswith("win"):
        cmd = ["ping", "-n", "1", target]
    else:
        cmd = ["ping", "-c", "1", target]

    try:
        proc = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=2)
        if proc.returncode == 0:
            print(f"{yes} {target}")
        else:
            print(f"{no} {target}")
    except FileNotFoundError:
        print(ping_not_found)
    except subprocess.TimeoutExpired:
        print(f"{no} {target}")
    except Exception:
        print(f"{no} {target}")

#Calcular sha256 de un archivo
def calcular_sha256():
    #Pide la ruta de un archivo, calcula su SHA-256 leyendo por bloques
    #(para soportar archivos grandes) y muestra el hash en hexadecimal.
    
    #Comprobar idiomas
    if idioma == "ESP":
        prompt = "Introduce la ruta del archivo para calcular su SHA-256: "
        empty_err = "Error: ruta no puede estar vacía"
        not_found = "Error: archivo no encontrado"
        perm_err = "Error: permiso denegado al leer el archivo"
        read_err = "Error al leer el archivo:"
        result_msg = "SHA-256:"
    else:
        #Noruego
        prompt = "Oppgi filstien for å beregne SHA-256: "
        empty_err = "Feil: sti kan ikke være tom"
        not_found = "Feil: fil ikke funnet"
        perm_err = "Feil: tilgang nektet ved lesing av filen"
        read_err = "Feil ved lesing av filen:"
        result_msg = "SHA-256:"
    
    path = input(prompt).strip()
    if not path:
        print(empty_err)
        return

    try:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            # Leer en bloques de 64 KiB
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        print(f"{result_msg} {h.hexdigest()}")
    except FileNotFoundError:
        print(not_found)
    except PermissionError:
        print(perm_err)
    except Exception as e:
        print(f"{read_err} {e}")


#Main
idioma = elegir_idioma()
menu_inicial()
herramienta = input_opcion()

if(herramienta == 1):
    #Usar nmap
    usar_nmap()
elif(herramienta == 2):
    #Usar pingsweep
    usar_pingsweep()
elif(herramienta == 3):
    #Calcular sha256 de un archivo
    calcular_sha256()

