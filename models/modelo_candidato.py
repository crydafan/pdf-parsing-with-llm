from enum import Enum

from pydantic import BaseModel, Field, computed_field, field_validator

from models.modelos_comunes import Lugar


class Sexo(str, Enum):
    MASCULINO = "masculino"
    FEMENINO = "femenino"


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
