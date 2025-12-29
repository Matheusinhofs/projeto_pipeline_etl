from pydantic import BaseModel, Field, field_validator
from typing import Optional
import math

class PlanilhaVendas(BaseModel):
    Organizador: int = Field(
        ge=48,      # mínimo permitido com margem
        le=17660,   # máximo permitido com margem
        description="Identificador com faixa ampliada em 5x baseada nos valores observados"
    )
    Ano_Mes: str
    Dia_da_Semana: str
    Tipo_Dia: str
    Objetivo: str
    Date: str
    AdSet_name: str
    Amount_spent: float = Field(
        ge=0,
        le=2949.8,
        description="Valor gasto com margem operacional de 5x baseada no máximo observado"
    )
    Link_clicks: Optional[int] = Field(default=None)
    Impressions: Optional[int] = Field(default=None)
    Conversions: Optional[int] = Field(default=None)
    Segmentação: str = Field(alias="Segmentação")
    Tipo_de_Anúncio: str = Field(alias="Tipo_de_Anúncio")
    Fase: str

    # -------- Tratamento de NaN → None --------
    @field_validator("Link_clicks", "Impressions", "Conversions", mode="before")
    def nan_to_none(cls, v):
        # pandas / float NaN
        if isinstance(v, float) and math.isnan(v):
            return None
        
        # pandas NA / None-like
        if v in ("NaN", "nan", "", None):
            return None
        
        return v
