import funcoes as fc
import os 
def knapsack_guloso_menor_peso(capacidade, itens):
    # Ordena os itens pelo peso em ordem crescente
    itens_ordenados = sorted(itens, key=lambda x: x['peso'])

    peso_total = 0
    valor_total = 0
    mochila = []
    vetor_solucao = [0] * len(itens)
    for i, item in enumerate (itens_ordenados):
        if peso_total + item['peso'] <= capacidade:
            mochila.append(item)
            peso_total += item['peso']
            valor_total += item['valor']
            vetor_solucao[i] = 1
        else:
            break
    #print(peso_total)
    return mochila, valor_total , vetor_solucao



root = r'large_scale'

### Nome do arquivo de cada instancia 
k1,k2,k3 = fc.sepera_lotes(root)

print(k1)

caminho_arquivo_pesos = os.path.join(root,k1[0])
print(caminho_arquivo_pesos)

itens ,capacidade ,vetor_solucao_otima = fc.ler_instancia(caminho_arquivo_pesos)
mochila , valor_total ,vetor_solucao= knapsack_guloso_menor_peso(capacidade,itens)


q=fc.metrica_qualidade(vetor_solucao,vetor_solucao_otima)
print(q)