# Examen SQL - Base de Datos Gimnasio

## Diagrama Entidad-Relación

```
+------------------+       +------------------+       +------------------+
|     miembros     |       |   asistencias    |       |      clases      |
+------------------+       +------------------+       +------------------+
| id          PK   |<------| miembro_id   FK  |       | id          PK   |
| nombre           |       | clase_id     FK  |------>| nombre           |
| edad             |       | id          PK   |       | instructor       |
| genero           |       | fecha            |       | horario          |
| fecha_inscripcion|       | calificacion     |       | capacidad_maxima |
| tipo_membresia   |       +------------------+       | duracion_minutos |
| activo           |                                  +------------------+
+------------------+
```

## Descripcion de Tablas

- **miembros**: Informacion de los socios del gimnasio
- **clases**: Clases grupales disponibles en el gimnasio
- **asistencias**: Registro de asistencia de miembros a las clases

---

## Preguntas

### Pregunta 1
¿Cuantos miembros activos tiene actualmente el gimnasio?

---

### Pregunta 2
¿Cual es la edad promedio de los miembros con membresia VIP?

---

### Pregunta 3
¿Cuantos miembros mayores de 50 anos hay y cual es su edad promedio?

---

### Pregunta 4
¿Cuantos miembros hay de cada tipo de membresia?

---

### Pregunta 5
¿Cual es la clase con mayor capacidad maxima?

---

### Pregunta 6
Lista todas las clases que duran mas de 60 minutos.

---

### Pregunta 7
¿Cuantas asistencias se registraron en total durante el ultimo mes?

---

### Pregunta 8
¿Cuantas clases tienen una calificacion promedio mayor a 3?

---

### Pregunta 9
¿Cuales son los 5 miembros que mas asistencias tienen registradas?

---

### Pregunta 10
¿Cuantas asistencias ha tenido la clase "Spinning" y cual es la calificacion promedio?

---

### Pregunta 11
¿Cuantos miembros hombres y cuantas mujeres hay en cada tipo de membresia?

---

### Pregunta 12
¿Cuales clases no han recibido ninguna calificacion de 5 estrellas?

---

## Notas

- La base de datos se encuentra en: `data/gimnasio.db`
- Usa SQLite para ejecutar tus consultas
- El campo `activo` usa 1 para activo y 0 para inactivo
- El campo `genero` usa 'M' para masculino y 'F' para femenino
