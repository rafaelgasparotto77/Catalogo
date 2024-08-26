import requests
import pandas as pd

# Defina sua chave de API do TMDb
API_KEY = 'f4361b8e93884b5489d61b6e218415c2'

# Função para buscar filmes
def buscar_filmes(pagina=1):
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=pt-BR&page={pagina}'
    resposta = requests.get(url)
    return resposta.json()

# Função para extrair dados dos filmes
def extrair_dados(dados):
    filmes = []
    for filme in dados['results']:
        nome = filme['title']
        diretor = buscar_diretor(filme['id'])
        genero = ', '.join(buscar_generos(filme['genre_ids']))
        ano = filme['release_date'][:4]
        nota = filme['vote_average']
        
        filmes.append({
            'Nome do Filme': nome,
            'Direção': diretor,
            'Gênero': genero,
            'Ano': ano,
            'Nota': nota
        })
    return filmes

# Função para buscar o diretor do filme
def buscar_diretor(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=pt-BR'
    resposta = requests.get(url)
    dados = resposta.json()
    for membro in dados['crew']:
        if membro['job'] == 'Director':
            return membro['name']
    return 'Desconhecido'

# Função para buscar os nomes dos gêneros
def buscar_generos(genre_ids):
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=pt-BR'
    resposta = requests.get(url)
    dados = resposta.json()
    generos = {g['id']: g['name'] for g in dados['genres']}
    return [generos[id] for id in genre_ids]

# Buscar filmes
dados_filmes = buscar_filmes()
filmes_extraidos = extrair_dados(dados_filmes)

# Criar um DataFrame e exportar para Excel
df = pd.DataFrame(filmes_extraidos)
df.to_excel('filmes.xlsx', index=False)

print("Os dados dos filmes foram exportados para 'filmes.xlsx'.")