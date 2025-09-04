def es_letra(ch):
    return ('A' <= ch <= 'Z') or ('a' <= ch <= 'z')

def es_digito(ch):
    return '0' <= ch <= '9'

def clase_simbolo(ch):
    if es_letra(ch):
        return "letra"
    elif es_digito(ch):
        return "digito"
    else:
        return "otro"

def cargar_afd(archivo_estados):
    transiciones = {}
    aceptacion = set()

    with open(archivo_estados, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            if linea.startswith("aceptacion:"):
                _, estados = linea.split(":")
                aceptacion = set(e.strip() for e in estados.split(","))
                continue
            partes = linea.split(";")
            if len(partes) == 3:
                estado, simbolo, destino = partes
                estado, simbolo, destino = estado.strip(), simbolo.strip(), destino.strip()
                transiciones.setdefault(estado, {})[simbolo] = destino
    return transiciones, aceptacion

def afd_eval(cadena, transiciones, aceptacion, inicial="q0", error="q_err"):
    estado = inicial
    if cadena == "":
        return False  # cadena vacía no es válida
    for ch in cadena:
        simbolo = clase_simbolo(ch)
        estado = transiciones.get(estado, {}).get(simbolo, error)
    return estado in aceptacion

if __name__ == "__main__":
    trans, acept = cargar_afd("estados.txt")

    with open("cadenas.txt", "r", encoding="utf-8") as f:
        for raw in f:
            cadena = raw.strip()
            if not cadena:
                continue
            resultado = afd_eval(cadena, trans, acept)
            print(f"{cadena!r} = {'ACEPTADA' if resultado else 'RECHAZADA'}")
