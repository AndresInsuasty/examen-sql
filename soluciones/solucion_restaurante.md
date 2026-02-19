# Soluciones - Examen SQL Restaurante

> "Donde los datos son el plato principal y las propinas son el postre."

---

## Pregunta 1
**¿Cual es el salario promedio de los meseros?**

```sql
SELECT AVG(salario) AS salario_promedio
FROM meseros;
```

**Respuesta:** 1,819.85

*Spoiler: Menos de lo que merecen por aguantar clientes dificiles.*

---

## Pregunta 2
**Lista los nombres de todos los meseros del turno "Noche" ordenados alfabeticamente.**

```sql
SELECT nombre
FROM meseros
WHERE turno = 'Noche'
ORDER BY nombre ASC;
```

*Los nocturnos: conocen mas secretos que el barista del lugar.*

---

## Pregunta 3
**¿Cuantas mesas hay en cada ubicacion del restaurante?**

```sql
SELECT ubicacion, COUNT(*) AS cantidad_mesas
FROM mesas
GROUP BY ubicacion;
```

*Terraza > Interior. Siempre. No se discute.*

---

## Pregunta 4
**¿Cual fue el monto total de ventas del restaurante en el ultimo mes?**

```sql
SELECT SUM(total) AS ventas_ultimo_mes
FROM ordenes
WHERE fecha >= DATE('now', '-1 month');
```

**Respuesta:** 75,755.25

*El numero que hace feliz (o triste) al dueno.*

---

## Pregunta 5
**¿Cual es la propina promedio que reciben los meseros? (ignorando ordenes sin propina)**

```sql
SELECT AVG(propina) AS propina_promedio
FROM ordenes
WHERE propina IS NOT NULL;
```

**Respuesta:** 18.79

*Recordatorio: dejar propina es de buena educacion y buen karma.*

---

## Pregunta 6
**¿Cual es el total promedio de las 10 ordenes con mayor monto?**

```sql
SELECT ROUND(AVG(total), 2) AS promedio_top10
FROM (
    SELECT total
    FROM ordenes
    ORDER BY total DESC
    LIMIT 10
);
```

**Respuesta:** 345.17

*Las mesas que pidieron "traigan de todo" literalmente.*

---

## Pregunta 7
**¿Cual es el mesero que ha atendido mas ordenes? Muestra su nombre y el total de ordenes.**

```sql
SELECT m.nombre, COUNT(*) AS total_ordenes
FROM meseros m
JOIN ordenes o ON m.id = o.mesero_id
GROUP BY m.id, m.nombre
ORDER BY total_ordenes DESC
LIMIT 1;
```

**Respuesta:** Narcisa de Blázquez (26 órdenes)

*Los que mas caminan, merecen los mejores zapatos.*

---

## Pregunta 8
**¿Cual es el mesero que ha generado mas ingresos en total? Muestra su nombre y el monto total.**

```sql
SELECT m.nombre, SUM(o.total) AS ingresos_generados
FROM meseros m
JOIN ordenes o ON m.id = o.mesero_id
GROUP BY m.id, m.nombre
ORDER BY ingresos_generados DESC
LIMIT 1;
```

**Respuesta:** Macaria Graciela Pineda Carrera (5,175.01)

*El empleado del mes eterno. Probablemente tambien el favorito del jefe.*

---

## Pregunta 9
**¿Cuantos comensales en promedio se sientan en las mesas de la Terraza?**

```sql
SELECT AVG(o.num_comensales) AS promedio_comensales_terraza
FROM ordenes o
JOIN mesas m ON o.mesa_id = m.id
WHERE m.ubicacion = 'Terraza';
```

**Respuesta:** 2.85

*La terraza: donde todos quieren estar, especialmente si hay wifi.*

---

## Pregunta 10
**¿Cuantos meseros han atendido mas de 20 ordenes?**

```sql
SELECT COUNT(*) AS meseros_experimentados
FROM (
    SELECT m.id
    FROM meseros m
    JOIN ordenes o ON m.id = o.mesero_id
    GROUP BY m.id
    HAVING COUNT(*) > 20
);
```

**Respuesta:** 9

*Los veteranos. Saben el menu de memoria y tus excusas tambien.*

---

## Pregunta 11
**¿Cual es el porcentaje promedio de propina respecto al total de la orden?**

```sql
SELECT AVG((propina / total) * 100) AS porcentaje_propina_promedio
FROM ordenes
WHERE propina IS NOT NULL AND total > 0;
```

**Respuesta:** 9.61%

*Si es menos del 10%, hay que tener una conversacion seria.*

---

## Pregunta 12
**¿Cuantas mesas de capacidad 6 o mas personas estan actualmente disponibles?**

```sql
SELECT COUNT(*) AS mesas_grandes_disponibles
FROM mesas
WHERE capacidad >= 6 AND disponible = 1;
```

**Respuesta:** 8

*Perfectas para cuando "somos pocos" significa "invitamos a medio mundo".*

---

> "Un buen analista de datos siempre pide los datos al dente: ni crudos ni sobre-procesados."
