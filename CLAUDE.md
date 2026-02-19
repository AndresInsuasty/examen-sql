# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Repositorio educativo con 5 examenes SQL basados en bases de datos SQLite tematicas (gimnasio, restaurante, hospital, banco, bar). Cada examen tiene 12 preguntas de nivel bajo-intermedio.

## Commands

```bash
# Instalar dependencias
uv sync

# Regenerar una base de datos (reemplazar con el nombre deseado)
uv run python src/generadores/gimnasio.py

# Conectarse a una base de datos para probar queries
sqlite3 data/gimnasio.db
```

## Architecture

**Generadores** (`src/generadores/`): Scripts Python que usan `faker` para generar datos ficticios en espanol. Cada generador:
- Crea 3 tablas relacionadas con claves foraneas
- Genera ~100-800 registros por base de datos
- Guarda el resultado en `data/<nombre>.db`

**Examenes** (`examenes/`): Markdown con diagrama ER ASCII y 12 preguntas en lenguaje natural.

**Soluciones** (`soluciones/`): Queries SQL resueltas con comentarios humoristicos para analistas de datos.

## Database Schema Pattern

Todas las BDs siguen el patron de 3 tablas:
1. **Entidad principal** (miembros, meseros, pacientes, clientes, bartenders)
2. **Entidad secundaria** (clases, mesas, doctores, cuentas, bebidas)
3. **Tabla de relacion/transacciones** (asistencias, ordenes, consultas, transacciones, ventas)

## Conventions

- Locale de faker: `es_ES`
- Campos booleanos: 1=true, 0=false
- Genero: 'M'/'F'
- Fechas: formato SQLite DATE
