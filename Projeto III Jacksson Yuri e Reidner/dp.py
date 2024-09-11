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
   

 
    print("valor_max",valor_max)
    ### Pegando os itens que forma a melhor solução
    w = capacidade
    itens_selecionados = []
    for i in range(n,0,-1):
        if dp[i][w] != dp[i-1][w]:
            itens_selecionados.append(itens[i-1])
            w -= itens[i-1]['peso']
    print(itens_selecionados)
    return valor_max

import os 
root = r'large_scale'

### Nome do arquivo de cada instancia 
k1,k2,k3 = fc.sepera_lotes(root)
nome_arquivo = k1[2]
path_arquivo = os.path.join(root,nome_arquivo)
itens , capacidade , saida_esperada , y = fc.ler_instancia(path_arquivo)
saida_dp = knapsack_dp(itens,capacidade)



