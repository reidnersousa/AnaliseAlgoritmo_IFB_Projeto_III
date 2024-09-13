
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
### K1 DP
k = ['knapPI_1_10000_1000_1', 'knapPI_1_1000_1000_1', 'knapPI_1_100_1000_1', 'knapPI_1_2000_1000_1', 'knapPI_1_200_1000_1', 'knapPI_1_5000_1000_1', 'knapPI_1_500_1000_1']
lista_q_k1_dp = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
lista_y_k1_dp = [10000, 1000, 100, 2000, 200, 5000, 500]
lista_tempo_k1_dp = [257.33471393585205, 2.2898528575897217, 0.025897979736328125, 9.79906153678894, 0.03775525093078613, 63.74329352378845, 0.49369239807128906]
####   Saida de guloso menor em relação a lista binaria do arquivo
### K1 CB
k = ['knapPI_1_10000_1000_1', 'knapPI_1_1000_1000_1', 'knapPI_1_100_1000_1', 'knapPI_1_2000_1000_1', 'knapPI_1_200_1000_1', 'knapPI_1_5000_1000_1', 'knapPI_1_500_1000_1']
lista_q_k1_cb = [0.9997995199122856, 0.9916151404509843, 0.9639225975729747, 0.9973152542372882, 0.9990211781455776, 0.999688920881005, 0.9992029663513186]
lista_y_k1_cb = [10000, 1000, 100, 2000, 200, 5000, 500]
lista_tempo_k1_cb = [0.0028332993388175964, 0.0009754002094268799, 5.21000474691391e-05, 0.0005885995924472809, 0.0001256987452507019, 0.0013744998723268509, 0.00019220076501369476]

## K1 GMP
lista_q_k1_gmp = [0.8789916383835983, 0.871896959800378, 0.9503662402973653, 0.8836700564971751, 0.9560420003559352, 0.8880874783420206, 0.8728211525799633]
lista_y_k1_gmp = [10000, 1000, 100, 2000, 200, 5000, 500]
lista_tempo_k1_gmp = [0.001953599974513054, 0.0006859004497528076, 5.3299590945243835e-05, 0.0004273001104593277, 0.00010699965059757233, 0.001019999384880066, 0.00021339952945709229]

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
fc.grafico_curvas(k1_tempo,k1_y,title='knapPI_1_curvas')
fc.grafico_barras(k1_q,k1_y,title='knapPI_1_barras')