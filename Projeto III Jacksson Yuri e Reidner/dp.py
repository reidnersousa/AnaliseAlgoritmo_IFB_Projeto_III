import funcoes as fc

def print_dp_table(dp):
    # Função para imprimir a matriz dp
    for row in dp:
        print(row)
    print()

def knapsack_dp(itens, capacidade):


    valores = []
    pesos = []
    for _, item in enumerate(itens):
    
        valores.append(item['valor'])
        pesos.append(item['peso'])

   
    n = len(valores)
    # Inicializa a tabela dp com zeros
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Exibe a tabela dp inicial
    #print("Tabela dp inicial:")
    #print_dp_table(dp)

    # Preenche a tabela dp
    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - pesos[i - 1]] + valores[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
      

    # O valor máximo é dp[n][capacidade]
    valor_max = dp[n][capacidade]
   

 
    #print("valor_max",valor_max)
    ### Pegando os itens que forma a melhor solução
    w = capacidade
    itens_selecionados = []
    solucao_otima = [0] * n 
    for i in range(n,0,-1):
        if dp[i][w] != dp[i-1][w]:
            itens_selecionados.append(itens[i-1])
            solucao_otima[i-1] = 1
            w -= itens[i-1]['peso']
    itens_selecionados.reverse()
    #print(solucao_otima)
    #print(itens_selecionados)
    return valor_max , solucao_otima

import os 
import time
root = r'large_scale'

### Nome do arquivo de cada instancia 
k1,k2,k3 = fc.sepera_lotes(root)

""" 
idx = 6
print('k1',k1,'idx',idx)

### Leitura de arquivo
nome_arquivo = k1[idx]
path_arquivo = os.path.join(root,nome_arquivo)
itens , capacidade , saida_arquivo , y = fc.ler_instancia(path_arquivo)

### Tempo dp  
inicio = time.time()
capacidade_max ,saida_dp = knapsack_dp(itens,capacidade)
fim = time.time()
tempo_exc = fim - inicio
### Beneficio dp  
beneficio_dp =fc.calcular_beneficio(itens,saida_dp)
### Beneficio extraindo do vetor solução da ultima linha 
beneficio_arquivo = fc.calcular_beneficio(itens,saida_arquivo)


q  =fc.metrica_qualidade(beneficio_dp,beneficio_arquivo)
print("q em relação a dp  com a lista binaria do arquivo ",q)
print("capacidade maxima possivel",capacidade_max)
print("Tempo execucao",tempo_exc,"nome arquivo",nome_arquivo)
#print("vetor Solução melhor possível",saida_dp)


""" 

import os
import time

# Inicializar listas para armazenar os resultados
lista_q = []
lista_y = []
lista_tempo = []
k = k3
# Loop para percorrer os arquivos em k1
for idx in range(len(k)):
    # Leitura de arquivo
    nome_arquivo = k[idx]
    path_arquivo = os.path.join(root, nome_arquivo)
    itens, capacidade, saida_arquivo, y = fc.ler_instancia(path_arquivo)

    # Tempo dp
    inicio = time.time()
    capacidade_max, saida_dp = knapsack_dp(itens, capacidade)
    fim = time.time()
    tempo_exc = fim - inicio

    # Beneficio dp  
    beneficio_dp = fc.calcular_beneficio(itens, saida_dp)

    # Beneficio extraindo do vetor solução da ultima linha 
    beneficio_arquivo = fc.calcular_beneficio(itens, saida_arquivo)

    # Cálculo da métrica de qualidade
    q = fc.metrica_qualidade(beneficio_dp, beneficio_arquivo)

    # Salvar os resultados em listas
    lista_q.append(q)
    lista_y.append(y)
    lista_tempo.append(tempo_exc)

    # Exibir os resultados para cada arquivo
    print(f"q em relação a dp com a lista binária do arquivo: {q}")
    print(f"Capacidade máxima possível: {capacidade_max}")
    print(f"Tempo de execução: {tempo_exc} segundos, Nome do arquivo: {nome_arquivo}")

# Agora, `lista_q` contém os valores de `q` e `lista_y` contém os valores de `y` para cada arquivo.
print("k",k)
print("lista_q",lista_q)
print("lista_y",lista_y)
print("lista_tempo",lista_tempo)