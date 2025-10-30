# ---- VIZOR: Herramienta para red team ---- #

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



idioma = elegir_idioma()
menu_inicial()
herramienta = input_opcion()

