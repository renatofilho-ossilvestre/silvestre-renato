import pandas as pd
from src.agrocarbon.model import compute_emissions


def test_compute_emissions_basic():
    df = pd.DataFrame({
        "atividade": [10, 5],
        "fator_emissao": [2.0, 3.0]
    })

    result = compute_emissions(df)

    assert result["emissao_total"].tolist() == [20.0, 15.0]
