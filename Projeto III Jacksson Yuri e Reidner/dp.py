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
import os
import time

def processar_arquivo_dp(k, root):
    
    lista_q = []
    lista_y = []
    lista_tempo = []


    for idx in range(len(k)):
        
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

        # Beneficio extraindo do vetor solução da última linha 
        beneficio_arquivo = fc.calcular_beneficio(itens, saida_arquivo)

        # Cálculo da métrica de qualidade
        q = fc.metrica_qualidade(beneficio_dp, beneficio_arquivo)

        
        lista_q.append(q)
        lista_y.append(y)
        lista_tempo.append(tempo_exc)

       
        print("q em relação a dp com a lista binária do arquivo:",q)
        print("Capacidade máxima possível: ",capacidade_max)
        print("Tempo de execução:",tempo_exc,"segundos  Nome do arquivo:",nome_arquivo)

   
    return lista_q, lista_y, lista_tempo


import os 
import time


### Nome do arquivo de cada instancia 
root = os.path.join(os.getcwd(), 'large_scale')  # Garante compatibilidade com diferentes sistemas operacionais

k1,k2,k3 = fc.sepera_lotes(root)

k = k2
lista_q, lista_y, lista_tempo = processar_arquivo_dp(k, root)

print("dp")
print("k:", k)
print("lista_q:", lista_q)
print("lista_y:", lista_y)
print("lista_tempo:", lista_tempo)