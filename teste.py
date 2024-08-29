import importlib.util

def check_library(nltk):
    spec = importlib.util.find_spec(nltk)
    if spec is not None:
        print(f'{nltk} está instalada.')
    else:
        print(f'{nltk} não está instalada. Por favor, instale-a.')

# Substitua 'library_name' pelo nome da biblioteca que deseja verificar
check_library('nltk')
check_library('pandas')
check_library('sklearn')