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
import timeit
root = r'large_scale'

### Nome do arquivo de cada instancia 
k1,k2,k3 = fc.sepera_lotes(root)
print('k1',k1)
idx = 2
print("k1[",idx,"]",k3[idx])
### Leitura de arquivo
nome_arquivo = k3[idx]
path_arquivo = os.path.join(root,nome_arquivo)
itens , capacidade , saida_esperada , y = fc.ler_instancia(path_arquivo)

### dp 
capacidade_max ,vetor_otima = knapsack_dp(itens,capacidade)
print("capacidade maxima possivel",capacidade_max)
print("vetor Solução melhor possível",vetor_otima)



### Criar uma função que escrever o melhor