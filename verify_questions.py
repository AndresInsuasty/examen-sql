#!/usr/bin/env python3
"""Verificación final - todas las preguntas deben tener respuestas cortas."""

import sqlite3

def query_db(db_path, query):
    """Execute query and return results."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        return f"ERROR: {e}"

# Todas las queries ACTUALIZADAS por examen
GIMNASIO = [
    ("P1", "SELECT COUNT(*) FROM miembros WHERE activo = 1;", "1 valor"),
    ("P2", "SELECT AVG(edad) FROM miembros WHERE tipo_membresia = 'VIP';", "1 valor"),
    ("P3", "SELECT COUNT(*), AVG(edad) FROM miembros WHERE edad > 50;", "2 valores"),
    ("P4", "SELECT tipo_membresia, COUNT(*) FROM miembros GROUP BY tipo_membresia;", "3-4 filas"),
    ("P5", "SELECT nombre, capacidad_maxima FROM clases ORDER BY capacidad_maxima DESC LIMIT 1;", "1 fila"),
    ("P6", "SELECT nombre, duracion_minutos FROM clases WHERE duracion_minutos > 60;", "variable"),
    ("P7", "SELECT COUNT(*) FROM asistencias WHERE fecha >= DATE('now', '-1 month');", "1 valor"),
    ("P8", "SELECT COUNT(*) FROM (SELECT c.id FROM clases c JOIN asistencias a ON c.id = a.clase_id WHERE a.calificacion IS NOT NULL GROUP BY c.id HAVING AVG(a.calificacion) > 3);", "1 valor"),
    ("P9", "SELECT m.nombre, COUNT(*) FROM miembros m JOIN asistencias a ON m.id = a.miembro_id GROUP BY m.id, m.nombre ORDER BY COUNT(*) DESC LIMIT 5;", "5 filas"),
    ("P10", "SELECT COUNT(*), AVG(calificacion) FROM asistencias a JOIN clases c ON a.clase_id = c.id WHERE c.nombre = 'Spinning';", "2 valores"),
    ("P11", "SELECT tipo_membresia, genero, COUNT(*) FROM miembros GROUP BY tipo_membresia, genero;", "6-8 filas"),
    ("P12", "SELECT nombre FROM clases WHERE id NOT IN (SELECT DISTINCT clase_id FROM asistencias WHERE calificacion = 5);", "variable"),
]

HOSPITAL = [
    ("P1", "SELECT COUNT(*) FROM pacientes;", "1 valor"),
    ("P2", "SELECT nombre, anios_experiencia FROM doctores WHERE especialidad = 'Cardiologia' ORDER BY anios_experiencia DESC;", "variable"),
    ("P3", "SELECT tipo_sangre, COUNT(*) FROM pacientes GROUP BY tipo_sangre ORDER BY COUNT(*) DESC;", "8 filas"),
    ("P4", "SELECT AVG(costo) FROM consultas;", "1 valor"),
    ("P5", "SELECT diagnostico, COUNT(*) FROM consultas GROUP BY diagnostico ORDER BY COUNT(*) DESC LIMIT 5;", "5 filas"),
    ("P6", "SELECT d.nombre, COUNT(*) FROM doctores d JOIN consultas c ON d.id = c.doctor_id GROUP BY d.id, d.nombre ORDER BY COUNT(*) DESC LIMIT 1;", "1 fila"),
    ("P7", "SELECT nombre, especialidad, anios_experiencia FROM doctores ORDER BY anios_experiencia DESC LIMIT 1;", "1 fila"),
    ("P8", "SELECT COUNT(*), AVG(edad) FROM pacientes WHERE edad < 18;", "2 valores"),
    ("P9", "SELECT d.especialidad, SUM(c.costo) FROM doctores d JOIN consultas c ON d.id = c.doctor_id GROUP BY d.especialidad ORDER BY SUM(c.costo) DESC LIMIT 1;", "1 fila"),
    ("P10", "SELECT CASE WHEN edad < 18 THEN '0-17' WHEN edad BETWEEN 18 AND 40 THEN '18-40' WHEN edad BETWEEN 41 AND 65 THEN '41-65' ELSE '65+' END, genero, COUNT(*) FROM pacientes GROUP BY 1, genero ORDER BY COUNT(*) DESC LIMIT 1;", "1 fila"),
    ("P11", "SELECT COUNT(*) FROM (SELECT d.id FROM doctores d JOIN consultas c ON d.id = c.doctor_id GROUP BY d.id HAVING COUNT(*) > 30);", "1 valor"),
    ("P12", "SELECT COUNT(*) FROM (SELECT p.id FROM pacientes p JOIN consultas c ON p.id = c.paciente_id WHERE c.fecha >= DATE('now', '-1 year') GROUP BY p.id HAVING COUNT(*) > 3);", "1 valor"),
]

BANCO = [
    ("P1", "SELECT ciudad, COUNT(*) FROM clientes GROUP BY ciudad ORDER BY COUNT(*) DESC LIMIT 1;", "1 fila"),
    ("P2", "SELECT AVG(saldo) FROM cuentas WHERE tipo_cuenta = 'Ahorro';", "1 valor"),
    ("P3", "SELECT AVG(saldo_total) FROM (SELECT SUM(saldo) AS saldo_total FROM clientes cl JOIN cuentas cu ON cl.id = cu.cliente_id GROUP BY cl.id ORDER BY saldo_total DESC LIMIT 10);", "1 valor"),
    ("P4", "SELECT tipo, COUNT(*) FROM transacciones GROUP BY tipo;", "4 filas"),
    ("P5", "SELECT SUM(monto) FROM transacciones WHERE tipo = 'Deposito' AND fecha >= DATE('now', '-1 month');", "1 valor"),
    ("P6", "SELECT COUNT(*), MAX(cnt) FROM (SELECT cliente_id, COUNT(*) AS cnt FROM cuentas GROUP BY cliente_id HAVING COUNT(*) > 1);", "2 valores"),
    ("P7", "SELECT ocupacion, COUNT(*) FROM clientes GROUP BY ocupacion ORDER BY COUNT(*) DESC LIMIT 1;", "1 fila"),
    ("P8", "SELECT COUNT(*) FROM cuentas WHERE tipo_cuenta = 'Inversion' AND saldo > 50000;", "1 valor"),
    ("P9", "SELECT COUNT(*), SUM(monto) FROM transacciones WHERE monto > 3000;", "2 valores"),
    ("P10", "SELECT nombre, edad FROM clientes WHERE edad IN ((SELECT MIN(edad) FROM clientes), (SELECT MAX(edad) FROM clientes));", "2 filas"),
    ("P11", "SELECT tipo_cuenta, SUM(saldo) FROM cuentas GROUP BY tipo_cuenta;", "4 filas"),
    ("P12", "SELECT COUNT(DISTINCT cl.id) FROM clientes cl JOIN cuentas cu ON cl.id = cu.cliente_id WHERE cl.ciudad = 'Madrid' AND cu.tipo_cuenta = 'Nomina';", "1 valor"),
]

BAR = [
    ("P1", "SELECT categoria, COUNT(*) FROM bebidas GROUP BY categoria;", "5 filas"),
    ("P2", "SELECT nombre, contenido_alcoholico FROM bebidas WHERE contenido_alcoholico > 15 ORDER BY contenido_alcoholico DESC;", "variable"),
    ("P3", "SELECT AVG(precio) FROM bebidas WHERE categoria = 'Coctel';", "1 valor"),
    ("P4", "SELECT COUNT(*) FROM bebidas WHERE disponible = 0;", "1 valor"),
    ("P5", "SELECT nombre, experiencia_anios FROM bartenders WHERE turno = 'Noche' AND experiencia_anios > 5;", "variable"),
    ("P6", "SELECT b.nombre, SUM(v.cantidad) FROM bebidas b JOIN ventas v ON b.id = v.bebida_id GROUP BY b.id, b.nombre ORDER BY SUM(v.cantidad) DESC LIMIT 1;", "1 fila"),
    ("P7", "SELECT b.categoria, SUM(b.precio * v.cantidad) FROM bebidas b JOIN ventas v ON b.id = v.bebida_id GROUP BY b.categoria;", "5 filas"),
    ("P8", "SELECT bt.nombre, COUNT(*) FROM bartenders bt JOIN ventas v ON bt.id = v.bartender_id GROUP BY bt.id, bt.nombre ORDER BY COUNT(*) DESC LIMIT 1;", "1 fila"),
    ("P9", "SELECT hora, COUNT(*) FROM ventas GROUP BY hora ORDER BY COUNT(*) DESC LIMIT 3;", "3 filas"),
    ("P10", "SELECT nombre, experiencia_anios FROM bartenders WHERE especialidad = 'Cocteles clasicos' ORDER BY experiencia_anios DESC LIMIT 1;", "1 fila"),
    ("P11", "SELECT nombre, precio FROM bebidas WHERE contenido_alcoholico = 0 ORDER BY precio ASC;", "variable"),
    ("P12", "SELECT bt.nombre, AVG(v.cantidad) FROM bartenders bt JOIN ventas v ON bt.id = v.bartender_id GROUP BY bt.id, bt.nombre ORDER BY AVG(v.cantidad) DESC LIMIT 1;", "1 fila"),
]

RESTAURANTE = [
    ("P1", "SELECT AVG(salario) FROM meseros;", "1 valor"),
    ("P2", "SELECT nombre FROM meseros WHERE turno = 'Noche' ORDER BY nombre ASC;", "variable"),
    ("P3", "SELECT ubicacion, COUNT(*) FROM mesas GROUP BY ubicacion;", "3-4 filas"),
    ("P4", "SELECT SUM(total) FROM ordenes WHERE fecha >= DATE('now', '-1 month');", "1 valor"),
    ("P5", "SELECT AVG(propina) FROM ordenes WHERE propina IS NOT NULL;", "1 valor"),
    ("P6", "SELECT AVG(total) FROM (SELECT total FROM ordenes ORDER BY total DESC LIMIT 10);", "1 valor"),
    ("P7", "SELECT m.nombre, COUNT(*) FROM meseros m JOIN ordenes o ON m.id = o.mesero_id GROUP BY m.id, m.nombre ORDER BY COUNT(*) DESC LIMIT 1;", "1 fila"),
    ("P8", "SELECT m.nombre, SUM(o.total) FROM meseros m JOIN ordenes o ON m.id = o.mesero_id GROUP BY m.id, m.nombre ORDER BY SUM(o.total) DESC LIMIT 1;", "1 fila"),
    ("P9", "SELECT AVG(o.num_comensales) FROM ordenes o JOIN mesas m ON o.mesa_id = m.id WHERE m.ubicacion = 'Terraza';", "1 valor"),
    ("P10", "SELECT COUNT(*) FROM (SELECT m.id FROM meseros m JOIN ordenes o ON m.id = o.mesero_id GROUP BY m.id HAVING COUNT(*) > 20);", "1 valor"),
    ("P11", "SELECT AVG((propina / total) * 100) FROM ordenes WHERE propina IS NOT NULL AND total > 0;", "1 valor"),
    ("P12", "SELECT COUNT(*) FROM mesas WHERE capacidad >= 6 AND disponible = 1;", "1 valor"),
]

db_paths = {
    "GIMNASIO": "data/gimnasio.db",
    "HOSPITAL": "data/hospital.db",
    "BANCO": "data/banco.db",
    "BAR": "data/bar.db",
    "RESTAURANTE": "data/restaurante.db"
}

all_exams = {
    "GIMNASIO": GIMNASIO,
    "HOSPITAL": HOSPITAL,
    "BANCO": BANCO,
    "BAR": BAR,
    "RESTAURANTE": RESTAURANTE
}

print("="*70)
print("VERIFICACIÓN FINAL - TODAS LAS PREGUNTAS ACTUALIZADAS")
print("="*70)

total_questions = 0
short_answers = 0
medium_answers = 0
long_answers = 0

for exam_name, questions in all_exams.items():
    print(f"\n{exam_name}:")
    for pregunta, query, expected in questions:
        result = query_db(db_paths[exam_name], query)
        if isinstance(result, list):
            num_rows = len(result)
            total_questions += 1
            
            # Clasificar
            if num_rows <= 3:
                short_answers += 1
                status = "✅"
            elif num_rows <= 8:
                medium_answers += 1
                status = "⚠️"
            else:
                long_answers += 1
                status = "❌"
            
            print(f"  {pregunta}: {num_rows} filas {status} (esperado: {expected})")
        else:
            print(f"  {pregunta}: ERROR - {result}")

print(f"\n{'='*70}")
print("RESUMEN FINAL")
print('='*70)
print(f"Total preguntas: {total_questions}")
print(f"✅ Respuestas cortas (1-3 filas): {short_answers}")
print(f"⚠️ Respuestas medianas (4-8 filas): {medium_answers}")
print(f"❌ Respuestas largas (>8 filas): {long_answers}")

if long_answers == 0:
    print("\n🎉 ¡PERFECTO! Todas las preguntas tienen respuestas cortas o medianas.")
else:
    print(f"\n⚠️ Todavía hay {long_answers} preguntas con respuestas muy largas.")
