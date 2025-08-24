import pandas as pd

# Primeiro Carregar o arquivo CSV 
df = pd.read_csv("blocos_carnaval_2018.csv", sep=";")

# Depois limpo as colunas e dados 
df.columns = df.columns.str.strip()
df['Bairro'] = df['Bairro'].str.strip()
df['Bloco'] = df['Bloco'].str.strip()
df['Data'] = df['Data'].str.strip()

# Entrada do usuário
bairro_input = input("Digite o nome do bairro: ").strip().lower()

# Filtrar por bairro
df_bairro = df[df['Bairro'].str.lower() == bairro_input]

if df_bairro.empty:
    print(f"Nenhum bloco encontrado no bairro {bairro_input}.")
else:
    blocos_por_dia = df_bairro.groupby('Data')['Bloco'].apply(list)
    print("\nBlocos por dia no bairro", bairro_input)
    print(blocos_por_dia)

    exportar = input("\nDeseja exportar o resultado para CSV? (s/n): ").strip().lower()
    if exportar == 's':
        arquivo = f"blocos_{bairro_input.replace(' ', '_')}.csv"
        df_bairro.to_csv(arquivo, index=False)
        print(f"Arquivo '{arquivo}' exportado com sucesso!")
