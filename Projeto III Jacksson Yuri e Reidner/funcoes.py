import os 
import matplotlib.pyplot as plt 
import numpy as np
   
def ler_instancia(caminho_arquivo):
    ### A primeira linha de cada arquivo possui dois inteiros:
    ### Y = Quantidade de itens 
    ### W = capacidade da mochila 
    
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    y , w = map(int,linhas[0].split())
    #print("y",y,"w",w)
    itens = []                  # Ignora a primeira linha que contém Y e W
    for linha in linhas[1:-1]:  # Ignora a última linha que contém o vetor X
        valor, peso = map(int, linha.split())  # Troquei a ordem para "valor, peso"
        itens.append({'valor': valor, 'peso': peso})

   
    capacidade = w     # O beneficio sera igual ao do arquivo large_scale_optium     
    vetor_solucao_otima = list(map(int, linhas[-1].split()))

    return itens, capacidade, vetor_solucao_otima ,y 
    




def sepera_lotes(root):
    arquivos = os.listdir(root)
    tam_parte = len(arquivos) // 3
    knaPI_1 = arquivos[:tam_parte]
    knaPI_2 = arquivos[tam_parte:2*tam_parte]
    knaPI_3 = arquivos[2*tam_parte:]
    return knaPI_1,knaPI_2,knaPI_3

def calcular_beneficio(itens,solucao):
    beneficio = 0
    for i in range(len(itens)):
        beneficio += itens[i]['valor']* solucao[i]
    return beneficio

def metrica_qualidade(beneficio,beneficio_esperado):
   ## Dp x *
   ## Gulos x 
    print("bene",beneficio)
    print("bene_espe",beneficio_esperado)
    q = beneficio/ beneficio_esperado
    return q


### eixo x tempo de execução/ qualidade da solução
### eixo y tamanho da entrada
### Gráfico curva tempo de execução 
def grafico_curvas(lista_tempo, lista_y, title):
    

    safe_title = ''.join(c for c in title if c.isalnum() or c in (' ', '_')).rstrip()
    arquivo_nome = 'imagens/' + safe_title + '.png'

    # Ordenar os valores de y (pegamos a lista_y[0] como base)
    y_sorted_indices = np.argsort(lista_y[0])

    # Aplicar a mesma ordenação para todas as listas
    lista_y_sorted = [np.array(ys)[y_sorted_indices] for ys in lista_y]
    lista_tempo_sorted = [np.array(ts)[y_sorted_indices] for ts in lista_tempo]

    # Plotar os gráficos com os valores ordenados
    plt.figure(figsize=(10, 6))
    
    plt.plot(lista_y_sorted[0], lista_tempo_sorted[0], marker='o', linestyle='-', color='green', label='dp')
    plt.plot(lista_y_sorted[0], lista_tempo_sorted[1], marker='o', linestyle='-', color='blue', label='gmp')
    plt.plot(lista_y_sorted[0], lista_tempo_sorted[2], marker='o', linestyle='-', color='yellow', label='cb')

    plt.title(title)
    plt.xlabel('Valor de y (ordenado)')
    plt.ylabel('Tempo de Execução (s)')
    plt.legend()
    plt.grid(True)
    
    os.makedirs(os.path.dirname(arquivo_nome),exist_ok=True)
    plt.savefig(arquivo_nome)    
    #plt.close()
    plt.show()



### Qualidade da solução
def grafico_barras(lista_q, lista_y, title):
   
    safe_title = ''.join(c for c in title if c.isalnum() or c in (' ', '_')).rstrip()
    arquivo_nome = 'imagens/' + safe_title + '.png'
    
    plt.figure(figsize=(10, 6))
    
    indices = np.arange(len(lista_y[0]))  # Cria os índices para cada valor de y
    largura = 0.2  
   
    plt.bar(indices - largura, lista_q[0], largura, label='dp', color='green')
    plt.bar(indices, lista_q[1], largura, label='gmp', color='blue')
    plt.bar(indices + largura, lista_q[2], largura, label='cb', color='yellow')
    
    
    plt.xlabel('Valor de y')
    plt.ylabel('Qualidade da Solução (q)')
    plt.title(title)
    plt.xticks(indices, lista_y[0])  
    plt.legend()
    plt.grid(True)
    
    os.makedirs(os.path.dirname(arquivo_nome),exist_ok=True)
    plt.savefig(arquivo_nome)  
    #plt.close()
    plt.show()
