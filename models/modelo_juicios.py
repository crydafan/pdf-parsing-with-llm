from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class TipoDeclaracion(str, Enum):
    LABORAL = "laboral"
    PENSION_ALIMENTOS = "pension_alimentos"
    CONTRACTUAL = "contractual"
    VIOLENCIA_FAMILIAR = "violencia_familiar"


class Declaracion(BaseModel):
    tipo: TipoDeclaracion = Field(
        ..., description="El tipo de declaración o antecedente"
    )
    expediente: str = Field(
        ...,
        description="El número de expediente o identificador asociado a la declaración",
    )
    fallo: str = Field(
        ...,
        description="La resolución, decisión o fallo emitida en relación con la declaración",
    )
    informacion_adicional: Optional[str] = Field(
        None,
        description="Información adicional sobre la declaración. Extraer directamente de los datos, sin interpretación ni resumen",
    )
