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
    #print("peso_total",peso_total)
    return mochila, valor_total , vetor_solucao



def faz_tudo(root,k1):
    l1 = []
    l2 = []
    for arquivo in (k1):
        path_arquivo = os.path.join(root,arquivo)
        itens , capacidade , saida_esperada , y = fc.ler_instancia(path_arquivo)
        mochila , valor_total ,saida= knapsack_guloso_menor_peso(capacidade,itens)
        beneficio_saida_esperada = fc.calcular_beneficio(itens,saida_esperada)
        beneficio_saida = fc.calcular_beneficio(itens,saida)

        q=fc.metrica_qualidade(beneficio_saida,beneficio_saida_esperada)
        l1.append(q)
        l2.append(y)
        k1_pi = []
        
    k1_pi.append(l1)
    k1_pi.append(l2)
    
    return k1_pi

    

root = r'large_scale'

### Nome do arquivo de cada instancia 
k1,k2,k3 = fc.sepera_lotes(root)

print("k1",k1)


k1_pi=faz_tudo(root,k1)
k2_pi=faz_tudo(root,k2)
k3_pi=faz_tudo(root,k3)


print(k1_pi)
print(k2_pi)
print(k3_pi)