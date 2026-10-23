def crear_nodo(dato):
    return {
        "dato": dato,
        "anterior": None,
        "siguiente": None
    }

def crear_navegador():
    return {"actual": None}

def visitar(navegador, pagina):
    nuevo = crear_nodo(pagina)
    actual = navegador["actual"]

    if actual is not None:
        actual["siguiente"] = None
        nuevo["anterior"] = actual
        actual["siguiente"] = nuevo

    navegador["actual"] = nuevo

def retroceder(navegador):
    actual = navegador["actual"]

    if actual["anterior"] is None:
        return False

    navegador["actual"] = actual["anterior"]
    return True

def avanzar(navegador):
    actual = navegador["actual"]

    if actual is None:
        return False

    if actual["siguiente"] is None:
        return False

    navegador["actual"] = actual["siguiente"]
    return True

def mostrar_actual(navegador):
    actual = navegador["actual"]

    if actual is None:
        print("No hay ninguna pagina")
    else:
        print("Pagina actual:", actual["dato"])


def menu():
    navegador = crear_navegador()

    while True:
        print("\n1. Visitar pagina")
        print("2. Retroceder")
        print("3. Avanzar")
        print("4. Mostrar pagina actual")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            pagina = input("Nombre de la pagina: ")
            visitar(navegador, pagina)
            print("Pagina visitada")

        elif opcion == "2":
            if retroceder(navegador):
                mostrar_actual(navegador)
            else:
                print("No se puede retroceder")

        elif opcion == "3":
            if avanzar(navegador):
                mostrar_actual(navegador)
            else:
                print("No se puede avanzar")

        elif opcion == "4":
            mostrar_actual(navegador)

        elif opcion == "5":
            break

        else:
            print("Opcion incorrecta")


menu()