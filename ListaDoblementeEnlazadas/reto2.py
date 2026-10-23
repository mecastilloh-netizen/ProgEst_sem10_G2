"""
Implementa insertar_despues(referencia, dato). Si referencia no existe, devuelve False; si existe, inserta el nuevo nodo y devuelve True.
Pregunta: ¿Cómo cambia cola si insertas después del último nodo?
"""

def crear_nodo(dato):
    return {
        "dato": dato,
        "siguiente": None,
        "anterior": None
    }

def insertar_despues(lista, referencia, dato):
    actual = lista["cabeza"]

    while actual is not None:
        if actual["dato"] == referencia:
            nuevo = crear_nodo(dato)

            nuevo["anterior"] = actual
            nuevo["siguiente"] = actual["siguiente"]

            if actual["siguiente"] is not None:
                actual["siguiente"]["anterior"] = nuevo
            else:
                lista["cola"] = nuevo

            actual["siguiente"] = nuevo

            return True

        actual = actual["siguiente"]

    return False


def mostrar(cabeza):
    actual = cabeza

    while actual is not None:
        print(actual["dato"], end=" <-> ")
        actual = actual["siguiente"]
    print("None")


nodo1 = crear_nodo(10)
nodo2 = crear_nodo(20)

nodo1["siguiente"] = nodo2
nodo2["anterior"] = nodo1

lista = {
    "cabeza": nodo1,
    "cola": nodo2
}

print(insertar_despues(lista, 10, 15))
mostrar(lista["cabeza"])

print(insertar_despues(lista, 20, 30))
mostrar(lista["cabeza"])

print(insertar_despues(lista, 50, 40))