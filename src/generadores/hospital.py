"""Generador de base de datos para un hospital."""

import sqlite3
import random
from datetime import datetime, timedelta
from pathlib import Path
from faker import Faker

fake = Faker("es_ES")


def crear_base_datos():
    """Crea la base de datos del hospital con datos ficticios."""
    db_path = Path(__file__).parent.parent.parent / "data" / "hospital.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Crear tablas
    cursor.execute("""
        CREATE TABLE pacientes (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            genero TEXT NOT NULL,
            tipo_sangre TEXT NOT NULL,
            fecha_registro DATE NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE doctores (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            especialidad TEXT NOT NULL,
            anios_experiencia INTEGER NOT NULL,
            consultorio TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE consultas (
            id INTEGER PRIMARY KEY,
            paciente_id INTEGER NOT NULL,
            doctor_id INTEGER NOT NULL,
            fecha DATE NOT NULL,
            diagnostico TEXT NOT NULL,
            costo REAL NOT NULL,
            FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
            FOREIGN KEY (doctor_id) REFERENCES doctores(id)
        )
    """)

    # Insertar pacientes
    tipos_sangre = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    generos = ["M", "F"]

    pacientes = []
    for i in range(1, 201):
        nombre = fake.name()
        edad = random.randint(1, 90)
        genero = random.choice(generos)
        tipo_sangre = random.choices(
            tipos_sangre,
            weights=[35, 6, 8, 2, 3, 1, 38, 7]
        )[0]
        fecha_registro = fake.date_between(start_date="-5y", end_date="today")
        pacientes.append((i, nombre, edad, genero, tipo_sangre, fecha_registro))

    cursor.executemany(
        "INSERT INTO pacientes VALUES (?, ?, ?, ?, ?, ?)", pacientes
    )

    # Insertar doctores
    especialidades = [
        "Medicina General", "Pediatria", "Cardiologia", "Dermatologia",
        "Traumatologia", "Neurologia", "Ginecologia", "Oftalmologia",
        "Otorrinolaringologia", "Psiquiatria"
    ]

    doctores = []
    for i in range(1, 16):
        nombre = "Dr. " + fake.name()
        especialidad = random.choice(especialidades)
        anios_experiencia = random.randint(2, 30)
        consultorio = f"{random.randint(1, 5)}{random.randint(0, 9):02d}"
        doctores.append((i, nombre, especialidad, anios_experiencia, consultorio))

    cursor.executemany(
        "INSERT INTO doctores VALUES (?, ?, ?, ?, ?)", doctores
    )

    # Insertar consultas
    diagnosticos = [
        "Gripe comun", "Hipertension", "Diabetes tipo 2", "Migrania",
        "Alergia estacional", "Infeccion urinaria", "Gastritis",
        "Lumbalgia", "Ansiedad", "Conjuntivitis", "Otitis",
        "Bronquitis", "Dermatitis", "Esguince", "Control rutinario"
    ]

    consultas = []
    for i in range(1, 501):
        paciente_id = random.randint(1, 200)
        doctor_id = random.randint(1, 15)
        fecha = fake.date_between(start_date="-1y", end_date="today")
        diagnostico = random.choice(diagnosticos)
        costo = round(random.uniform(50, 500), 2)
        consultas.append((i, paciente_id, doctor_id, fecha, diagnostico, costo))

    cursor.executemany(
        "INSERT INTO consultas VALUES (?, ?, ?, ?, ?, ?)", consultas
    )

    conn.commit()
    conn.close()
    print(f"Base de datos creada: {db_path}")


if __name__ == "__main__":
    crear_base_datos()
