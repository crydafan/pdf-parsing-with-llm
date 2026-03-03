from typing import Optional
from enum import Enum

from pydantic import BaseModel, Field


class TipoIngreso(str, Enum):
    REMUNERACION_BRUTA_ANUAL = "remuneracion_bruta_anual"
    INGRESO_PROFESIONAL_INDIVIDUAL = "ingreso_profesional_individual"
    OTROS_INGRESOS_ANUALES = "otros_ingresos_anuales"


class DesgloseIngresos(BaseModel):
    tipo_ingreso: TipoIngreso = Field(..., description="El tipo de ingreso")
    monto_sector_publico: float = Field(
        ..., description="El monto de ingresos provenientes del sector público"
    )
    monto_sector_privado: float = Field(
        ..., description="El monto de ingresos provenientes del sector privado"
    )
    monto_total: float = Field(..., description="El monto total de ingresos")


class BienInmueble(BaseModel):
    tipo: str = Field(..., description="El tipo de bien inmueble")
    direccion: str = Field(..., description="La dirección del bien inmueble")
    valor_estimado: float = Field(
        ..., description="El valor estimado del bien inmueble"
    )
    valor_declarado: float = Field(
        ..., description="El valor declarado por el candidato del bien inmueble"
    )
    inscrito_en_sunarp: bool = Field(
        ..., description="Indica si el bien inmueble está inscrito en SUNARP"
    )
    informacion_adicional: Optional[str] = Field(
        None,
        description="Información adicional sobre el bien inmueble. Extraer de los datos, sin interpretación ni resumen",
    )


class BienMueble(BaseModel):
    placa: str = Field(..., description="La placa del vehículo")
    caracteristicas: str = Field(..., description="Las características del vehículo")
    valor_estimado: float = Field(..., description="El valor estimado del vehículo")
    informacion_adicional: Optional[str] = Field(
        None,
        description="Información adicional sobre el vehículo. Extraer de los datos, sin interpretación ni resumen",
    )


class ParticipacionSocietaria(BaseModel):
    persona_juridica: str = Field(..., description="El nombre de la persona jurídica")
    numero_acciones_participaciones: int = Field(
        ..., description="El número de acciones o participaciones que posee"
    )
    valor_nominal_total_acciones_participaciones: float = Field(
        ...,
        description="El valor nominal total de las acciones o participaciones que posee",
    )
    informacion_adicional: Optional[str] = Field(
        None,
        description="Información adicional sobre la participación societaria. Extraer de los datos, sin interpretación ni resumen",
    )
