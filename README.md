# Catalogo
Um catalogo de filmes
import requests
import pandas as pd

def get_movie_data(movie_title, api_key):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    api_key = "SUA_CHAVE_DE_API_AQUI"  # Substitua pela sua chave de API do Rotten Tomatoes
    movie_title = input("Digite o título do filme: ")
    
    movie_data = get_movie_data(movie_title, api_key)
    
    if 'Error' in movie_data:
        print("Filme não encontrado.")
        return
    
    movie_info = {
        "Nome do Filme": movie_data["Title"],
        "Direção": movie_data["Director"],
        "Gênero": movie_data["Genre"],
        "Ano": movie_data["Year"],
        "Nota": movie_data["imdbRating"]
    }
    
    df = pd.DataFrame([movie_info])
    df.to_excel("filme.xlsx", index=False)
    print("Dados do filme exportados para filme.xlsx com sucesso!")

if __name__ == "__main__":
    main()
