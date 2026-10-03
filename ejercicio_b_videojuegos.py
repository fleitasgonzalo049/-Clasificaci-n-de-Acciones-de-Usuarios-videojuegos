# Actividad b - Clasificación de acciones de usuarios
# Plataforma de videojuegos

datos = [
    {"usuario": "user01", "accion": "Combate", "duracion": 120, "resultado": "Victoria"},
    {"usuario": "user02", "accion": "Exploración", "duracion": 300, "resultado": "Descubrimiento"},
    {"usuario": "user03", "accion": "Interacción social", "duracion": 180, "resultado": "Mensaje enviado"},
    {"usuario": "user04", "accion": "Combate", "duracion": 90, "resultado": "Derrota"},
    {"usuario": "user05", "accion": "Exploración", "duracion": 240, "resultado": "Sin hallazgos"}
]

def clasificar_accion(usuario):
    accion = usuario["accion"]
    resultado = usuario["resultado"]

    if accion == "Combate" and resultado == "Victoria":
        return "Combate exitoso"
    elif accion == "Combate" and resultado == "Derrota":
        return "Combate fallido"
    elif accion == "Exploración" and resultado == "Descubrimiento":
        return "Exploración exitosa"
    elif accion == "Exploración" and resultado == "Sin hallazgos":
        return "Exploración sin resultado"
    elif accion == "Interacción social":
        return "Interacción social"

    return "Acción no clasificada"


print("CLASIFICACIÓN DE ACCIONES")
print("-" * 50)

for usuario in datos:
    categoria = clasificar_accion(usuario)
    print(
        f'{usuario["usuario"]}: '
        f'{usuario["accion"]} - '
        f'{usuario["duracion"]} segundos - '
        f'{usuario["resultado"]} -> '
        f'{categoria}'
    )
