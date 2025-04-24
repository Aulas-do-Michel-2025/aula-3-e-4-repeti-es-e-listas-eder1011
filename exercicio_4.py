"""
#### Exercício 4 - Lista de organismos

Você recebeu uma lista que contém, para cada organismos detectado numa amostra, uma outra lista contendo a 
quantidade de leituras que esse organismo teve em cada identificador taxonômico.

Obs: Deixei a lista direto no exercício para facilitar. Mas faça o código para descobrir, não coloque a resposta direto!

Por exemplo:

[[100, 200, 300], [1, 99, 10000], [1, 1, 1]].

Eu quero que você identifique o organismo que teve a maior média de leituras entre todos os organismos da lista.

Ao identificar digite a posição em que esse organismo se encontra na lista.

No exemplo acima, você imprimiria:

"O organismo com maior média é o da posição 1 da lista."

Porque o organismo da posição 0 tem média de (100 + 200 + 300) / 3 = 200, o organismo da posição 0
tem média de (1 + 99 + 10000) / 3 = 3366,66 e o da posição 2 tem média de (1 + 1 + 1) / 3 = 1.

Logo o da posição 1 é maior.

------

Exemplo:
lista_de_organismos = [[100, 200, 300], [1, 99, 10000], [1, 1, 1]]

Resposta:
O organismo com maior média é o da posição 1 da lista.

Dica: Utilize mais de um for para resolver o exercício, um para a lista de organismos e um para cada lista. Cuidado com a identação.

O cálculo de média já foi feito em sala e pode ser usado de exemplo.
"""

# Lista
lista_de_organismos = [[50, 50, 50], [125, 99, 12], [19, 91, 42], [40, 189, 0], [1, 0, 0], [100, 100, 70], [99, 12, 12]]

# Fazer a partir daqui
soma = 0
tamanho = len(lista_de_organismos[0])
for valor in lista_de_organismos[0]:
    soma += valor
media0 = soma / tamanho


soma = 0
tamanho = len(lista_de_organismos[1])
for valor in lista_de_organismos[1]:
    soma += valor
media1 = soma / tamanho


soma = 0
tamanho = len(lista_de_organismos[2])
for valor in lista_de_organismos[2]:
    soma += valor
media2 = soma / tamanho


soma = 0
tamanho = len(lista_de_organismos[3])
for valor in lista_de_organismos[3]:
    soma += valor
media3 = soma / tamanho


soma = 0
tamanho = len(lista_de_organismos[4])
for valor in lista_de_organismos[4]:
    soma += valor
media4 = soma / tamanho


soma = 0
tamanho = len(lista_de_organismos[5])
for valor in lista_de_organismos[5]:
    soma += valor
media5 = soma / tamanho


soma = 0
tamanho = len(lista_de_organismos[6])
for valor in lista_de_organismos[6]:
    soma += valor
media6 = soma / tamanho


medias = media0, media1, media2, media3, media4, media5, media6
maior_media = max(medias)
posição = medias.index(maior_media)
print(f"O organismo com maior média é o da posição {posição} da lista.")
