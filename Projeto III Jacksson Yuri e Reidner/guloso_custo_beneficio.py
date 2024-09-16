

import funcoes as fc
import os 
import time

def knapsack_guloso_custo_beneficio(capacidade,itens):
    
    itens_ordenados = sorted(itens,key = lambda x : x['valor']/x['peso'],reverse = True)
    peso_total = 0
    valor_total = 0
    mochila =[]
    vetor_solucao = [0] *len(itens)
    for i,item in enumerate(itens_ordenados):
        if peso_total + item['peso'] <= capacidade:
            mochila.append(item)
            peso_total  += item['peso']
            valor_total += item['valor']

            vetor_solucao[i]= 1
        else:
            break
    return mochila, valor_total , vetor_solucao





""" 
print("k1",k1)
nome_arquivo = k1[2]
path_arquivo = os.path.join(root,nome_arquivo)
itens , capacidade , saida_esperada ,y = fc.ler_instancia(path_arquivo)
mochila , valor_total ,saida= knapsack_guloso_custo_beneficio(capacidade,itens)
beneficio_saida_esperada = fc.calcular_beneficio(itens,saida_esperada)

beneficio_saida = fc.calcular_beneficio(itens,saida)
q=fc.metrica_qualidade(beneficio_saida,beneficio_saida_esperada)

print("saida",beneficio_saida,"q",q)

""" 


def processar_arquivo_gmp(k,root):
    lista_q = []
    lista_y = []
    lista_tempo = []
    ### Pecorre k
    for idx in range(len(k)):
        nome_arquivo = k[idx]
        path_arquivo = os.path.join(root,nome_arquivo)
        itens, capacidade , saida_arquivo , y = fc.ler_instancia(path_arquivo)

        ## Tempo guloso menor_peso
        inicio = time.perf_counter()
        mochila , valor_total ,saida= knapsack_guloso_custo_beneficio(capacidade,itens)
        fim  = time.perf_counter()
        tempo_exc = fim - inicio
        ### Beneficio guloso menor peso
        beneficio_cb = valor_total
        ### Beneficio vetor solução da última linha 
        beneficio_arquivo = fc.calcular_beneficio(itens,saida_arquivo)

        
        q=fc.metrica_qualidade(beneficio_cb,beneficio_arquivo)

        lista_q.append(q)
        lista_y.append(y)
        lista_tempo.append(tempo_exc)

        
        print("q em relação a guloso custo benficio com a lista binária do arquivo:",q)
        print("Capacidade máxima possível: ",valor_total)
        print("Tempo de execução:",tempo_exc,"segundos  Nome do arquivo:",nome_arquivo)
    
    return lista_q, lista_y, lista_tempo


root = os.path.join(os.getcwd(), 'large_scale')  # Garante compatibilidade com diferentes sistemas operacionais

### Nome do arquivo de cada instancia 
k1,k2,k3 = fc.sepera_lotes(root)
k = k2
lista_q, lista_y, lista_tempo = processar_arquivo_gmp(k, root)


print("k =", k)
print("lista_q_cb =", lista_q)
print("lista_y_cb =", lista_y)
print("lista_tempo_cb =", lista_tempo)