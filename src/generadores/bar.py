"""Generador de base de datos para un bar."""

import sqlite3
import random
from datetime import datetime, timedelta
from pathlib import Path
from faker import Faker

fake = Faker("es_ES")


def crear_base_datos():
    """Crea la base de datos del bar con datos ficticios."""
    db_path = Path(__file__).parent.parent.parent / "data" / "bar.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Crear tablas
    cursor.execute("""
        CREATE TABLE bartenders (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            experiencia_anios INTEGER NOT NULL,
            turno TEXT NOT NULL,
            especialidad TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE bebidas (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL,
            contenido_alcoholico REAL NOT NULL,
            disponible INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE ventas (
            id INTEGER PRIMARY KEY,
            bebida_id INTEGER NOT NULL,
            bartender_id INTEGER NOT NULL,
            fecha DATE NOT NULL,
            cantidad INTEGER NOT NULL,
            hora TEXT NOT NULL,
            FOREIGN KEY (bebida_id) REFERENCES bebidas(id),
            FOREIGN KEY (bartender_id) REFERENCES bartenders(id)
        )
    """)

    # Insertar bartenders
    turnos = ["Tarde", "Noche", "Madrugada"]
    especialidades = ["Cocteles clasicos", "Cocteles modernos", "Cerveza artesanal", "Vinos", "Mixologia molecular"]

    bartenders = []
    for i in range(1, 13):
        nombre = fake.name()
        experiencia_anios = random.randint(1, 15)
        turno = random.choice(turnos)
        especialidad = random.choice(especialidades)
        bartenders.append((i, nombre, experiencia_anios, turno, especialidad))

    cursor.executemany(
        "INSERT INTO bartenders VALUES (?, ?, ?, ?, ?)", bartenders
    )

    # Insertar bebidas
    bebidas_info = [
        ("Cerveza Lager", "Cerveza", 5.50, 4.5),
        ("Cerveza IPA", "Cerveza", 7.00, 6.5),
        ("Cerveza Stout", "Cerveza", 6.50, 5.5),
        ("Mojito", "Coctel", 9.00, 12.0),
        ("Margarita", "Coctel", 10.00, 15.0),
        ("Pina Colada", "Coctel", 9.50, 13.0),
        ("Daiquiri", "Coctel", 8.50, 14.0),
        ("Whisky", "Destilado", 12.00, 40.0),
        ("Vodka", "Destilado", 8.00, 40.0),
        ("Ron", "Destilado", 7.50, 37.5),
        ("Tequila", "Destilado", 9.00, 38.0),
        ("Gin Tonic", "Coctel", 10.50, 15.0),
        ("Vino Tinto", "Vino", 6.00, 13.5),
        ("Vino Blanco", "Vino", 5.50, 12.0),
        ("Sangria", "Vino", 7.00, 11.0),
        ("Agua", "Sin alcohol", 2.00, 0.0),
        ("Refresco", "Sin alcohol", 3.00, 0.0),
        ("Zumo Natural", "Sin alcohol", 4.00, 0.0),
        ("Caipirinha", "Coctel", 9.00, 14.0),
        ("Cosmopolitan", "Coctel", 11.00, 16.0),
    ]

    bebidas = []
    for i, (nombre, categoria, precio, alcohol) in enumerate(bebidas_info, 1):
        disponible = random.choices([1, 0], weights=[90, 10])[0]
        bebidas.append((i, nombre, categoria, precio, alcohol, disponible))

    cursor.executemany(
        "INSERT INTO bebidas VALUES (?, ?, ?, ?, ?, ?)", bebidas
    )

    # Insertar ventas
    horas = [f"{h:02d}:00" for h in range(18, 24)] + [f"{h:02d}:00" for h in range(0, 4)]

    ventas = []
    for i in range(1, 601):
        bebida_id = random.randint(1, 20)
        bartender_id = random.randint(1, 12)
        fecha = fake.date_between(start_date="-6m", end_date="today")
        cantidad = random.choices([1, 2, 3, 4, 5], weights=[50, 30, 12, 5, 3])[0]
        hora = random.choice(horas)
        ventas.append((i, bebida_id, bartender_id, fecha, cantidad, hora))

    cursor.executemany(
        "INSERT INTO ventas VALUES (?, ?, ?, ?, ?, ?)", ventas
    )

    conn.commit()
    conn.close()
    print(f"Base de datos creada: {db_path}")


if __name__ == "__main__":
    crear_base_datos()
