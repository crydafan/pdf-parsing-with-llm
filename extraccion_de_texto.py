import pdfplumber

import re


ROMAN_SECTION_PATTERN = re.compile(
    r"\n\s*((?:I|II|III|IV|V|VI|VII|VIII|IX)\.\s+.+?)\n(?=[A-ZÁÉÍÓÚÑ])",
    re.MULTILINE,
)


def extraer_texto(ruta: str) -> str:
    texto_completo: list[str] = []

    with pdfplumber.open(ruta) as pdf:
        for page in pdf.pages:
            texto = page.extract_text(x_tolerance=2, y_tolerance=2)

            if not texto:
                continue

            texto_completo.append(texto)

    return "\n".join(texto_completo)


def limpiar_texto(texto: str) -> str:
    # Remove page numbers like 1/12
    # texto = re.sub(r"\n\d+/\d+\n", "\n", texto)

    # Remove timestamp
    # texto = re.sub(r"\d{2}/\d{2}/\d{4}.*", "", texto)

    # Remove excessive spaces
    texto = re.sub(r"[ \t]+", " ", texto)

    # Normalize newlines
    texto = re.sub(r"\n{2,}", "\n\n", texto)

    return texto.strip()


def extraer_secciones(texto: str) -> dict[str, str]:
    matches = list(ROMAN_SECTION_PATTERN.finditer(texto))

    secciones: dict[str, str] = {}

    for i, match in enumerate(matches):
        section_title = match.group(1).strip()
        start = match.end()

        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            end = len(texto)

        section_content = texto[start:end].strip()
        secciones[section_title] = section_content

    return secciones
