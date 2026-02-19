# Examen SQL - Base de Datos Bar

## Diagrama Entidad-Relacion

```
+------------------+       +------------------+       +------------------+
|   bartenders     |       |      ventas      |       |     bebidas      |
+------------------+       +------------------+       +------------------+
| id          PK   |<------| bartender_id FK  |       | id          PK   |
| nombre           |       | bebida_id    FK  |------>| nombre           |
| experiencia_anios|       | id          PK   |       | categoria        |
| turno            |       | fecha            |       | precio           |
| especialidad     |       | cantidad         |       | contenido_alcoholico
+------------------+       | hora             |       | disponible       |
                           +------------------+       +------------------+
```

## Descripcion de Tablas

- **bartenders**: Cantineros del bar y sus especialidades
- **bebidas**: Catalogo de bebidas disponibles
- **ventas**: Registro de ventas realizadas

---

## Preguntas

### Pregunta 1
¿Cuantas bebidas hay en cada categoria?

---

### Pregunta 2
Lista todas las bebidas con contenido alcoholico mayor a 15%, ordenadas de mayor a menor graduacion.

---

### Pregunta 3
¿Cual es el precio promedio de los cocteles?

---

### Pregunta 4
¿Cuantas bebidas estan actualmente no disponibles?

---

### Pregunta 5
Lista los bartenders del turno "Noche" con mas de 5 anos de experiencia.

---

### Pregunta 6
¿Cual es la bebida mas vendida? Muestra nombre y cantidad total vendida.

---

### Pregunta 7
¿Cual es el ingreso total generado por cada categoria de bebida?

---

### Pregunta 8
¿Cual es el bartender que ha realizado mas ventas? Muestra su nombre y el total de ventas.

---

### Pregunta 9
¿Cuales son las 3 horas con mas ventas en el bar?

---

### Pregunta 10
¿Cual es el bartender con mayor experiencia en "Cocteles clasicos"?

---

### Pregunta 11
Lista las bebidas sin alcohol ordenadas por precio de menor a mayor.

---

### Pregunta 12
¿Cual bartender tiene el mayor promedio de unidades vendidas por venta?

---

## Notas

- La base de datos se encuentra en: `data/bar.db`
- Usa SQLite para ejecutar tus consultas
- El campo `disponible` usa 1 para disponible y 0 para no disponible
- El campo `turno` puede ser: "Tarde", "Noche" o "Madrugada"
- La hora se almacena en formato "HH:00"
