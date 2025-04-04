import mlflow.sklearn
import os


# Carregando o modelo que treinamos no arquivo model_traning.py
experiment_id = '161726363035860353'
run_id = '3201b1ca127d4ae28a1ce98640d98ec6'
model = mlflow.sklearn.load_model(f'mlruns/{experiment_id}/{run_id}/artifacts/model')


# Definindo a temperatura que queremos prever
temperature = 30

# Fazendo a previsão
pred = model.predict([[temperature]])
os.system('cls') # Essa linha é só para limpar o terminal e facilitar a leitura, mas n precisa se n quiser
print(f'A previsão de vendas para {temperature} graus é: {pred[0]:.2f}')
