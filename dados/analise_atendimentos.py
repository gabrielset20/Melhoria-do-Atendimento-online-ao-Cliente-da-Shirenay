import pandas as pd

df = pd.read_excel("Base_Atendimentos_Shineray_500_Registros.xlsx")

def classificar_tempo(tempo):
    if tempo <= 5:
        return "Bom"
    elif tempo <= 10:
        return "Regular"
    else:
        return "Ruim"

df["Classificacao_Atendimento"] = df["Tempo_Resposta_Min"].apply(classificar_tempo)

print("Tempo médio:", df["Tempo_Resposta_Min"].mean())
print("Maior tempo:", df["Tempo_Resposta_Min"].max())
print("Menor tempo:", df["Tempo_Resposta_Min"].min())

print("\nClassificação dos atendimentos:")
print(df["Classificacao_Atendimento"].value_counts())

print("\nDesistência por classificação:")
print(df.groupby("Classificacao_Atendimento")["Cliente_Desistiu"].value_counts())

df.to_excel("Analise_Atendimentos.xlsx", index=False)
