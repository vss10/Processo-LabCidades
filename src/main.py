import pandas as pd
from util import normalizar_texto, situacoes_validas

#tentativa de leitura do arquivo csv
try:
    debitos_data = pd.read_csv('../data/processed/debitos_tratados.csv', sep=';')
except Exception:
    raise ValueError('Erro ao ler arquivo de débitos')
print('Base de débitos lida com sucesso!')

#tentativa da leitura do arquivo de parâmetros
try:
    with open('../parameters/parametros.txt', 'r') as f:
        linhas = [linha.strip() for linha in f.readlines()]
except Exception:
    raise ValueError('Erro ao ler arquivo de parâmetros')
print('Parâmetros lidos com sucesso')

#verificação do formato do arquivo .txt
if(len(linhas)<4):
    raise ValueError('Arquivo de parâmetros incompleto')
    
if not (linhas[0].lower().startswith('situacaopagamento')):
    raise ValueError('Primeira Linha em formato invalido.')

if normalizar_texto(linhas[2]) != "variaveis:":
    raise ValueError('Terceira linha inválida, Esperado - Variáveis:')

print('Formato do arquivo de parâmetros validados')

#extrair situação:
try:
    situacao = linhas[0].split('=')[1]
    situacao = (situacao.replace("'", "").replace('"', "").strip())
except Exception:
    raise ValueError("Erro a interpretar situação de pagamento")

#validar situação
situacao_normalizada = normalizar_texto(situacao)
if(situacao_normalizada not in situacoes_validas):
    raise ValueError(f'Situação inválida: {situacao}')

situacao = situacoes_validas[situacao_normalizada]

#extrair variáveis
variaveis = linhas[3:]
variaveis = [v for v in variaveis if v != '']
if(len(variaveis)==0):
    raise ValueError('Não foram informadas variáveis')

#validar variáveis
variaveis_invalidas = []

for v in variaveis:
    if v not in debitos_data.columns:
        variaveis_invalidas.append(v)

if(len(variaveis_invalidas)>0):
    raise ValueError('Variáveis inexistentes na base: ', ', '.join(variaveis_invalidas))

print('Variaveis validadas com sucesso')

#filtragem
filtrado = debitos_data[debitos_data['situacaoPagamento']==situacao]

#selecao das colunas
saida = filtrado[variaveis]

#exportar arquivo .csv
try:
    saida.to_csv("../data/processed/saida.csv", index=False, sep=';', encoding='utf-8-sig')

except Exception:
    raise ValueError('Erro ao gerar arquivo de saída')