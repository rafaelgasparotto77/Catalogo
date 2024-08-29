# Importe as bibliotecas necessárias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# Carregue os dados (supondo que você já tenha o DataFrame 'df' com 'texto_preprocessado' e 'sentiment')
# Certifique-se de que a coluna sentiment está presente e contém 'positive' ou 'negative'
df = pd.read_csv('IMDB Dataset.csv')

# Codifique os rótulos (sentimentos) como números
label_encoder = LabelEncoder()
df['sentiment'] = label_encoder.fit_transform(df['sentiment'])  # 0 para negativo, 1 para positivo

# Divida os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(df['review'], df['sentiment'], test_size=0.2, random_state=42)

# Tokenização e padronização dos dados
max_words = 5000
tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(X_train)

X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)

max_len = 100  # Comprimento máximo das sequências
X_train_pad = pad_sequences(X_train_seq, maxlen=max_len)
X_test_pad = pad_sequences(X_test_seq, maxlen=max_len)

# Crie o modelo da rede neural
model = Sequential()
model.add(Embedding(max_words, 128, input_length=max_len))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(100))
model.add(Dense(1, activation='sigmoid'))  # Ativação sigmoid para classificação binária

# Compile o modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Treine o modelo
batch_size = 64
epochs = 5

history = model.fit(X_train_pad, y_train, epochs=epochs, batch_size=batch_size, validation_data=(X_test_pad, y_test), verbose=2)

# Avalie o modelo
loss, accuracy = model.evaluate(X_test_pad, y_test, verbose=0)
print(f'Accuracy: {accuracy * 100:.2f}%')

import joblib

# Supondo que 'model' seja seu modelo treinado
joblib.dump(model, 'modelo_recomendacao.pkl')

# Supondo que 'tokenizer' seja seu tokenizer treinado
joblib.dump(tokenizer, 'tokenizer.pkl')