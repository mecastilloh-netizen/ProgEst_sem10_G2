"""
Resuelve en Python. No uses clases ni bibliotecas que implementen listas enlazadas.
Comprueba cada solución con una lista vacía, un solo nodo y varios nodos cuando corresponda.

Crea buscar(dato), que devuelva True si existe y False si no existe.
Compara el recorrido desde cabeza con el recorrido desde cola.
"""
def crear_nodo(dato):
    return {"dato": dato,
            "siguiente": None,
            "anterior": None}

def buscar_desde_cabeza(cabeza, dato):
    actual = cabeza

    while actual is not None:
        if actual["dato"] == dato:
            return True

        actual = actual["siguiente"]
    return False

def buscar_desde_cola(cola, dato):
    actual = cola

    while actual is not None:
        if actual["dato"] == dato:
            return True
        actual = actual["anterior"]

    return False

def buscar(cabeza, dato):
    return buscar_desde_cabeza(cabeza, dato)

nodo1 = crear_nodo(10)
nodo2 = crear_nodo(20)
nodo3 = crear_nodo(30)

nodo1["siguiente"] = nodo2
nodo2["anterior"] = nodo1

nodo2["siguiente"] = nodo3
nodo3["anterior"] = nodo2

cabeza = nodo1
cola = nodo3

print(buscar(cabeza, 20))
print(buscar_desde_cola(cola, 20))
print(buscar(cabeza, 50))