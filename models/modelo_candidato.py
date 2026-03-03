from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, computed_field, field_validator


class Sexo(str, Enum):
    MASCULINO = "masculino"
    FEMENINO = "femenino"


class Lugar(BaseModel):
    country: Optional[str] = Field(
        ..., description="El pais donde se encuentra el lugar"
    )
    department: Optional[str] = Field(
        ..., description="El departamento donde se encuentra el lugar"
    )
    province: Optional[str] = Field(
        ..., description="La provincia donde se encuentra el lugar"
    )
    district: Optional[str] = Field(
        ..., description="El distrito donde se encuentra el lugar"
    )
    address: Optional[str] = Field(
        None,
        description="La dirección del lugar (si está redactada o no disponible, puede dejarse vacía)",
    )


class Candidato(BaseModel):
    nombre: str = Field(..., description="Nombre del candidato")
    sexo: Sexo = Field(..., description="Sexo del candidato")
    fecha_nacimiento: str = Field(
        ..., description="Fecha de nacimiento del candidato en formato DD/MM/AAAA"
    )

    @field_validator("fecha_nacimiento", mode="before")
    def parse_fecha_nacimiento(cls, value: str) -> str:
        return value.replace("/", "-")

    @computed_field
    @property
    def edad(self) -> int:
        from datetime import datetime

        fecha_nacimiento = datetime.strptime(self.fecha_nacimiento, "%d-%m-%Y")
        hoy = datetime.today()
        edad = (
            hoy.year
            - fecha_nacimiento.year
            - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        )
        return edad

    lugar_nacimiento: Lugar = Field(
        ..., description="Lugar de nacimiento del candidato"
    )
    residencia: Lugar = Field(
        ...,
        description="Lugar de residencia del candidato. Si no se provee el país se asume Perú",
    )
