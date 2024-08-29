from flask import Flask, request, render_template
import joblib
import pandas as pd
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer

app = Flask(__name__)

# Carregue o modelo e o tokenizer
model = joblib.load('modelo_recomendacao.pkl')
tokenizer = joblib.load('tokenizer.pkl')  # Salve e carregue o tokenizer também

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        # Pré-processar a crítica
        review_seq = tokenizer.texts_to_sequences([review])
        padded_review = pad_sequences(review_seq, maxlen=100)
        
        # Faça a previsão
        prediction = model.predict(padded_review)
        sentiment = 'Positivo' if prediction[0][0] > 0.5 else 'Negativo'
        
        return render_template('index.html', prediction=sentiment)

if __name__ == '__main__':
    app.run(debug=True)