# Soluciones - Examen SQL Banco

> "Donde los INTs son dinero y los JOINs son inversiones."

---

## Pregunta 1
**¿Cual es la ciudad con mas clientes del banco y cuantos tiene?**

```sql
SELECT ciudad, COUNT(*) AS cantidad_clientes
FROM clientes
GROUP BY ciudad
ORDER BY cantidad_clientes DESC
LIMIT 1;
```

**Respuesta:** Granada (16 clientes)

*Mapa del dinero: donde Marketing planea abrir la proxima sucursal.*

---

## Pregunta 2
**¿Cual es el saldo promedio de las cuentas de tipo "Ahorro"?**

```sql
SELECT AVG(saldo) AS saldo_promedio_ahorro
FROM cuentas
WHERE tipo_cuenta = 'Ahorro';
```

**Respuesta:** 16651.27

*El sueno de todo ahorrador: ver este numero crecer.*

---

## Pregunta 3
**¿Cual es el saldo promedio de los 10 clientes con mayor saldo total?**

```sql
SELECT ROUND(AVG(saldo_total), 2) AS saldo_promedio_top10
FROM (
    SELECT SUM(cu.saldo) AS saldo_total
    FROM clientes cl
    JOIN cuentas cu ON cl.id = cu.cliente_id
    GROUP BY cl.id
    ORDER BY saldo_total DESC
    LIMIT 10
);
```

**Respuesta:** 101566.97

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

**Respuesta:** 66829.85

*Dinero entrando = banco feliz = accionistas felices.*

---

## Pregunta 6
**¿Cuantos clientes tienen mas de una cuenta y cual es el maximo de cuentas que tiene un cliente?**

```sql
SELECT COUNT(*) AS cantidad_clientes,
       MAX(cantidad_cuentas) AS max_cuentas
FROM (
    SELECT cliente_id, COUNT(*) AS cantidad_cuentas
    FROM cuentas
    GROUP BY cliente_id
    HAVING COUNT(*) > 1
);
```

**Respuesta:** 40 clientes, máximo: 3 cuentas

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

**Respuesta:** Estudiante (21 clientes)

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

**Respuesta:** 27

*Los que ya leieron "Padre Rico, Padre Pobre".*

---

## Pregunta 9
**¿Cuantas transacciones superan los 3,000 y cual es el monto total de esas transacciones?**

```sql
SELECT COUNT(*) AS cantidad,
       ROUND(SUM(monto), 2) AS monto_total
FROM transacciones
WHERE monto > 3000;
```

**Respuesta:** 186 transacciones, monto total: 750978.13
*Las que activan alertas y generan correos de "¿Fuiste tu?".*

---

## Pregunta 10
**¿Cual es el cliente mas joven y cual es el mas viejo del banco? Muestra nombre y edad de ambos.**

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
**¿Cuantos clientes de Madrid tienen cuentas de tipo "Nomina"?**

```sql
SELECT COUNT(DISTINCT cl.id) AS clientes_nomina_madrid
FROM clientes cl
JOIN cuentas cu ON cl.id = cu.cliente_id
WHERE cl.ciudad = 'Madrid'
AND cu.tipo_cuenta = 'Nomina';
```

**Respuesta:** 6

*Madrilenos con trabajo estable. El segmento favorito del banco.*

---

> "Un buen analista de datos diversifica: no solo en inversiones, sino tambien en tipos de JOINs."
