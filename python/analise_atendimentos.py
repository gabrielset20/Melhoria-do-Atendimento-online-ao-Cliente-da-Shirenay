import pandas as pd
from pathlib import Path

arquivo = Path("../dados/Base_Atendimentos_Shineray_500_Registros.xlsx")

if not arquivo.exists():
    print("Erro: arquivo Excel não encontrado.")
    print("Confira se o arquivo está dentro da pasta 'dados' com este nome:")
    print("Base_Atendimentos_Shineray_500_Registros.xlsx")
    exit()

df = pd.read_excel(arquivo)

def classificar_tempo(tempo):
    if tempo <= 5:
        return "Bom"
    elif tempo <= 15:
        return "Regular"
    else:
        return "Ruim"

df["Classificacao_Atendimento"] = df["Tempo_Resposta_Min"].apply(classificar_tempo)

print("===== ANÁLISE DE ATENDIMENTOS SHINERAY =====")
print("Total de atendimentos:", len(df))
print("Tempo médio de resposta:", round(df["Tempo_Resposta_Min"].mean(), 2), "minutos")
print("Menor tempo de resposta:", df["Tempo_Resposta_Min"].min(), "minutos")
print("Maior tempo de resposta:", df["Tempo_Resposta_Min"].max(), "minutos")

print("\nClassificação dos atendimentos:")
print(df["Classificacao_Atendimento"].value_counts())

print("\nDesistência por classificação:")
print(df.groupby("Classificacao_Atendimento")["Cliente_Desistiu"].value_counts())

print("\nDesempenho por vendedora:")
print(df.groupby("Vendedora")["Tempo_Resposta_Min"].mean().round(2))

saida = "Analise_Atendimentos.xlsx"
df.to_excel(saida, index=False)

print("\nArquivo gerado com sucesso:", saida)
