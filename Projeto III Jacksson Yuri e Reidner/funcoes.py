import os 


def ler_instancia(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    itens = []
    for linha in linhas[:-1]:  # Ignora a última linha que contém o vetor X
        valor, peso = map(int, linha.split())  # Troquei a ordem para "valor, peso"
        itens.append({'valor': valor, 'peso': peso})

    capacidade = 1000  # Verifique se a capacidade é sempre 1000 ou se deve ser lida do arquivo
    
    vetor_solucao_otima = list(map(int, linhas[-1].split()))

    return itens, capacidade, vetor_solucao_otima
    




def sepera_lotes(root):
    arquivos = os.listdir(root)
    tam_parte = len(arquivos) // 3
    knaPI_1 = arquivos[:tam_parte]
    knaPI_2 = arquivos[tam_parte:2*tam_parte]
    knaPI_3 = arquivos[2*tam_parte:]
    return knaPI_1,knaPI_2,knaPI_3

def metrica_qualidade(saida,saida_esperada):
    saida = sum(saida)
    saida_esperada = sum(saida_esperada)
    q = saida/ saida_esperada
    return q



