# from enum import Enum

# from models.modelo_trabajo import ExperienciaLaboral
# from models.modelo_educacion import Estudio
# from models.modelo_juicios import Declaracion
# from models.modelo_bienes import BienMueble, BienInmueble, DesgloseIngresos
from typing import Type, TypeVar

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

# from extraccion_de_texto import extraer_secciones, extraer_texto, limpiar_texto
from models.modelo_bienes import Bienes
from models.modelo_candidato import Candidato
from models.modelo_juicios import Declaraciones
from models.modelo_trabajo import ExperienciasLaborales
from models.modelo_educacion import Estudios


load_dotenv()


T = TypeVar("T", bound=BaseModel)


"""
class Seccion(Enum):
    INFORMACION_PERSONAL = (0, Candidato)
    EXPERIENCIA_LABORAL = (1, ExperienciaLaboral)
    EDUCACION = (2, Estudio)
    SENTENCIAS_JUDICIALES = (5, Declaracion)
    # RENUNCIAS = (6,)
    BIENES = (7,)
"""


cliente = OpenAI()


def extraccion_estructurada(datos: str, modelo: Type[T]) -> T | None:
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

    resultado = respuesta.output_parsed
    if not resultado:
        print("No se pudo parsear la respuesta.")
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
