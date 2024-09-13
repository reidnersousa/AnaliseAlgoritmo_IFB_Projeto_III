
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

import funcoes as fc
### Saida de dp em relação a lista binárias do arquivo:
### K1
k1_dp =  ['knapPI_1_10000_1000_1', 'knapPI_1_1000_1000_1', 'knapPI_1_100_1000_1','knapPI_1_2000_1000_1', 'knapPI_1_200_1000_1', 'knapPI_1_5000_1000_1', 'knapPI_1_500_1000_1']
lista_q_k1_dp = [0.13478294038644756, 0.44201236629176377, 1.0,0.3023638418079096, 1.0, 0.19653327642273483, 0.6439338808607964]
lista_y_k1_dp = [10000, 1000, 100, 2000, 200, 5000, 500]
lista_tempo_k1_dp=  [3.439962863922119, 0.32391858100891113,0.025923490524291992, 0.6470110416412354, 0.05793118476867676, 1.697784423828125, 0.14803838729858398]
####   Saida de guloso menor em relação a lista binaria do arquivo
## K1
lista_q_k1_gmp = [0.11564152740988598, 0.4133533933911895, 0.7489887394774243, 0.2632316384180791, 0.7118704395799964, 0.1598476435756736, 0.5649582423675364]
lista_y_k1_gmp= [10000, 1000, 100, 2000, 200, 5000, 500]
lista_tempo_k1_gmp= [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# ### Saida guloso custo_beneficio em relação a lista binária do arquivo
lista_q_k1_cb = [0.09905667909170102, 0.3397978092949012, 0.6760686563900733, 0.22945084745762712, 0.7118704395799964, 0.14396090531258027, 0.4676854835915029]
lista_y_k1_cb= [10000, 1000, 100, 2000, 200, 5000, 500]
lista_tempo_k1_cb= [0.0, 0.0010004043579101562, 0.0,0.00150299072265625, 0.0, 0.003026723861694336, 0.0]

k1_tempo = []
k1_y = []
k1_q = []

k1_tempo.append(lista_tempo_k1_dp)
k1_tempo.append(lista_tempo_k1_gmp)
k1_tempo.append(lista_tempo_k1_cb)

k1_y.append(lista_y_k1_dp)
k1_y.append(lista_y_k1_gmp)
k1_y.append(lista_y_k1_cb)

k1_q.append(lista_q_k1_dp)
k1_q.append(lista_q_k1_gmp)
k1_q.append(lista_q_k1_cb)
fc.grafico_curva(k1_tempo,k1_y,title='knapPI_1')
fc.grafico_barras(k1_q,k1_y,title='knapPI_1')