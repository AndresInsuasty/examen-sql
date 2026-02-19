"""Generador de base de datos para un restaurante."""

import sqlite3
import random
from datetime import datetime, timedelta
from pathlib import Path
from faker import Faker

fake = Faker("es_ES")


def crear_base_datos():
    """Crea la base de datos del restaurante con datos ficticios."""
    db_path = Path(__file__).parent.parent.parent / "data" / "restaurante.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Crear tablas
    cursor.execute("""
        CREATE TABLE meseros (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            fecha_contratacion DATE NOT NULL,
            turno TEXT NOT NULL,
            salario REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE mesas (
            id INTEGER PRIMARY KEY,
            capacidad INTEGER NOT NULL,
            ubicacion TEXT NOT NULL,
            disponible INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE ordenes (
            id INTEGER PRIMARY KEY,
            mesa_id INTEGER NOT NULL,
            mesero_id INTEGER NOT NULL,
            fecha DATE NOT NULL,
            total REAL NOT NULL,
            propina REAL,
            num_comensales INTEGER NOT NULL,
            FOREIGN KEY (mesa_id) REFERENCES mesas(id),
            FOREIGN KEY (mesero_id) REFERENCES meseros(id)
        )
    """)

    # Insertar meseros
    turnos = ["Manana", "Tarde", "Noche"]
    meseros = []
    for i in range(1, 21):
        nombre = fake.name()
        fecha_contratacion = fake.date_between(start_date="-5y", end_date="-1m")
        turno = random.choice(turnos)
        salario = round(random.uniform(1200, 2500), 2)
        meseros.append((i, nombre, fecha_contratacion, turno, salario))

    cursor.executemany(
        "INSERT INTO meseros VALUES (?, ?, ?, ?, ?)", meseros
    )

    # Insertar mesas
    ubicaciones = ["Interior", "Terraza", "Barra", "VIP"]
    mesas = []
    for i in range(1, 26):
        capacidad = random.choice([2, 4, 6, 8])
        ubicacion = random.choice(ubicaciones)
        disponible = random.choices([1, 0], weights=[70, 30])[0]
        mesas.append((i, capacidad, ubicacion, disponible))

    cursor.executemany(
        "INSERT INTO mesas VALUES (?, ?, ?, ?)", mesas
    )

    # Insertar ordenes
    ordenes = []
    for i in range(1, 401):
        mesa_id = random.randint(1, 25)
        mesa_capacidad = mesas[mesa_id - 1][1]
        mesero_id = random.randint(1, 20)
        fecha = fake.date_between(start_date="-6m", end_date="today")
        total = round(random.uniform(25, 350), 2)
        propina = round(total * random.uniform(0, 0.20), 2) if random.random() > 0.1 else None
        num_comensales = random.randint(1, mesa_capacidad)
        ordenes.append((i, mesa_id, mesero_id, fecha, total, propina, num_comensales))

    cursor.executemany(
        "INSERT INTO ordenes VALUES (?, ?, ?, ?, ?, ?, ?)", ordenes
    )

    conn.commit()
    conn.close()
    print(f"Base de datos creada: {db_path}")


if __name__ == "__main__":
    crear_base_datos()
