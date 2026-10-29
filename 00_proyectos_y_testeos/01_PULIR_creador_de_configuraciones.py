configuraciones = {}
categorias_permitidas = {"sistema", "usuario", "red"}
historial_acciones = []

def agregar_config(config_name, config_value):
    # Validamos si el nombre está permitido usando el conjunto
    if config_name not in categorias_permitidas:
        print(f"Error: '{config_name}' no es válido. Debe ser uno de: {categorias_permitidas}")
        return  # Salimos de la función si no es válido

    configuraciones[config_name] = config_value
    print(f"Configuración '{config_name}' agregada con valor: {config_value}")

def listar_configuraciones():
    if configuraciones:
        print("Configuraciones actuales:")
        for config_name, config_value in configuraciones.items():
            print(f"{config_name}: {config_value}")
    else:
        print("No hay configuraciones registradas.")

while True:
    opcion = input("Seleccione una opción:\n1. Agregar configuración\n2. Listar configuraciones\n3. Salir\n> ")
    
    if opcion == "1":
        config_name = input('Qué configuración desea agregar? (sistema, usuario, red): ')
        config_value = input('Ingrese el valor: ')
        agregar_config(config_name, config_value)

    elif opcion == "2":
        listar_configuraciones()

    elif opcion == "3":
        break
