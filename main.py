# Fase 1

# 1 Establecer variables

b5: int = 5
b10: int = 10
b20: int = 20
b50: int = 50
b100: int = 100
b200: int = 200
b500: int = 500

precio_total = 0

seguirPidiendo = True

# 2 Arrays
menu = []
precio_plato = []
comanda = []

# Llenado de datos
for i in range(3):
    plato = input("Introduce un plato en el menú: ")
    precio = int(input("Introduce el precio de " + plato + ": "))

    menu.append(plato)
    precio_plato.append(precio)

# pendiente: mostrar carta al usuario

# Elegir comida
while(seguirPidiendo):
    peticion = input("Qué quieres comer?: ")
    if peticion in menu:
        comanda.append(peticion)
    else:
        print("No tenemos ese plato!")

    print(comanda)

    terminar = input("Has terminado de pedir(1= SI / 0= NO): ")

    if (terminar == "1"):
        seguirPidiendo = False
    else:
        seguirPidiendo = True

# Cobrar
for plato in comanda:
    i = 0
    for item in menu:
        if plato == item:
            precio_total += precio_plato[i]
        i += 1

print(f'Factura: {precio_total}€')