from __future__ import annotations
from pathlib import Path
import typer
from rich import print
import pandas as pd

from .model import compute_emissions

app = typer.Typer(add_completion=False)


@app.command()
def run(
    input_path: Path = typer.Option(..., "--input", "-i", help="Arquivo CSV de entrada"),
    output_path: Path = typer.Option(Path("output.csv"), "--output", "-o", help="Arquivo CSV de saída"),
):
    """
    Executa o cálculo de emissões a partir de um CSV.
    """

    df = pd.read_csv(input_path)
    out = compute_emissions(df)
    out.to_csv(output_path, index=False)

    print(f"[green]✔ Emissões calculadas com sucesso![/green]")
    print(f"Arquivo salvo em: {output_path}")


if __name__ == "__main__":
    app()
