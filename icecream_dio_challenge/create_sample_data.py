import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def create_data():
    # Gerando dados para exemplo]

    # Definindo uma semente fixa para acertividade
    np.random.seed(42)

    # Gerando 100 resultados de temperatura entre 20 e 40
    temperatures = np.random.uniform(20, 40, 100)

    # Gerando vendas correlacionadas com a temperatura
    orders = 10 * temperatures + np.random.normal(0, 10, 100)

    # Criando um DataFrame com nossos dados para exportar para .xlsx
    df = pd.DataFrame({'temperatura': temperatures, 'vendas': orders})

    return df
    

# Isso aqui significa que o código só vai rodar se o arquivo for executado diretamente
if __name__ == '__main__':
    # Utilizando a função que criamos para gerar os dados
    df = create_data()

    # Exportando para .xlsx
    df.to_excel('dados_sorvete.xlsx', index=False)
    print('Arquivo gerado com sucesso!')
