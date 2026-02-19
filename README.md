# Examenes SQL

Repositorio educativo con 5 examenes de SQL basados en bases de datos tematicas. Ideal para practicar y evaluar habilidades SQL de nivel bajo-intermedio.

## Contenido

El repositorio incluye 5 bases de datos SQLite con tematicas diferentes:

| Base de Datos | Tema | Tablas |
|---------------|------|--------|
| `gimnasio.db` | Sistema de gimnasio | miembros, clases, asistencias |
| `restaurante.db` | Gestion de restaurante | meseros, mesas, ordenes |
| `hospital.db` | Sistema hospitalario | pacientes, doctores, consultas |
| `banco.db` | Entidad bancaria | clientes, cuentas, transacciones |
| `bar.db` | Bar/Cantina | bartenders, bebidas, ventas |

Cada examen incluye:
- Diagrama Entidad-Relacion en formato ASCII
- 12 preguntas de logica de negocio en lenguaje natural
- Solucion con query SQL y respuesta explicada

## Estructura del Proyecto

```
examen-sql/
├── pyproject.toml              # Configuracion del proyecto
├── README.md                   # Este archivo
├── src/
│   └── generadores/            # Scripts para generar las BDs
│       ├── gimnasio.py
│       ├── restaurante.py
│       ├── hospital.py
│       ├── banco.py
│       └── bar.py
├── data/                       # Bases de datos SQLite
│   ├── gimnasio.db
│   ├── restaurante.db
│   ├── hospital.db
│   ├── banco.db
│   └── bar.db
├── examenes/                   # Preguntas de cada examen
│   ├── examen_gimnasio.md
│   ├── examen_restaurante.md
│   ├── examen_hospital.md
│   ├── examen_banco.md
│   └── examen_bar.md
└── soluciones/                 # Respuestas y queries SQL
    ├── solucion_gimnasio.md
    ├── solucion_restaurante.md
    ├── solucion_hospital.md
    ├── solucion_banco.md
    └── solucion_bar.md
```

## Requisitos

- Python 3.10+
- uv (gestor de paquetes)

## Instalacion

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd examen-sql

# Instalar dependencias
uv sync
```

## Uso

### Realizar un examen

1. Abre el archivo de examen correspondiente en `examenes/`
2. Lee el diagrama ER para entender la estructura de la BD
3. Conectate a la base de datos usando SQLite:

```bash
sqlite3 data/gimnasio.db
```

4. Responde las 12 preguntas escribiendo queries SQL
5. Consulta las soluciones en `soluciones/` para verificar tus respuestas

### Regenerar las bases de datos

Si deseas regenerar los datos con nuevos valores aleatorios:

```bash
uv run python src/generadores/gimnasio.py
uv run python src/generadores/restaurante.py
uv run python src/generadores/hospital.py
uv run python src/generadores/banco.py
uv run python src/generadores/bar.py
```

## Temas SQL Evaluados

Los examenes cubren los siguientes conceptos:

- SELECT basico con filtros WHERE
- Operadores de comparacion (>, <, =, BETWEEN, IN, LIKE)
- Funciones de agregacion (COUNT, SUM, AVG, MAX, MIN)
- GROUP BY con y sin HAVING
- ORDER BY (ASC/DESC)
- INNER JOIN entre tablas
- Subconsultas simples
- CASE WHEN para categorizacion
- Combinacion de multiples conceptos

## Nivel de Dificultad

Bajo-Intermedio. Ideal para:
- Estudiantes aprendiendo SQL
- Profesionales preparando entrevistas tecnicas
- Cursos de introduccion a bases de datos
- Practica autodidacta

## Licencia

Uso educativo libre.
