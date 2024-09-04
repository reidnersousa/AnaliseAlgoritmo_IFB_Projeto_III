
import os 
import funcoes as fc

def knapsack_dp(capacidade,itens):
    solucao_otima=[]
    valores = []
    pesos = []
    ## Ajustando os dados para o knapsack
    for _, item in enumerate(itens):
        valores.append(item['valor'])
        pesos.append(item['peso'])
    
    ## Criando a tabela com valores 0
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(len(valores) + 1)]
    ## Preenche a tabela dp
    for i in range(1,len(valores)+1):
        for w in range(1,capacidade+1):
            if pesos[i-1]<= w:
                dp[i][w] = max(dp[i-1][w],dp[i-1][w-pesos[i-1]]+valores[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    max_valores = dp[len(valores)][capacidade]
    print(max_valores)
    return 1,max_valores,3
    

root = r'large_scale'

k1,k2,k3 = fc.sepera_lotes(root)
print(k1[2])
caminho_arquivo_pesos = os.path.join(root,k1[2])


itens ,capacidade ,y = fc.ler_instancia(caminho_arquivo_pesos)
mochila, valor_total , saida = knapsack_dp(capacidade,itens)
