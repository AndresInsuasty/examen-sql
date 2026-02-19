# Soluciones - Examen SQL Gimnasio

> "El unico lugar donde sudar es aceptable... y tus queries tambien."

---

## Pregunta 1
**¿Cuantos miembros activos tiene actualmente el gimnasio?**

```sql
SELECT COUNT(*) AS miembros_activos
FROM miembros
WHERE activo = 1;
```

*Spoiler: Mas que los que realmente van al gym en enero.*

---

## Pregunta 2
**¿Cual es la edad promedio de los miembros con membresia VIP?**

```sql
SELECT AVG(edad) AS edad_promedio_vip
FROM miembros
WHERE tipo_membresia = 'VIP';
```

*Los VIP: porque pagar mas te hace sentir mas fit.*

---

## Pregunta 3
**Lista el nombre y edad de todos los miembros mayores de 50 anos, ordenados de mayor a menor edad.**

```sql
SELECT nombre, edad
FROM miembros
WHERE edad > 50
ORDER BY edad DESC;
```

*La edad es solo un numero... especialmente cuando haces cardio.*

---

## Pregunta 4
**¿Cuantos miembros hay de cada tipo de membresia?**

```sql
SELECT tipo_membresia, COUNT(*) AS cantidad
FROM miembros
GROUP BY tipo_membresia;
```

*Basica, Premium, VIP: el ciclo de vida de toda resolucion de Ano Nuevo.*

---

## Pregunta 5
**¿Cual es la clase con mayor capacidad maxima?**

```sql
SELECT nombre, capacidad_maxima
FROM clases
ORDER BY capacidad_maxima DESC
LIMIT 1;
```

*Capacidad maxima != asistencia real. Nunca.*

---

## Pregunta 6
**Lista todas las clases que duran mas de 60 minutos.**

```sql
SELECT nombre, duracion_minutos
FROM clases
WHERE duracion_minutos > 60;
```

*Para los que piensan que sufrir poco es para principiantes.*

---

## Pregunta 7
**¿Cuantas asistencias se registraron en total durante el ultimo mes?**

```sql
SELECT COUNT(*) AS asistencias_ultimo_mes
FROM asistencias
WHERE fecha >= DATE('now', '-1 month');
```

*Nota: Los datos pueden variar segun la proximidad al verano.*

---

## Pregunta 8
**¿Cual es la calificacion promedio de cada clase? Muestra solo las clases con promedio mayor a 3.**

```sql
SELECT c.nombre, AVG(a.calificacion) AS calificacion_promedio
FROM clases c
JOIN asistencias a ON c.id = a.clase_id
WHERE a.calificacion IS NOT NULL
GROUP BY c.id, c.nombre
HAVING AVG(a.calificacion) > 3;
```

*Si tu clase tiene menos de 3 estrellas, quizas es hora de cambiar la playlist.*

---

## Pregunta 9
**¿Cuales son los 5 miembros que mas asistencias tienen registradas?**

```sql
SELECT m.nombre, COUNT(*) AS total_asistencias
FROM miembros m
JOIN asistencias a ON m.id = a.miembro_id
GROUP BY m.id, m.nombre
ORDER BY total_asistencias DESC
LIMIT 5;
```

*Los MVPs del gimnasio. Probablemente viven ahi.*

---

## Pregunta 10
**Lista el nombre de los miembros que han asistido a la clase de "Spinning" junto con la fecha de asistencia.**

```sql
SELECT m.nombre, a.fecha
FROM miembros m
JOIN asistencias a ON m.id = a.miembro_id
JOIN clases c ON a.clase_id = c.id
WHERE c.nombre = 'Spinning';
```

*Spinning: donde pagas para andar en bicicleta sin ir a ninguna parte.*

---

## Pregunta 11
**¿Cuantos miembros hombres y cuantas mujeres hay en cada tipo de membresia?**

```sql
SELECT tipo_membresia, genero, COUNT(*) AS cantidad
FROM miembros
GROUP BY tipo_membresia, genero
ORDER BY tipo_membresia, genero;
```

*Datos demograficos: porque a Marketing le encanta hacer graficas.*

---

## Pregunta 12
**¿Cuales clases no han recibido ninguna calificacion de 5 estrellas?**

```sql
SELECT c.nombre
FROM clases c
WHERE c.id NOT IN (
    SELECT DISTINCT clase_id
    FROM asistencias
    WHERE calificacion = 5
);
```

*O la clase es muy dificil, o muy temprano. Probablemente muy temprano.*

---

> "Un buen analista de datos nunca salta el dia de pierna... ni el dia de JOINs."
