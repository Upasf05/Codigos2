try:
    semestre = int(input("Ingrese número del semestre que actualmente cursa: ")) 
    if semestre >= 3:
       print("Ha avanzado mucho en su carrera universitaria.")
    else:
       print("Todavía esta comenzando su carrera universitaria") 
except ValueError:
    print("Ingresar un número, no letras.")       