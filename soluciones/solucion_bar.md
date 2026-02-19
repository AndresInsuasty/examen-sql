# Soluciones - Examen SQL Bar

> "Donde los datos fluyen como los cocteles y los GROUP BY son la vida social."

---

## Pregunta 1
**¿Cuantas bebidas hay en cada categoria?**

```sql
SELECT categoria, COUNT(*) AS cantidad
FROM bebidas
GROUP BY categoria
ORDER BY cantidad DESC;
```

*Variedad es la clave. Como en la vida.*

---

## Pregunta 2
**Lista todas las bebidas con contenido alcoholico mayor a 15%, ordenadas de mayor a menor graduacion.**

```sql
SELECT nombre, contenido_alcoholico
FROM bebidas
WHERE contenido_alcoholico > 15
ORDER BY contenido_alcoholico DESC;
```

*Las bebidas que vienen con responsabilidad incluida.*

---

## Pregunta 3
**¿Cual es el precio promedio de los cocteles?**

```sql
SELECT AVG(precio) AS precio_promedio_cocteles
FROM bebidas
WHERE categoria = 'Coctel';
```

**Respuesta:** 9.64

*El precio del arte liquido.*

---

## Pregunta 4
**¿Cuantas bebidas estan actualmente no disponibles?**

```sql
SELECT COUNT(*) AS bebidas_no_disponibles
FROM bebidas
WHERE disponible = 0;
```

**Respuesta:** 2

*Las que estan "en pausa" hasta que llegue el proveedor.*

---

## Pregunta 5
**Lista los bartenders del turno "Noche" con mas de 5 anos de experiencia.**

```sql
SELECT nombre, experiencia_anios
FROM bartenders
WHERE turno = 'Noche'
AND experiencia_anios > 5
ORDER BY experiencia_anios DESC;
```

*Los maestros nocturnos. Saben mezclar y tambien escuchar.*

---

## Pregunta 6
**¿Cual es la bebida mas vendida? Muestra nombre y cantidad total vendida.**

```sql
SELECT b.nombre, SUM(v.cantidad) AS total_vendido
FROM bebidas b
JOIN ventas v ON b.id = v.bebida_id
GROUP BY b.id, b.nombre
ORDER BY total_vendido DESC
LIMIT 1;
```

**Respuesta:** Cosmopolitan (85 unidades)

*La estrella del menu. Probablemente tiene su propio club de fans.*

---

## Pregunta 7
**¿Cual es el ingreso total generado por cada categoria de bebida?**

```sql
SELECT b.categoria, SUM(b.precio * v.cantidad) AS ingresos_totales
FROM bebidas b
JOIN ventas v ON b.id = v.bebida_id
GROUP BY b.categoria
ORDER BY ingresos_totales DESC;
```

*Datos que deciden que tan grande es la seccion de cocteles el proximo mes.*

---

## Pregunta 8
**¿Cual es el bartender que ha realizado mas ventas? Muestra su nombre y el total de ventas.**

```sql
SELECT bt.nombre, COUNT(*) AS total_ventas
FROM bartenders bt
JOIN ventas v ON bt.id = v.bartender_id
GROUP BY bt.id, bt.nombre
ORDER BY total_ventas DESC
LIMIT 1;
```

**Respuesta:** Rico Heredia Torralba (60 ventas)

*El ranking de productividad. Con estilo.*

---

## Pregunta 9
**¿Cuales son las 3 horas con mas ventas en el bar?**

```sql
SELECT hora, COUNT(*) AS total_ventas
FROM ventas
GROUP BY hora
ORDER BY total_ventas DESC
LIMIT 3;
```

*Happy hour revelado por los datos. La ciencia detras de la fiesta.*

---

## Pregunta 10
**¿Cual es el bartender con mayor experiencia en "Cocteles clasicos"?**

```sql
SELECT nombre, experiencia_anios
FROM bartenders
WHERE especialidad = 'Cocteles clasicos'
ORDER BY experiencia_anios DESC
LIMIT 1;
```

**Respuesta:** Paula Olmedo Pedrero (15 años)

*El guardian de las recetas tradicionales. Probablemente juzga tus gustos.*

---

## Pregunta 11
**Lista las bebidas sin alcohol ordenadas por precio de menor a mayor.**

```sql
SELECT nombre, precio
FROM bebidas
WHERE contenido_alcoholico = 0
ORDER BY precio ASC;
```

*Para los conductores designados y los que tienen que trabajar manana temprano.*

---

## Pregunta 12
**¿Cual bartender tiene el mayor promedio de unidades vendidas por venta?**

```sql
SELECT bt.nombre, ROUND(AVG(v.cantidad), 2) AS promedio_unidades
FROM bartenders bt
JOIN ventas v ON bt.id = v.bartender_id
GROUP BY bt.id, bt.nombre
ORDER BY promedio_unidades DESC
LIMIT 1;
```

**Respuesta:** Nélida Beltran Capdevila (2.03 unidades promedio)

*El que vende mas por ticket es el que mejor convence... o el que mejor mezcla.*

---

> "Un buen analista de datos sabe que la mejor query, como el mejor coctel, tiene el balance perfecto."
