#PENSAMIENTO COMPUTACIONAL
#FECHA:15/04/2024
#AUTOR: Luisa Sophia Valenzuela Sandoval 1343124
#AUTOR: Luis Carlos Valenzuela Sandoval  1318324
#Objetivos: Desarrollar un programa en Python que simule un sistema de cuidado de plantas. El objetivo es que los usuarios interactúen con el programa para gestionar el bienestar de sus plantas virtuales.
#Entrada: Solicita al usuario que introduzca información sobre su planta. Como mínimo debe Solicitar el tipo de planta (flor, árbol, arbusto, suculenta, helecho), el nombre de la planta, nivel inicial de agua, nivel inicial de nutrientes en la tierra.
#Procesos: Realizar las operaciones que corresponden a cada opcion del menu de la planta.
#Salida: Los mensajes indicando la cantidad de agua y nutrientes de la planta dependiendo la opcion que hayan seleccionado.
nom_planta= str(input("Ingrese el nombre de la planta: "))
tipo_planta = ""
opcion = 10 
while opcion != 5 : 
    print("---------- Seleccione el tipo de planta----------")
    print("1.Flor ")
    print("2.Arbol")
    print("3.Arbusto")
    print("4. Suculenta")
    print("5. Helecho")
    
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        print("Flor")
        tipo_planta ="Flor"
    elif opcion==2:
        print("Arbol")
        tipo_planta ="Arbol"
    elif opcion==3:
        print("Arbusto")
        tipo_planta ="Arbusto"
    elif opcion==4:
        print("Suculenta")
        tipo_planta ="Suculenta"
    elif opcion==5:
        print("Helecho")
        tipo_planta ="Helecho"
    else:
        print("Has seleccionado un número fuera del rango")

    agua = int(input("Ingrese el nivel de agua de la planta: "))
    nutrientes = int(input("Ingrese el nivel de nutrientes de la planta: "))


    Opcion = 0 
    while Opcion != 6 : 

        print("---------- MENÚ DE OPCIONES DE LA PLANTA ----------")
        print("1. Ver información")
        print("2. Regar planta")
        print("3. Asolear planta")
        print("4. Abonar planta")
        print("5. Paso del tiempo")
        print("6. Salir")

        Opcion = int(input("Seleccione una opción del menú: "))
        if Opcion == 1:
            print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print("HAS SELECCIONADO LA OPCION SOBRE INFORMACIÓN DE LA PLANTA:")
            print("Nombre de la planta : ", nom_planta)
            print("Tipo de planta: ", tipo_planta)
            print("Nivel inicial de agua: ", agua)
            print("Nivel de nutrientes de la tierra: ", nutrientes)
            print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        elif Opcion==2:
            print("HAS SELECCIONADO LA OPCION DE REGAR PLANTA")
            if agua == 0: 
                cant=agua * 0.10  #cant = aumento 
                agua = agua + cant 
                print("El nivel de agua actual de su planta es: ", agua)  
            else:
                cant= agua * 0.10 #cant= aumento 
                agua = agua + cant
                print("El nivel de agua actual de su planta es: ", agua)
        elif Opcion ==3:
            print("HAS SELECCIONADO LA OPCION DE ASOLEAR PLANTA:")
            if agua < 0.08:
                print("No es posible asolear la planta debido al nivel actual de agua, se recomienda regar la planta")
            else:
                agua>0.08
                dism= agua *0.08         # dism = CANTIDAD A DISMINUIR
                agua = agua - dism
                print("El nivel de agua de la planta es: ", agua)
        elif Opcion == 4: 
            print("HAS SELECCIONADO LA OPCION DE ABONAR PLANTA:")
            if nutrientes >500: 
                print("No es posible duplicar los nutrientes: El nivel de nutrientes actual es: ", nutrientes)
            else :
                nutrientes<500
                nutrientes = nutrientes * 2
                print("El nivel de nutrientes actual es: ", nutrientes)
        elif Opcion == 5: 
            print("HAS SELECCIONADO LA OPCION SOBRE EL PASO DEL TIEMPO:")
            horas = int(input("Ingrese el número de horas que desea simular: "))
            cont=0
            while cont<horas:
                agua=agua*0.05
                nutrientes=nutrientes-50
                cont=cont+1
            print("El porcentaje de agua despues de" , horas, "horas es :", agua)
            print("El porcentaje de nutrientes despues de  ",horas, "horas es :", nutrientes)
        elif Opcion == 6: 
            print("¡Gracias por usar el programa :)!")
