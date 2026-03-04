# Extracción de Hojas de Vida — Observa Perú

Herramienta interna para extraer y estructurar automáticamente la información contenida en las hojas de vida de candidatos políticos, como parte del proyecto **Observa Perú**.

## ¿Qué hace?

Lee los PDFs de hojas de vida ubicados en `data/hojas-vida/`, los procesa con GPT-4.1 y genera un único archivo `candidatos.json` con los datos estructurados de todos los candidatos.

La información extraída por candidato incluye:

- Datos personales (nombre, sexo, fecha de nacimiento, lugar de nacimiento, residencia)
- Experiencia laboral
- Estudios
- Sentencias y juicios
- Bienes (inmuebles, muebles, participaciones societarias e ingresos)

## Uso

```bash
python main.py
```

El archivo `candidatos.json` se genera automáticamente al finalizar.

## Requisitos

- Python 3.11+
- Una API key de OpenAI en un archivo `.env`:
  ```
  OPENAI_API_KEY=sk-...
  ```
- Dependencias:
  ```bash
  uv sync
  ```
