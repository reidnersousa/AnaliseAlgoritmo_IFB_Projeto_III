

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
k =  ['knapPI_1_10000_1000_1', 'knapPI_1_1000_1000_1', 'knapPI_1_100_1000_1',
    'knapPI_1_2000_1000_1', 'knapPI_1_200_1000_1', 'knapPI_1_5000_1000_1', 
    'knapPI_1_500_1000_1']
lista_q = [0.13478294038644756, 0.44201236629176377, 1.0,
          0.3023638418079096, 1.0, 0.19653327642273483, 0.6439338808607964]
lista_y = [10000, 1000, 100, 2000, 200, 5000, 500]
lista_tempo=  [3.439962863922119, 0.32391858100891113,
              0.025923490524291992, 0.6470110416412354, 0.05793118476867676, 
              1.697784423828125, 0.14803838729858398]

fc.grafico_curva(lista_tempo,lista_y)