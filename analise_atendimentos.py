import pandas as pd

arquivo = "dados/Base_Atendimentos_Shineray_500_Registros.xlsx"

df = pd.read_excel(arquivo)

def classificar_tempo(tempo):
    if tempo <= 5:
        return "Bom"
    elif tempo <= 15:
        return "Regular"
    else:
        return "Ruim"

df["Classificacao_Atendimento"] = df["Tempo_Resposta_Min"].apply(classificar_tempo)

print("===== ANÁLISE DE ATENDIMENTOS =====")
print("Total de atendimentos:", len(df))
print("Tempo médio:", round(df["Tempo_Resposta_Min"].mean(), 2))
print("Maior tempo:", df["Tempo_Resposta_Min"].max())
print("Menor tempo:", df["Tempo_Resposta_Min"].min())

print("\nClassificações:")
print(df["Classificacao_Atendimento"].value_counts())

print("\nDesistências:")
print(df.groupby("Classificacao_Atendimento")["Cliente_Desistiu"].value_counts())

df.to_excel("Analise_Atendimentos.xlsx", index=False)

print("\nArquivo gerado com sucesso!")
