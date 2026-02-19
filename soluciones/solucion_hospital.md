# Soluciones - Examen SQL Hospital

> "Donde los JOINs curan y los NULL son el verdadero diagnostico."

---

## Pregunta 1
**¿Cuantos pacientes hay registrados en el hospital?**

```sql
SELECT COUNT(*) AS total_pacientes
FROM pacientes;
```

*Todos vinieron por "un dolorcito" que termino siendo algo mas.*

---

## Pregunta 2
**Lista todos los doctores de la especialidad "Cardiologia" ordenados por anos de experiencia (de mayor a menor).**

```sql
SELECT nombre, anios_experiencia
FROM doctores
WHERE especialidad = 'Cardiologia'
ORDER BY anios_experiencia DESC;
```

*Los que mas saben del corazon... literalmente.*

---

## Pregunta 3
**¿Cual es la distribucion de pacientes por tipo de sangre? Muestra tipo y cantidad.**

```sql
SELECT tipo_sangre, COUNT(*) AS cantidad
FROM pacientes
GROUP BY tipo_sangre
ORDER BY cantidad DESC;
```

*O+ domina el mundo. Es ciencia, no opinion.*

---

## Pregunta 4
**¿Cual es el costo promedio de las consultas en el hospital?**

```sql
SELECT AVG(costo) AS costo_promedio
FROM consultas;
```

*Mas barato que buscar sintomas en internet y asustarte.*

---

## Pregunta 5
**Lista los 5 diagnosticos mas frecuentes con su cantidad de casos.**

```sql
SELECT diagnostico, COUNT(*) AS casos
FROM consultas
GROUP BY diagnostico
ORDER BY casos DESC
LIMIT 5;
```

*Spoiler: "Control rutinario" significa que alguien se cuida. Bien por ellos.*

---

## Pregunta 6
**¿Cuantas consultas ha realizado cada doctor? Muestra nombre del doctor y cantidad.**

```sql
SELECT d.nombre, COUNT(*) AS total_consultas
FROM doctores d
JOIN consultas c ON d.id = c.doctor_id
GROUP BY d.id, d.nombre
ORDER BY total_consultas DESC;
```

*Los mas ocupados probablemente duermen en el consultorio.*

---

## Pregunta 7
**¿Cual es el doctor con mas anos de experiencia? Muestra nombre, especialidad y anos.**

```sql
SELECT nombre, especialidad, anios_experiencia
FROM doctores
ORDER BY anios_experiencia DESC
LIMIT 1;
```

*El Yoda de la medicina. Probablemente tiene historias increibles.*

---

## Pregunta 8
**Lista los pacientes menores de 18 anos junto con su tipo de sangre.**

```sql
SELECT nombre, edad, tipo_sangre
FROM pacientes
WHERE edad < 18
ORDER BY edad;
```

*Los valientes del hospital. Merecen una paleta despues de cada consulta.*

---

## Pregunta 9
**¿Cual es el ingreso total generado por cada especialidad medica?**

```sql
SELECT d.especialidad, SUM(c.costo) AS ingresos_totales
FROM doctores d
JOIN consultas c ON d.id = c.doctor_id
GROUP BY d.especialidad
ORDER BY ingresos_totales DESC;
```

*Datos que el departamento de finanzas mira con una sonrisa (o no).*

---

## Pregunta 10
**¿Cuantos pacientes hombres y mujeres hay en cada rango de edad? (0-17, 18-40, 41-65, 65+)**

```sql
SELECT
    CASE
        WHEN edad < 18 THEN '0-17'
        WHEN edad BETWEEN 18 AND 40 THEN '18-40'
        WHEN edad BETWEEN 41 AND 65 THEN '41-65'
        ELSE '65+'
    END AS rango_edad,
    genero,
    COUNT(*) AS cantidad
FROM pacientes
GROUP BY rango_edad, genero
ORDER BY rango_edad, genero;
```

*Datos demograficos: el pan de cada dia de todo epidemiologo.*

---

## Pregunta 11
**Lista los doctores que han atendido mas de 30 consultas, mostrando nombre y total de consultas.**

```sql
SELECT d.nombre, COUNT(*) AS total_consultas
FROM doctores d
JOIN consultas c ON d.id = c.doctor_id
GROUP BY d.id, d.nombre
HAVING COUNT(*) > 30;
```

*Los heroes sin capa (pero con bata blanca).*

---

## Pregunta 12
**¿Cuales pacientes han tenido mas de 3 consultas en el ultimo ano?**

```sql
SELECT p.nombre, COUNT(*) AS num_consultas
FROM pacientes p
JOIN consultas c ON p.id = c.paciente_id
WHERE c.fecha >= DATE('now', '-1 year')
GROUP BY p.id, p.nombre
HAVING COUNT(*) > 3;
```

*Clientes frecuentes. Ojala sean solo chequeos de rutina.*

---

> "Un buen analista de datos nunca autodiagnostica... pero si optimiza queries."
