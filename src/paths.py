# pathlib para facilitar o trabalho com caminhos de arquivos
from pathlib import Path

# definindo a raiz do projeto
base_dir = Path(__file__).resolve().parent.parent
# definindo o caminho da base de dados
raw_data_path = base_dir / "data" / "raw" / "base_rh.csv"
# caminho para a base de dados tratada
processed_data_path = base_dir / "data" / "processed" / "base_rh_clean.csv"