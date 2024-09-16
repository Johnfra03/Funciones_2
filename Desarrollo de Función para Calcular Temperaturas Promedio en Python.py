def calcular_promedio_temperaturas(ciudades, ciudad_elegida):
    # Verifica si la ciudad elegida es válida
    if ciudad_elegida < 1 or ciudad_elegida > len(ciudades):
        print("Número de ciudad no válido.")
        return

    # Obtiene la ciudad correspondiente a la elección del usuario
    ciudad = ciudades[ciudad_elegida - 1]
    suma_temperaturas_ciudad = 0  # Acumulador para la suma de las temperaturas de la ciudad
    total_dias = 0  # Contador de los días totales

    # Recorre cada semana de la ciudad
    for semana in ciudad:
        # Recorre cada día de la semana y suma la temperatura
        for dia in semana:
            suma_temperaturas_ciudad += dia['temp']
            total_dias += 1  # Incrementa el número de días

    # Calcula el promedio dividiendo la suma total de las temperaturas por el número de días
    promedio_ciudad = suma_temperaturas_ciudad / total_dias
    print(f"Promedio de temperatura para Ciudad {ciudad_elegida}: {promedio_ciudad:.2f}°F")

    return promedio_ciudad  # Retorna el promedio de la ciudad seleccionada


# Datos de ejemplo: 3 ciudades durante 4 semanas (valores de temperatura modificados)
nuevas_temperaturas = [
    [
        [{"dia": "Lunes", "temp": 75}, {"dia": "Martes", "temp": 77}, {"dia": "Miércoles", "temp": 80},
         {"dia": "Jueves", "temp": 82}, {"dia": "Viernes", "temp": 84}, {"dia": "Sábado", "temp": 86},
         {"dia": "Domingo", "temp": 85}],
        [{"dia": "Lunes", "temp": 74}, {"dia": "Martes", "temp": 76}, {"dia": "Miércoles", "temp": 79},
         {"dia": "Jueves", "temp": 81}, {"dia": "Viernes", "temp": 83}, {"dia": "Sábado", "temp": 87},
         {"dia": "Domingo", "temp": 88}],
        [{"dia": "Lunes", "temp": 76}, {"dia": "Martes", "temp": 78}, {"dia": "Miércoles", "temp": 81},
         {"dia": "Jueves", "temp": 83}, {"dia": "Viernes", "temp": 85}, {"dia": "Sábado", "temp": 89},
         {"dia": "Domingo", "temp": 90}],
        [{"dia": "Lunes", "temp": 78}, {"dia": "Martes", "temp": 80}, {"dia": "Miércoles", "temp": 82},
         {"dia": "Jueves", "temp": 84}, {"dia": "Viernes", "temp": 86}, {"dia": "Sábado", "temp": 88},
         {"dia": "Domingo", "temp": 89}]
    ],
    [
        [{"dia": "Lunes", "temp": 65}, {"dia": "Martes", "temp": 67}, {"dia": "Miércoles", "temp": 70},
         {"dia": "Jueves", "temp": 72}, {"dia": "Viernes", "temp": 75}, {"dia": "Sábado", "temp": 78},
         {"dia": "Domingo", "temp": 80}],
        [{"dia": "Lunes", "temp": 66}, {"dia": "Martes", "temp": 68}, {"dia": "Miércoles", "temp": 71},
         {"dia": "Jueves", "temp": 74}, {"dia": "Viernes", "temp": 77}, {"dia": "Sábado", "temp": 79},
         {"dia": "Domingo", "temp": 82}],
        [{"dia": "Lunes", "temp": 64}, {"dia": "Martes", "temp": 66}, {"dia": "Miércoles", "temp": 69},
         {"dia": "Jueves", "temp": 73}, {"dia": "Viernes", "temp": 76}, {"dia": "Sábado", "temp": 78},
         {"dia": "Domingo", "temp": 81}],
        [{"dia": "Lunes", "temp": 67}, {"dia": "Martes", "temp": 69}, {"dia": "Miércoles", "temp": 72},
         {"dia": "Jueves", "temp": 75}, {"dia": "Viernes", "temp": 78}, {"dia": "Sábado", "temp": 80},
         {"dia": "Domingo", "temp": 83}]
    ],
    [
        [{"dia": "Lunes", "temp": 95}, {"dia": "Martes", "temp": 97}, {"dia": "Miércoles", "temp": 99},
         {"dia": "Jueves", "temp": 101}, {"dia": "Viernes", "temp": 100}, {"dia": "Sábado", "temp": 98},
         {"dia": "Domingo", "temp": 97}],
        [{"dia": "Lunes", "temp": 96}, {"dia": "Martes", "temp": 98}, {"dia": "Miércoles", "temp": 100},
         {"dia": "Jueves", "temp": 102}, {"dia": "Viernes", "temp": 99}, {"dia": "Sábado", "temp": 97},
         {"dia": "Domingo", "temp": 95}],
        [{"dia": "Lunes", "temp": 97}, {"dia": "Martes", "temp": 99}, {"dia": "Miércoles", "temp": 101},
         {"dia": "Jueves", "temp": 103}, {"dia": "Viernes", "temp": 98}, {"dia": "Sábado", "temp": 96},
         {"dia": "Domingo", "temp": 94}],
        [{"dia": "Lunes", "temp": 98}, {"dia": "Martes", "temp": 100}, {"dia": "Miércoles", "temp": 102},
         {"dia": "Jueves", "temp": 104}, {"dia": "Viernes", "temp": 99}, {"dia": "Sábado", "temp": 97},
         {"dia": "Domingo", "temp": 95}]
    ]
]


def main():
    while True:
        # Solicita al usuario que elija la ciudad
        try:
            ciudad_elegida = int(input("Elige una ciudad (1, 2 o 3) o 0 para salir: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if ciudad_elegida == 0:
            print("Saliendo del programa.")
            break

        # Llama a la función con la ciudad elegida
        calcular_promedio_temperaturas(nuevas_temperaturas, ciudad_elegida)


# Llama a la función principal
main()
