from typing import Optional

from pydantic import BaseModel, Field

from models.modelos_comunes import Lugar


class Empresa(BaseModel):
    nombre: Optional[str] = Field(..., description="El nombre de la empresa")
    ruc: Optional[str] = Field(
        None,
        description="El RUC (Registro Único de Contribuyentes) de la empresa (si está redactado o no disponible, puede dejarse vacío)",
    )
    lugar: Optional[Lugar] = Field(
        None,
        description="La ubicación de la sede principal de la empresa (si está redactada o no disponible, puede dejarse vacía)",
    )


class ExperienciaLaboral(BaseModel):
    empresa: Optional[Empresa] = Field(
        ...,
        description="La empresa donde trabajó el candidato",
    )
    puesto: Optional[str] = Field(..., description="El cargo desempeñado en la empresa")
    anio_inicio: str = Field(
        ...,
        description="El año de inicio de la experiencia laboral en formato YYYY",
    )
    anio_fin: Optional[str] = Field(
        None,
        description="El año de fin de la experiencia laboral en formato YYYY (si actualmente trabaja allí, puede dejarse vacío)",
    )
