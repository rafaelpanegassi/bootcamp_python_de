# Para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# %%
from typing import Dict, Any

livro: Dict[str,int] = { 
    'titulo' : 'Data',
    'autor':'Rafael',
    'ano':2024
} 

print(livro)

listagem_dicionario: list = livro.items()
for i in listagem_dicionario:
    print(i)


