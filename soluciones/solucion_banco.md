# Soluciones - Examen SQL Banco

> "Donde los INTs son dinero y los JOINs son inversiones."

---

## Pregunta 1
**¿Cuantos clientes tiene el banco en cada ciudad?**

```sql
SELECT ciudad, COUNT(*) AS cantidad_clientes
FROM clientes
GROUP BY ciudad
ORDER BY cantidad_clientes DESC;
```

*Mapa del dinero: donde Marketing planea abrir la proxima sucursal.*

---

## Pregunta 2
**¿Cual es el saldo promedio de las cuentas de tipo "Ahorro"?**

```sql
SELECT AVG(saldo) AS saldo_promedio_ahorro
FROM cuentas
WHERE tipo_cuenta = 'Ahorro';
```

*El sueno de todo ahorrador: ver este numero crecer.*

---

## Pregunta 3
**Lista los 10 clientes con mayor saldo total (sumando todas sus cuentas).**

```sql
SELECT cl.nombre, SUM(cu.saldo) AS saldo_total
FROM clientes cl
JOIN cuentas cu ON cl.id = cu.cliente_id
GROUP BY cl.id, cl.nombre
ORDER BY saldo_total DESC
LIMIT 10;
```

*Los que reciben llamadas del gerente en su cumpleanos.*

---

## Pregunta 4
**¿Cuantas transacciones de cada tipo se han realizado?**

```sql
SELECT tipo, COUNT(*) AS cantidad
FROM transacciones
GROUP BY tipo
ORDER BY cantidad DESC;
```

*Depositos vs Retiros: la batalla eterna.*

---

## Pregunta 5
**¿Cual es el monto total de depositos realizados en el ultimo mes?**

```sql
SELECT SUM(monto) AS total_depositos
FROM transacciones
WHERE tipo = 'Deposito'
AND fecha >= DATE('now', '-1 month');
```

*Dinero entrando = banco feliz = accionistas felices.*

---

## Pregunta 6
**Lista los clientes que tienen mas de una cuenta, mostrando nombre y cantidad de cuentas.**

```sql
SELECT cl.nombre, COUNT(*) AS cantidad_cuentas
FROM clientes cl
JOIN cuentas cu ON cl.id = cu.cliente_id
GROUP BY cl.id, cl.nombre
HAVING COUNT(*) > 1
ORDER BY cantidad_cuentas DESC;
```

*Los organizados (o los que no confian en un solo lugar).*

---

## Pregunta 7
**¿Cual es la ocupacion mas comun entre los clientes del banco?**

```sql
SELECT ocupacion, COUNT(*) AS cantidad
FROM clientes
GROUP BY ocupacion
ORDER BY cantidad DESC
LIMIT 1;
```

*Datos utiles para el departamento de Marketing y sus campanas "personalizadas".*

---

## Pregunta 8
**¿Cuantas cuentas de inversion tienen un saldo mayor a 50,000?**

```sql
SELECT COUNT(*) AS cuentas_inversion_altas
FROM cuentas
WHERE tipo_cuenta = 'Inversion'
AND saldo > 50000;
```

*Los que ya leieron "Padre Rico, Padre Pobre".*

---

## Pregunta 9
**Lista las transacciones con monto mayor a 3,000, mostrando tipo, monto y descripcion.**

```sql
SELECT tipo, monto, descripcion
FROM transacciones
WHERE monto > 3000
ORDER BY monto DESC;
```

*Las que activan alertas y generan correos de "¿Fuiste tu?".*

---

## Pregunta 10
**¿Cual es el cliente mas joven y cual es el mas viejo del banco? Muestra nombre y edad de ambos.**

```sql
-- Cliente mas joven
SELECT nombre, edad, 'Mas joven' AS categoria
FROM clientes
ORDER BY edad ASC
LIMIT 1;

-- Cliente mas viejo
SELECT nombre, edad, 'Mas viejo' AS categoria
FROM clientes
ORDER BY edad DESC
LIMIT 1;
```

*O en una sola query elegante:*

```sql
SELECT nombre, edad
FROM clientes
WHERE edad = (SELECT MIN(edad) FROM clientes)
   OR edad = (SELECT MAX(edad) FROM clientes);
```

*Del millenial ahorrador al jubilado con experiencia.*

---

## Pregunta 11
**¿Cual es el saldo total del banco por tipo de cuenta?**

```sql
SELECT tipo_cuenta, SUM(saldo) AS saldo_total
FROM cuentas
GROUP BY tipo_cuenta
ORDER BY saldo_total DESC;
```

*El patrimonio del banco desglosado. Importante para el reporte anual.*

---

## Pregunta 12
**Lista los clientes de Madrid que tienen cuentas de tipo "Nomina".**

```sql
SELECT DISTINCT cl.nombre, cl.ciudad
FROM clientes cl
JOIN cuentas cu ON cl.id = cu.cliente_id
WHERE cl.ciudad = 'Madrid'
AND cu.tipo_cuenta = 'Nomina';
```

*Madrilenos con trabajo estable. El segmento favorito del banco.*

---

> "Un buen analista de datos diversifica: no solo en inversiones, sino tambien en tipos de JOINs."
