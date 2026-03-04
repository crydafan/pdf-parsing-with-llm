from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class NivelEstudio(str, Enum):
    BACHILLER = "bachiller"
    MAESTRIA = "maestro"
    DOCTORADO = "doctorado"


class Estudio(BaseModel):
    institucion: str = Field(
        ...,
        description="El nombre de la institución educativa donde el candidato estudió",
    )
    grado: NivelEstudio = Field(..., description="El nivel de estudio del candidato")
    campo: str = Field(..., description="El campo de estudio del candidato")
    anio_graduacion: Optional[int] = Field(
        ..., description="El año en que el candidato se graduó"
    )
    informacion_adicional: Optional[str] = Field(
        ...,
        description="Notas adicionales sobre los estudios del candidato. Extraer directamente de los datos, sin interpretación ni resumen",
    )


class Estudios(BaseModel):
    estudios: list[Estudio] = Field(
        ...,
        description="Una lista de estudios del candidato",
    )
