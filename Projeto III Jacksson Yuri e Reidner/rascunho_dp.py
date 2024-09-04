def print_dp_table(dp):
    # Função para imprimir a matriz dp
    for row in dp:
        print(row)
    print()

def knapsack(values, weights, capacity):
    n = len(values)
    # Inicializa a tabela dp com zeros
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Exibe a tabela dp inicial
    print("Tabela dp inicial:")
    print_dp_table(dp)

    # Preenche a tabela dp
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
        
        # Exibe a tabela dp após cada item
        print(f"Tabela dp após considerar o item {i} (peso={weights[i-1]}, valor={values[i-1]}):")
        print_dp_table(dp)

    # O valor máximo é dp[n][capacity]
    max_value = dp[n][capacity]
    print(f'O valor máximo que pode ser obtido é {max_value}')

    # Exibe a última linha da tabela dp
    print("Última linha da tabela dp:")
    print(dp[n])

    return max_value

# Exemplo de uso
values = [60, 100, 120]  # Valores dos itens
weights = [10, 20, 30]   # Pesos dos itens
capacity = 50            # Capacidade da mochila

max_value = knapsack(values, weights, capacity)
