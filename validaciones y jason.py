import json
import re
import hashlib
import os

def validar_contrasena(password):
    # Validar: Mínimo 8 caracteres, 1 mayúscula, 1 minúscula, 1 número y 1 carácter especial
    patron = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return re.match(patron, password) is not None

def guardar_usuario(usuario, password):
    archivo = "usuarios.json"
    
    # 1. Validar la contraseña antes de procesarla
    if not validar_contrasena(password):
        print("Error: La contraseña debe tener al menos 8 caracteres, una mayúscula, un número y un símbolo.")
        return

    # 2. Hashear la contraseña por seguridad
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    nuevo_usuario = {"usuario": usuario, "password": password_hash}

    # 3. Leer la base de datos JSON si ya existe para no sobrescribir datos
    datos = []
    if os.path.exists(archivo):
        with open(archivo, "r") as file:
            try:
                datos = json.load(file)
            except json.JSONDecodeError:
                datos = [] # Por si el archivo está vacío o corrupto

    # 4. Agregar el nuevo registro y guardar
    datos.append(nuevo_usuario)
    with open(archivo, "w") as file:
        json.dump(datos, file, indent=4)
    
    print(f"Usuario '{usuario}' registrado correctamente en la base JSON.")

# Prueba del código
guardar_usuario("josias_hazael", "Uade2026!Backend")