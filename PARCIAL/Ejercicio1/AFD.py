def cargar_afd(archivo_estados):
    transiciones = {}
    aceptacion = set()

    with open(archivo_estados, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            if linea.startswith("aceptacion:"):
                _, estados = linea.split(":", 1)
                aceptacion = set(e.strip() for e in estados.split(",") if e.strip())
                continue
            partes = linea.split(";")
            if len(partes) != 3:
                continue
            estado, simbolo, destino = (p.strip() for p in partes)
            transiciones.setdefault(estado, {})[simbolo] = destino
    return transiciones, aceptacion

def afd_eval(cadena, transiciones, aceptacion, inicial="q0", error="q_err"):
    estado = inicial
    
    for s in cadena:
        estado = transiciones.get(estado, {}).get(s, error)
    return estado in aceptacion

if __name__ == "__main__":
    trans, acept = cargar_afd("estados.txt")
    with open("cadenas.txt", "r", encoding="utf-8") as f:
        for linea in f:
            if linea.lstrip().startswith("#"):
                continue  
            cadena = linea.rstrip("\n").strip()  
            display = "<vacía>" if cadena == "" else cadena
            resultado = afd_eval(cadena, trans, acept)
            print(f"{display!r} = {'ACEPTADA' if resultado else 'RECHAZADA'}")
