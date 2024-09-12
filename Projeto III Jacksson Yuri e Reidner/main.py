

### solução otima de k1_100_1000_1
##
##  Valor total da solu��o �tima: 8568
##  Peso total da solu��o �tima: 3198 (capacidade m�xima = 995)



##  para y = 100 e  w  = 1000
### Valor m�ximo que pode ser obtido: 9147
# Itens selecionados (valor, peso): [(800, 90), (641, 46),
# (724, 29), (726, 98), (931, 70), (908, 97), (997, 199), 
# (874, 138), (700, 72), (598, 94), (791, 9), (457, 43)]
### 
import os 
import guloso_menor_peso  as gmp
import funcoes as fc
import dp as dp 


root = r'large_scale'

k1,k2,k3 = fc.sepera_lotes(root)

print("k1",k1)
print("k2",k2)
print("k3",k3)

path_arquivo = os.path.join(root,k1[2])
itens , capacidade , saida_esperada , y = fc.ler_instancia(path_arquivo)

### Mochila guloso_menor
mochila , valor_total ,saida_gmp= gmp.knapsack_guloso_menor_peso(capacidade,itens)
beneficio_gmp = fc.calcular_beneficio(itens,saida_gmp)

## Mochila dp 
capacidade_max ,saida_dp= dp.knapsack_dp(itens,capacidade)
beneficio_dp = fc.calcular_beneficio(itens,saida_dp)

q=fc.metrica_qualidade(beneficio_gmp,beneficio_dp)
print("q em relação a menor_peso com dp ",q)





def faz_tudo(root,k1):
    l1 = []
    l2 = []
    for arquivo in (k1):
        path_arquivo = os.path.join(root,arquivo)
        
        itens , capacidade , saida_esperada , y = fc.ler_instancia(path_arquivo)

        ### Mochila guloso_menor
        mochila , valor_total ,saida_gmp= gmp.knapsack_guloso_menor_peso(capacidade,itens)
        beneficio_gmp = fc.calcular_beneficio(itens,saida_gmp)

        ## Mochila dp  ## Roda o dp aqui não será bom , preciso apenas do vetor solução
        capacidade_max ,saida_dp= dp.knapsack_dp(itens,capacidade)
        beneficio_dp = fc.calcular_beneficio(itens,saida_dp)

        q=fc.metrica_qualidade(beneficio_gmp,beneficio_dp)


        l1.append(q)
        l2.append(y)
        k1_pi = []
        
    k1_pi.append(l1)
    k1_pi.append(l2)
    
    return k1_pi

k1_pi=faz_tudo(root,k1)
#k2_pi=faz_tudo(root,k2)
#k3_pi=faz_tudo(root,k3)


print(k1_pi)
#print(k2_pi)
#print(k3_pi)