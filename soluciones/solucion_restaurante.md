# Soluciones - Examen SQL Restaurante

> "Donde los datos son el plato principal y las propinas son el postre."

---

## Pregunta 1
**¿Cual es el salario promedio de los meseros?**

```sql
SELECT AVG(salario) AS salario_promedio
FROM meseros;
```

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

*El numero que hace feliz (o triste) al dueno.*

---

## Pregunta 5
**¿Cual es la propina promedio que reciben los meseros? (ignorando ordenes sin propina)**

```sql
SELECT AVG(propina) AS propina_promedio
FROM ordenes
WHERE propina IS NOT NULL;
```

*Recordatorio: dejar propina es de buena educacion y buen karma.*

---

## Pregunta 6
**Lista las 10 ordenes con el total mas alto, mostrando el id de la orden, total y propina.**

```sql
SELECT id, total, propina
FROM ordenes
ORDER BY total DESC
LIMIT 10;
```

*Las mesas que pidieron "traigan de todo" literalmente.*

---

## Pregunta 7
**¿Cuantas ordenes ha atendido cada mesero? Muestra nombre del mesero y cantidad de ordenes.**

```sql
SELECT m.nombre, COUNT(*) AS total_ordenes
FROM meseros m
JOIN ordenes o ON m.id = o.mesero_id
GROUP BY m.id, m.nombre
ORDER BY total_ordenes DESC;
```

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

*La terraza: donde todos quieren estar, especialmente si hay wifi.*

---

## Pregunta 10
**Lista los meseros que han atendido mas de 20 ordenes.**

```sql
SELECT m.nombre, COUNT(*) AS total_ordenes
FROM meseros m
JOIN ordenes o ON m.id = o.mesero_id
GROUP BY m.id, m.nombre
HAVING COUNT(*) > 20;
```

*Los veteranos. Saben el menu de memoria y tus excusas tambien.*

---

## Pregunta 11
**¿Cual es el porcentaje promedio de propina respecto al total de la orden?**

```sql
SELECT AVG((propina / total) * 100) AS porcentaje_propina_promedio
FROM ordenes
WHERE propina IS NOT NULL AND total > 0;
```

*Si es menos del 10%, hay que tener una conversacion seria.*

---

## Pregunta 12
**¿Cuales mesas de capacidad 6 o mas personas estan actualmente disponibles?**

```sql
SELECT id, capacidad, ubicacion
FROM mesas
WHERE capacidad >= 6 AND disponible = 1;
```

*Perfectas para cuando "somos pocos" significa "invitamos a medio mundo".*

---

> "Un buen analista de datos siempre pide los datos al dente: ni crudos ni sobre-procesados."
