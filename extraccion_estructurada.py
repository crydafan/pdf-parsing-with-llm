from typing import Type, TypeVar

from dotenv import load_dotenv
from openai import APIError, BadRequestError, OpenAI, RateLimitError
from pydantic import BaseModel

from modelos.modelo_bienes import Bienes
from modelos.modelo_candidato import Candidato
from modelos.modelo_educacion import Estudios
from modelos.modelo_juicios import Declaraciones
from modelos.modelo_trabajo import ExperienciasLaborales

load_dotenv()


T = TypeVar("T", bound=BaseModel)


cliente = OpenAI()


def extraccion_estructurada(datos: str, modelo: Type[T]) -> T | None:
    try:
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
                    "content": f"Extrae la información relevante de la siguiente hoja de vida. Devuelve toda la información en un formato estructurado. La hoja de vida es la siguiente:\n\n{datos}",
                },
            ],
            text_format=modelo,
        )
    except BadRequestError as e:
        print(
            f"[ERROR] Solicitud inválida para '{modelo.__name__}': {e.message} (código: {e.code})"
        )
        return None
    except RateLimitError as e:
        print(f"[ERROR] Límite de tasa alcanzado para '{modelo.__name__}': {e.message}")
        return None
    except APIError as e:
        print(
            f"[ERROR] Error de la API de OpenAI para '{modelo.__name__}': {e.message} (status: {e.code})"
        )
        return None

    resultado = respuesta.output_parsed
    if not resultado:
        print(f"[WARN] No se pudo parsear la respuesta para '{modelo.__name__}'.")
        return None

    return resultado


def extraer_informacion_personal(datos_en_secciones: list[str]) -> Candidato | None:
    seccion = 0
    return extraccion_estructurada(datos_en_secciones[seccion], Candidato)


def extraer_experiencia_laboral(
    datos_en_secciones: list[str],
) -> ExperienciasLaborales | None:
    seccion = 1
    return extraccion_estructurada(datos_en_secciones[seccion], ExperienciasLaborales)


def extraer_educacion(datos_en_secciones: list[str]) -> Estudios | None:
    seccion = 2
    return extraccion_estructurada(datos_en_secciones[seccion], Estudios)


def extraer_sentencias_judiciales(
    datos_en_secciones: list[str],
) -> Declaraciones | None:
    seccion = 5
    return extraccion_estructurada(datos_en_secciones[seccion], Declaraciones)


def extraer_bienes(datos_en_secciones: list[str]) -> Bienes | None:
    seccion = 6
    return extraccion_estructurada(datos_en_secciones[seccion], Bienes)
