import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Carregue os dados do arquivo data.csv
df = pd.read_csv('data.csv')

# Verifique se a coluna correta está presente no DataFrame
if 'Movie Rating' in df.columns:
    X = df[['Movie Rating', 'Votes']]
    y = df['Movie Rating']  # Suponha que 'Movie Rating' represente a qualidade dos filmes
else:
    print("Coluna 'Movie Rating' não encontrada no DataFrame.")

# Divida os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crie o modelo da rede neural para regressão
model = Sequential()
model.add(Dense(64, input_dim=2, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))  # Linear activation para regressão

# Compile o modelo
model.compile(loss='mean_squared_error', optimizer='adam')

# Treine o modelo
batch_size = 64
epochs = 10

history = model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_data=(X_test, y_test))

# Avalie o modelo
loss = model.evaluate(X_test, y_test)
print(f'Loss: {loss}')

# Salve o modelo para uso posterior
model.save('modelo_recomendacao.h5')