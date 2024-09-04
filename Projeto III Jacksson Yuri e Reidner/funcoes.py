import os 


def ler_instancia(caminho_arquivo):
    ### A primeira linha de cada arquivo possui dois inteiros:
    ### Y = Quantidade de itens 
    ### W = capacidade da mochila 
    
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    y , w = map(int,linhas[0].split())
    print("y",y,"w",w)
    itens = []                  # Ignora a primeira linha que contém Y e W
    for linha in linhas[1:-1]:  # Ignora a última linha que contém o vetor X
        valor, peso = map(int, linha.split())  # Troquei a ordem para "valor, peso"
        itens.append({'valor': valor, 'peso': peso})

    capacidade = 1000  # Verifique se a capacidade é sempre 1000 ou se deve ser lida do arquivo
    
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
   
    print(beneficio)
    print(beneficio_esperado)
    q = beneficio/ beneficio_esperado
    return q



