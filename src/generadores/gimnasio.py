"""Generador de base de datos para un gimnasio."""

import sqlite3
import random
from datetime import datetime, timedelta
from pathlib import Path
from faker import Faker

fake = Faker("es_ES")


def crear_base_datos():
    """Crea la base de datos del gimnasio con datos ficticios."""
    db_path = Path(__file__).parent.parent.parent / "data" / "gimnasio.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Crear tablas
    cursor.execute("""
        CREATE TABLE miembros (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            genero TEXT NOT NULL,
            fecha_inscripcion DATE NOT NULL,
            tipo_membresia TEXT NOT NULL,
            activo INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE clases (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            instructor TEXT NOT NULL,
            horario TEXT NOT NULL,
            capacidad_maxima INTEGER NOT NULL,
            duracion_minutos INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE asistencias (
            id INTEGER PRIMARY KEY,
            miembro_id INTEGER NOT NULL,
            clase_id INTEGER NOT NULL,
            fecha DATE NOT NULL,
            calificacion INTEGER,
            FOREIGN KEY (miembro_id) REFERENCES miembros(id),
            FOREIGN KEY (clase_id) REFERENCES clases(id)
        )
    """)

    # Insertar miembros
    tipos_membresia = ["Basica", "Premium", "VIP"]
    generos = ["M", "F"]

    miembros = []
    for i in range(1, 151):
        nombre = fake.name()
        edad = random.randint(18, 65)
        genero = random.choice(generos)
        fecha_inscripcion = fake.date_between(start_date="-3y", end_date="today")
        tipo_membresia = random.choice(tipos_membresia)
        activo = random.choices([1, 0], weights=[85, 15])[0]
        miembros.append((i, nombre, edad, genero, fecha_inscripcion, tipo_membresia, activo))

    cursor.executemany(
        "INSERT INTO miembros VALUES (?, ?, ?, ?, ?, ?, ?)", miembros
    )

    # Insertar clases
    clases_info = [
        ("Spinning", "08:00"),
        ("Yoga", "09:00"),
        ("CrossFit", "10:00"),
        ("Pilates", "11:00"),
        ("Zumba", "12:00"),
        ("Boxeo", "16:00"),
        ("Aerobicos", "17:00"),
        ("Funcional", "18:00"),
        ("Natacion", "19:00"),
        ("Pesas", "20:00"),
    ]

    clases = []
    for i, (nombre, horario) in enumerate(clases_info, 1):
        instructor = fake.name()
        capacidad = random.choice([15, 20, 25, 30])
        duracion = random.choice([45, 60, 90])
        clases.append((i, nombre, instructor, horario, capacidad, duracion))

    cursor.executemany(
        "INSERT INTO clases VALUES (?, ?, ?, ?, ?, ?)", clases
    )

    # Insertar asistencias
    asistencias = []
    miembros_activos = [m[0] for m in miembros if m[6] == 1]

    for i in range(1, 501):
        miembro_id = random.choice(miembros_activos)
        clase_id = random.randint(1, 10)
        fecha = fake.date_between(start_date="-6m", end_date="today")
        calificacion = random.choices(
            [None, 1, 2, 3, 4, 5],
            weights=[20, 5, 10, 20, 30, 15]
        )[0]
        asistencias.append((i, miembro_id, clase_id, fecha, calificacion))

    cursor.executemany(
        "INSERT INTO asistencias VALUES (?, ?, ?, ?, ?)", asistencias
    )

    conn.commit()
    conn.close()
    print(f"Base de datos creada: {db_path}")


if __name__ == "__main__":
    crear_base_datos()
