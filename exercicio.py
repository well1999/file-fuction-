### 1. Funções para arquivo csv Complete a função abaixo para extrair uma coluna do arquivo csv em uma lista. Os elementos devem ter o tipo de dado correto.###
def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int, tipo_dado: str):
    coluna = []
%%writefile carros.csv
id,valor_venda,valor_manutencao,portas,pessoas,porta_malas
1,vhigh,med,2,2,small
2,med,vhigh,2,2,small
3,low,vhigh,2,2,small
4,low,high,2,2,small
5,low,high,2,2,small
6,low,high,4,4,big
7,low,high,4,4,big
8,low,med,2,2,small
9,low,med,2,2,small
10,low,med,2,2,small
11,low,med,4,4,big
12,low,low,2,2,small
13,low,low,4,4,small
14,low,low,4,4,med

valor_venda = extrai_coluna_csv(
nome_arquivo='./carros.csv',
indice_coluna=1,
tipo_dado='str'
)
print(valor_venda)

###2. Funções para arquivo txt Complete a função abaixo para extrair uma as palavras de uma linha do arquivo txt em uma lista.
Você pode testar a função com os códigos abaixo.
 # extrair a coluna pessoas
pessoas = extrai_coluna_csv(
nome_arquivo='./carros.csv',
indice_coluna=4,
tipo_dado='int'
)
print(pessoas) # deve retornar [2, 2, 2, ...]
 def extrai_linha_txt(nome_arquivo: str, numero_linha: int):
palavras_linha = []

return palavras_linha
linha10 = extrai_linha_txt(nome_arquivo='./carros.txt', numero_linha=10)
print(linha10)
