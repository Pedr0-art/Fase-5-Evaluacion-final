# Nombre del estudiante: Pedro Martin Sanes Vergara
# Grupo: 2204
# Programa: Ingenieria Electronica
# Codigo Fuente: Autoria propia

#====================================================
# EJERCICIO:#5 EVALUACION FINAL
#====================================================


def evaluar_jornada(horas_dias):
    total_horas = sum(horas_dias)
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario estándar"
    return total_horas, clasificacion


def main():
    # [Nombre del recurso, Lunes, Martes, Miércoles, Jueves, Viernes]
    matriz_horas = [
        ["Ana Gómez", 8, 8, 8, 8, 8],
        ["Carlos Ruiz", 9, 9, 8, 9, 8],
        ["Laura Pérez", 7, 8, 8, 7, 6],
        ["Diego Torres", 10, 8, 8, 8, 7],
    ]

    print("--- Reporte semanal de jornada laboral ---")
    for fila in matriz_horas:
        nombre = fila[0]
        horas_semana = fila[1:]
        total, estado = evaluar_jornada(horas_semana)
        print(f"Recurso: {nombre} | Total horas: {total} | Jornada: {estado}")


if __name__ == "__main__":
    main()