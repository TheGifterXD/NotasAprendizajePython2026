registros = {


}
categorias = {"item", "cantidad",}
historial_acciones = []

def agregar_item(item, cantidad):
    try:
        if not isinstance(item, str):
            raise TypeError("El item debe ser un texto")
        cantidad = int(cantidad)
        registros[item] = cantidad
        print(f"El item '{item}' ha sido agregado con la cantidad de: {cantidad} unidades")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return
    registros[item] = cantidad
    print(f"El item '{item}' ha sido agregado con la cantidad de: {cantidad} unidades")

def listar_stock():
    if registros:
        print("El stock actual es:")
        for item, cantidad in registros.items():
            print(f"{item}: {cantidad} unidades")
    else:
        print("No hay stock registrado.")

while True:
    opcion = input("Seleccione una opción:\n1. Agregar item\n2. Listar el stock\n3. Salir\n> ")
    
    if opcion == "1":
        item = input('De que tipo es el item desea agregar?: ')
        cantidad = input('Ingrese el valor: ')
        agregar_item(item, cantidad)

    elif opcion == "2":
        listar_stock()

    elif opcion == "3":
        break
