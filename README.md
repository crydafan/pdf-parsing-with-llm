# Candidate CV Extraction — Observa Perú

An internal tool for automatically extracting and structuring information from political candidates' CVs as part of the **Observa Perú** project.

## What does it do?

The tool reads candidate CV PDFs located in `data/hojas-vida/`, processes them using GPT-4.1, and generates a single `candidatos.json` file containing structured data for all candidates.

The extracted information for each candidate includes:

* Personal information (name, sex, date of birth, place of birth, residence)
* Work experience
* Education
* Court rulings and legal proceedings
* Assets (real estate, movable property, corporate holdings, and income)

## Usage

```bash
python main.py
```

The `candidatos.json` file is generated automatically once processing is complete.

## Requirements

* Python 3.11+
* An OpenAI API key stored in a `.env` file:

```env
OPENAI_API_KEY=sk-...
```

* Dependencies:

```bash
uv sync
```
