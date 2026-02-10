# importando as bibliotecas
# pandas para manipulação e análise de dados
import pandas as pd
# pathlib para facilitar o trabalho com caminhos de arquivos
from pathlib import Path

# lendo a base de dados e armazenando em um dataframe
def load_data(path: Path) -> pd.DataFrame:
  return pd.read_csv(path, sep=';')