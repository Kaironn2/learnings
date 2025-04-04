import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import mlflow
import mlflow.sklearn


# Carregando os dados que geramos no arquivo create_sample_data.py
df = pd.read_excel('dados_sorvete.xlsx')


# x será nossa entrada e precisa estar em 2D, então precisa ser um DataFrame
x = df[['temperatura']]
# y será nossa saída e pode ser uma Series, então não precisa ser um DataFrame
y = df['vendas']

# Dividindo os dados para treino e teste
# Passando a mesma seed para garantir consistência nos resultados. Então usamos 42 de novo
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


# Definindo nosso experimento do mlflow
mlflow.set_experiment('vendas_de_sorvetes')

# Iniciando o experimento e treinando o modelo
with mlflow.start_run():
    # Setando nosso modelo
    model = LinearRegression()
    model.fit(x_train, y_train)


    # Registrando parametros e metricas
    pred_train = model.predict(x_train)
    pred_test = model.predict(x_test)
    mse_train = mean_squared_error(y_train, pred_train)
    mse_test = mean_squared_error(y_test, pred_test)


    # Salvando o modelo
    mlflow.sklearn.log_model(model, 'model')

    print('MSE Treino:', mse_train)
    print('MSE Teste:', mse_test)

