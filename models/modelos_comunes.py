from typing import Optional

from pydantic import BaseModel, Field


class Lugar(BaseModel):
    pais: Optional[str] = Field(..., description="El pais donde se encuentra el lugar")
    departamento: Optional[str] = Field(
        ..., description="El departamento donde se encuentra el lugar"
    )
    provincia: Optional[str] = Field(
        ..., description="La provincia donde se encuentra el lugar"
    )
    distrito: Optional[str] = Field(
        ..., description="El distrito donde se encuentra el lugar"
    )
    direccion: Optional[str] = Field(
        ...,
        description="La dirección del lugar (si está redactada o no disponible, puede dejarse vacía)",
    )
