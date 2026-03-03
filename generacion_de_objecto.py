from dotenv import load_dotenv
from openai import OpenAI

from extraccion_de_texto import extraer_secciones, extraer_texto, limpiar_texto

from models.modelo_candidato import Candidato

load_dotenv()


def main():
    ruta = "data/hojas-vida/alfonso-lopez-chau-nava.pdf"

    texto = extraer_texto(ruta)
    texto_limpio = limpiar_texto(texto)
    texto_en_secciones = extraer_secciones(texto_limpio)

    _llave, texto = texto_en_secciones.items().__iter__().__next__()

    cliente = OpenAI()

    respuesta = cliente.responses.parse(
        model="gpt-4.1",
        temperature=0,
        input=[
            {
                "role": "system",
                "content": "Eres un asistente que extrae información de hojas de vida y la organiza en un formato estructurado.",
            },
            {
                "role": "user",
                "content": f"Extrae la información relevante de la siguiente hoja de vida. Devuelve toda la información en un formato estructurado. La hoja de vida es la siguiente:\n\n{texto}",
            },
        ],
        text_format=Candidato,
    )

    modelo = respuesta.output_parsed
    if not modelo:
        print("No se pudo parsear la respuesta.")
        return

    print(modelo.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
