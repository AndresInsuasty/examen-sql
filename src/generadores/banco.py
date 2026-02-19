"""Generador de base de datos para un banco."""

import sqlite3
import random
from datetime import datetime, timedelta
from pathlib import Path
from faker import Faker

fake = Faker("es_ES")


def crear_base_datos():
    """Crea la base de datos del banco con datos ficticios."""
    db_path = Path(__file__).parent.parent.parent / "data" / "banco.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Crear tablas
    cursor.execute("""
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            ocupacion TEXT NOT NULL,
            fecha_apertura DATE NOT NULL,
            ciudad TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE cuentas (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER NOT NULL,
            tipo_cuenta TEXT NOT NULL,
            saldo REAL NOT NULL,
            fecha_apertura DATE NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE transacciones (
            id INTEGER PRIMARY KEY,
            cuenta_id INTEGER NOT NULL,
            tipo TEXT NOT NULL,
            monto REAL NOT NULL,
            fecha DATE NOT NULL,
            descripcion TEXT,
            FOREIGN KEY (cuenta_id) REFERENCES cuentas(id)
        )
    """)

    # Insertar clientes
    ocupaciones = [
        "Ingeniero", "Medico", "Abogado", "Profesor", "Comerciante",
        "Contador", "Arquitecto", "Empresario", "Estudiante", "Jubilado"
    ]
    ciudades = [
        "Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao",
        "Malaga", "Zaragoza", "Murcia", "Palma", "Granada"
    ]

    clientes = []
    for i in range(1, 121):
        nombre = fake.name()
        edad = random.randint(18, 75)
        ocupacion = random.choice(ocupaciones)
        fecha_apertura = fake.date_between(start_date="-10y", end_date="-1m")
        ciudad = random.choice(ciudades)
        clientes.append((i, nombre, edad, ocupacion, fecha_apertura, ciudad))

    cursor.executemany(
        "INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?)", clientes
    )

    # Insertar cuentas
    tipos_cuenta = ["Ahorro", "Corriente", "Nomina", "Inversion"]

    cuentas = []
    cuenta_id = 1
    for cliente in clientes:
        num_cuentas = random.choices([1, 2, 3], weights=[60, 30, 10])[0]
        for _ in range(num_cuentas):
            tipo_cuenta = random.choice(tipos_cuenta)
            if tipo_cuenta == "Inversion":
                saldo = round(random.uniform(5000, 100000), 2)
            elif tipo_cuenta == "Ahorro":
                saldo = round(random.uniform(500, 30000), 2)
            else:
                saldo = round(random.uniform(100, 15000), 2)
            fecha_apertura = fake.date_between(
                start_date=cliente[4],
                end_date="today"
            )
            cuentas.append((cuenta_id, cliente[0], tipo_cuenta, saldo, fecha_apertura))
            cuenta_id += 1

    cursor.executemany(
        "INSERT INTO cuentas VALUES (?, ?, ?, ?, ?)", cuentas
    )

    # Insertar transacciones
    tipos_transaccion = ["Deposito", "Retiro", "Transferencia", "Pago"]
    descripciones = [
        "Nomina mensual", "Pago servicios", "Compra supermercado",
        "Transferencia familiar", "Pago alquiler", "Retiro cajero",
        "Deposito efectivo", "Pago tarjeta", "Suscripcion", "Varios"
    ]

    transacciones = []
    for i in range(1, 801):
        cuenta_id = random.randint(1, len(cuentas))
        tipo = random.choice(tipos_transaccion)
        if tipo in ["Deposito", "Transferencia"]:
            monto = round(random.uniform(50, 5000), 2)
        else:
            monto = round(random.uniform(10, 2000), 2)
        fecha = fake.date_between(start_date="-1y", end_date="today")
        descripcion = random.choice(descripciones)
        transacciones.append((i, cuenta_id, tipo, monto, fecha, descripcion))

    cursor.executemany(
        "INSERT INTO transacciones VALUES (?, ?, ?, ?, ?, ?)", transacciones
    )

    conn.commit()
    conn.close()
    print(f"Base de datos creada: {db_path}")


if __name__ == "__main__":
    crear_base_datos()
