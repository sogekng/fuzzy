import csv
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def analise(opcao):

    with open('movies.json', 'r', encoding='utf-8') as file:
        json_data = file.read()

    DICIONARIO = json.loads(json_data)
    
    avaliacoes = [val[0] for val in DICIONARIO.values()]
    medidas_estatisticas = {
        "Média das avaliações": np.mean(avaliacoes),
        "Mediana das avaliações": np.median(avaliacoes),
        "Moda das avaliações": np.argmax(np.bincount(avaliacoes)),
        "Amplitude das avaliações": np.ptp(avaliacoes),
        "Desvio padrão das avaliações": np.std(avaliacoes),
        "Variância das avaliações": np.var(avaliacoes)
    }

    if opcao == '1':
        plt.hist(avaliacoes, bins=10)
        plt.xlabel('Avaliações')
        plt.ylabel('Frequência')
        plt.title('Distribuição das Avaliações dos Filmes')
        plt.show()
    elif opcao == '2':
        frequencia_classificacoes = [val[2] for val in DICIONARIO.values()]
        classificacoes, contagem = np.unique(frequencia_classificacoes, return_counts=True)
        plt.bar(classificacoes, contagem)
        plt.xlabel('Classificações')
        plt.ylabel('Contagem')
        plt.title('Frequência das Classificações dos Filmes')
        plt.show()
    elif opcao == '3':
        tabela_dinamica = pd.DataFrame(DICIONARIO.values(), columns=['Avaliação', 'Classificação', 'Resultado'])
        tabela_dinamica = tabela_dinamica.groupby('Resultado').count()
        print(tabela_dinamica)
    elif opcao == '4':
        # Separatrizes
        quartis = np.percentile(avaliacoes, [25, 50, 75])
        print("\nSeparatrizes:")
        print("Primeiro Quartil: " + str(quartis[0]))
        print("Mediana: " + str(quartis[1]))
        print("Terceiro Quartil: " + str(quartis[2]))
    elif opcao == '5':
        # Dispersão
        print("\nDispersão:")
        print("Mínimo: " + str(np.min(avaliacoes)))
        print("Máximo: " + str(np.max(avaliacoes)))
        print("Amplitude: " + str(np.ptp(avaliacoes)))
    elif opcao == '6':
        print("\nMedidas estatísticas:\n")
        for key, value in medidas_estatisticas.items():
            print(key + ": " + str(value))