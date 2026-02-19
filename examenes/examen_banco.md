# Examen SQL - Base de Datos Banco

## Diagrama Entidad-Relacion

```
+------------------+       +------------------+       +------------------+
|     clientes     |       |     cuentas      |       |  transacciones   |
+------------------+       +------------------+       +------------------+
| id          PK   |<------| cliente_id   FK  |       | id          PK   |
| nombre           |       | id          PK   |<------| cuenta_id    FK  |
| edad             |       | tipo_cuenta      |       | tipo             |
| ocupacion        |       | saldo            |       | monto            |
| fecha_apertura   |       | fecha_apertura   |       | fecha            |
| ciudad           |       +------------------+       | descripcion      |
+------------------+                                  +------------------+
```

## Descripcion de Tablas

- **clientes**: Informacion de los clientes del banco
- **cuentas**: Cuentas bancarias de los clientes
- **transacciones**: Movimientos realizados en las cuentas

---

## Preguntas

### Pregunta 1
¿Cual es la ciudad con mas clientes del banco y cuantos tiene?

---

### Pregunta 2
¿Cual es el saldo promedio de las cuentas de tipo "Ahorro"?

---

### Pregunta 3
¿Cual es el saldo promedio de los 10 clientes con mayor saldo total?

---

### Pregunta 4
¿Cuantas transacciones de cada tipo se han realizado?

---

### Pregunta 5
¿Cual es el monto total de depositos realizados en el ultimo mes?

---

### Pregunta 6
¿Cuantos clientes tienen mas de una cuenta y cual es el maximo de cuentas que tiene un cliente?

---

### Pregunta 7
¿Cual es la ocupacion mas comun entre los clientes del banco?

---

### Pregunta 8
¿Cuantas cuentas de inversion tienen un saldo mayor a 50,000?

---

### Pregunta 9
¿Cuantas transacciones superan los 3,000 y cual es el monto total de esas transacciones?

---

### Pregunta 10
¿Cual es el cliente mas joven y cual es el mas viejo del banco? Muestra nombre y edad de ambos.

---

### Pregunta 11
¿Cual es el saldo total del banco por tipo de cuenta?

---

### Pregunta 12
¿Cuantos clientes de Madrid tienen cuentas de tipo "Nomina"?

---

## Notas

- La base de datos se encuentra en: `data/banco.db`
- Usa SQLite para ejecutar tus consultas
- Los tipos de cuenta incluyen: "Ahorro", "Corriente", "Nomina", "Inversion"
- Los tipos de transaccion incluyen: "Deposito", "Retiro", "Transferencia", "Pago"
