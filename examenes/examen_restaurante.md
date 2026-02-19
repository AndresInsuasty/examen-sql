# Examen SQL - Base de Datos Restaurante

## Diagrama Entidad-Relacion

```
+------------------+       +------------------+       +------------------+
|     meseros      |       |     ordenes      |       |      mesas       |
+------------------+       +------------------+       +------------------+
| id          PK   |<------| mesero_id    FK  |       | id          PK   |
| nombre           |       | mesa_id      FK  |------>| capacidad        |
| fecha_contratacion       | id          PK   |       | ubicacion        |
| turno            |       | fecha            |       | disponible       |
| salario          |       | total            |       +------------------+
+------------------+       | propina          |
                           | num_comensales   |
                           +------------------+
```

## Descripcion de Tablas

- **meseros**: Empleados que atienden las mesas
- **mesas**: Mesas disponibles en el restaurante
- **ordenes**: Registro de pedidos realizados

---

## Preguntas

### Pregunta 1
¿Cual es el salario promedio de los meseros?

---

### Pregunta 2
Lista los nombres de todos los meseros del turno "Noche" ordenados alfabeticamente.

---

### Pregunta 3
¿Cuantas mesas hay en cada ubicacion del restaurante?

---

### Pregunta 4
¿Cual fue el monto total de ventas del restaurante en el ultimo mes?

---

### Pregunta 5
¿Cual es la propina promedio que reciben los meseros? (ignorando ordenes sin propina)

---

### Pregunta 6
Lista las 10 ordenes con el total mas alto, mostrando el id de la orden, total y propina.

---

### Pregunta 7
¿Cuantas ordenes ha atendido cada mesero? Muestra nombre del mesero y cantidad de ordenes.

---

### Pregunta 8
¿Cual es el mesero que ha generado mas ingresos en total? Muestra su nombre y el monto total.

---

### Pregunta 9
¿Cuantos comensales en promedio se sientan en las mesas de la Terraza?

---

### Pregunta 10
Lista los meseros que han atendido mas de 20 ordenes.

---

### Pregunta 11
¿Cual es el porcentaje promedio de propina respecto al total de la orden?

---

### Pregunta 12
¿Cuales mesas de capacidad 6 o mas personas estan actualmente disponibles?

---

## Notas

- La base de datos se encuentra en: `data/restaurante.db`
- Usa SQLite para ejecutar tus consultas
- El campo `disponible` usa 1 para disponible y 0 para ocupada
- El campo `turno` puede ser: "Manana", "Tarde" o "Noche"
