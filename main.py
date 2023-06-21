from analise import analise

def main():
    while True:
        print("\n----Menu----")
        print("\n1. Histograma das avaliações")
        print("2. Gráfico de barras das classificações")
        print("3. Tabelas dinâmicas")
        print("4. Separatrizes")
        print("5. Dispersão")
        print("6. Medidas estatísticas")
        opcao = input("\nDigite a opcao: ")
        analise(opcao)

if __name__ == "__main__":
    main()