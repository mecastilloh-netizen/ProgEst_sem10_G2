def crear_nodo(dato):
    return {"dato": dato, "siguiente": None}

def insertar_inicio(cabeza, dato):
    nuevo = crear_nodo(dato)
    nuevo["siguiente"] = cabeza
    return nuevo

def insertar_final(cabeza, dato):
    nuevo = crear_nodo(dato)
    if cabeza is None:
        return nuevo
    actual = cabeza
    while actual["siguiente"] is not None:
        actual = actual["siguiente"]
    actual["siguiente"] = nuevo
    return cabeza

def mostrar(cabeza):
    actual = cabeza
    while actual is not None:
        print(actual["dato"], end=" → ")
        actual = actual["siguiente"]
    print("None")

def buscar(cabeza, dato):
    actual = cabeza
    posicion = 0
    while actual is not None:
        if actual["dato"] == dato:
            return posicion
        actual = actual["siguiente"]
        posicion += 1
    return -1

def eliminar(cabeza, dato):
    if cabeza is None:
        return None, False
    if cabeza["dato"] == dato:
        return cabeza["siguiente"], True
    anterior = cabeza
    actual = cabeza["siguiente"]
    while actual is not None:
        if actual["dato"] == dato:
            anterior["siguiente"] = actual["siguiente"]
            return cabeza, True
        anterior = actual
        actual = actual["siguiente"]
    return cabeza, False

def contar(cabeza):
    total = 0
    actual = cabeza
    while actual is not None:
        total += 1
        actual = actual["siguiente"]
    return total

def atender(cabeza):
    if cabeza is None:
        return None, None

    nombre = cabeza["dato"]
    cabeza = cabeza["siguiente"]
    return cabeza, nombre

def insertar_despues(cabeza, referente, nombre):
    actual = cabeza

    while actual is not None:
        if actual["dato"] == referente:
            nuevo = crear_nodo(nombre)
            nuevo["siguiente"] = actual["siguiente"]
            actual["siguiente"] = nuevo
            return cabeza, True

        actual = actual["siguiente"]

    return cabeza, False

def invertir(cabeza):
    anterior = None
    actual = cabeza

    while actual is not None:
        siguiente = actual["siguiente"]
        actual["siguiente"] = anterior
        anterior = actual
        actual = siguiente

    return anterior

def menu():
    cabeza = None
    while True:
        print("\n1. Agregar turno  2. Mostrar  3. Buscar")
        print("4. Eliminar turno  5. Contar  6. Atender turno")
        print("7. Insertar después  8. Invertir lista  0. Salir")

        opcion = input("Opción: ").strip()

        if opcion == "0":
            break

        if opcion in ("1", "3", "4"):
            nombre = input("Nombre: ").strip()
            if not nombre:
                print("Escriba un nombre.")
                continue

        if opcion == "1":
            cabeza = insertar_final(cabeza, nombre)
            print("Turno agregado")

        elif opcion == "2":
            mostrar(cabeza)

        elif opcion == "3":
            posicion = buscar(cabeza, nombre)
            if posicion == -1:
                print("No encontrado")
            else:
                print("Posición:", posicion)

        elif opcion == "4":
            cabeza, eliminado = eliminar(cabeza, nombre)
            print("Eliminado" if eliminado else "No encontrado")

        elif opcion == "5":
            print("Total:", contar(cabeza))

        elif opcion == "6":
            cabeza, nombre = atender(cabeza)
            if nombre is None:
                print("No hay turnos pendientes")
            else:
                print("Turno atendido:", nombre)

        elif opcion == "7":
            referente = input("Insertar después de: ").strip()
            nombre = input("Nombre nuevo: ").strip()

            if not referente or not nombre:
                print("Escriba los nombres.")
                continue

            cabeza, insertado = insertar_despues(cabeza, referente, nombre)

            if insertado:
                print("Turno insertado")
            else:
                print("No se encontró a", referente)

        elif opcion == "8":
            cabeza = invertir(cabeza)
            print("Lista invertida")
            mostrar(cabeza)

        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()