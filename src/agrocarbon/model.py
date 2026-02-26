from __future__ import annotations
from dataclasses import dataclass
import pandas as pd


@dataclass(frozen=True)
class EmissionConfig:
    col_atividade: str = "atividade"
    col_fator: str = "fator_emissao"
    col_result: str = "emissao_total"


def compute_emissions(df: pd.DataFrame, cfg: EmissionConfig = EmissionConfig()) -> pd.DataFrame:
    missing = [c for c in [cfg.col_atividade, cfg.col_fator] if c not in df.columns]
    if missing:
        raise ValueError(f"Colunas ausentes: {missing}")

    out = df.copy()
    out[cfg.col_result] = out[cfg.col_atividade].astype(float) * out[cfg.col_fator].astype(float)
    return out
