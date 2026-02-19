# Examen SQL - Base de Datos Hospital

## Diagrama Entidad-Relacion

```
+------------------+       +------------------+       +------------------+
|    pacientes     |       |    consultas     |       |     doctores     |
+------------------+       +------------------+       +------------------+
| id          PK   |<------| paciente_id  FK  |       | id          PK   |
| nombre           |       | doctor_id    FK  |------>| nombre           |
| edad             |       | id          PK   |       | especialidad     |
| genero           |       | fecha            |       | anios_experiencia|
| tipo_sangre      |       | diagnostico      |       | consultorio      |
| fecha_registro   |       | costo            |       +------------------+
+------------------+       +------------------+
```

## Descripcion de Tablas

- **pacientes**: Informacion de los pacientes registrados
- **doctores**: Medicos del hospital y sus especialidades
- **consultas**: Registro de consultas medicas realizadas

---

## Preguntas

### Pregunta 1
¿Cuantos pacientes hay registrados en el hospital?

---

### Pregunta 2
Lista todos los doctores de la especialidad "Cardiologia" ordenados por anos de experiencia (de mayor a menor).

---

### Pregunta 3
¿Cual es la distribucion de pacientes por tipo de sangre? Muestra tipo y cantidad.

---

### Pregunta 4
¿Cual es el costo promedio de las consultas en el hospital?

---

### Pregunta 5
Lista los 5 diagnosticos mas frecuentes con su cantidad de casos.

---

### Pregunta 6
¿Cual es el doctor que ha realizado mas consultas? Muestra su nombre y el total de consultas.

---

### Pregunta 7
¿Cual es el doctor con mas anos de experiencia? Muestra nombre, especialidad y anos.

---

### Pregunta 8
¿Cuantos pacientes menores de 18 anos hay y cual es su edad promedio?

---

### Pregunta 9
¿Cual es la especialidad medica que genera mas ingresos y cuanto es el total?

---

### Pregunta 10
¿Que rango de edad y genero tiene la mayor cantidad de pacientes?

---

### Pregunta 11
¿Cuantos doctores han atendido mas de 30 consultas?

---

### Pregunta 12
¿Cuantos pacientes han tenido mas de 3 consultas en el ultimo ano?

---

## Notas

- La base de datos se encuentra en: `data/hospital.db`
- Usa SQLite para ejecutar tus consultas
- El campo `genero` usa 'M' para masculino y 'F' para femenino
- Los tipos de sangre incluyen: A+, A-, B+, B-, AB+, AB-, O+, O-
