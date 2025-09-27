
def ler_tabela(nome_arquivo):
    tabela = []
    # abre o arquivo de entrada para leitura e depois de ler, o retorna
    with open(nome_arquivo, "r") as f:
        for linha in f:
            valores = list(map(float, linha.split()))
            tabela.append(valores)
    return tabela


# função simplex
def simplex(tabela):
    num_linhas = len(tabela)
    num_colunas = len(tabela[0])

    while True:
    # Escolhe a coluna pivô com base no maior positivo da linha "Z"
        linha_objetivo = tabela[0][:-1] #ignorar coluna "b"
        coluna_pivo = max(range(num_colunas-1), key=lambda j: tabela[0][j])
        if tabela[0][coluna_pivo] <= 0:
            break #finalizado, solução ótima encontrada

        # Escolher a linha pivô (razâo entre "b" e o valor da coluna pivô na linha)
        razao = []
        for i in range(1, num_linhas):
            if tabela[i][coluna_pivo] > 0:
                razao.append((tabela[i][-1]/tabela[i][coluna_pivo] , i))
        if not razao:
            raise Exception("Erro! Nenhuma razão encontrada entre as linhas com a coluna pivô")
        _, linha_pivo = min(razao)

        # Normalizar a linha pivô
        pivo = tabela[linha_pivo][coluna_pivo]
        tabela[linha_pivo] = [x / pivo for x in tabela[linha_pivo]]

        # Zerar a coluna pivo nas outras linhas
        for i in range(num_linhas):
            if i != linha_pivo:
                fator = tabela[i][coluna_pivo]
                tabela[i] = [tabela[i][j] - fator * tabela[linha_pivo][j] for j in range(num_colunas)]

    return tabela


# função para retirar o resultado a partir da tabela simplex
def resposta(resultado):
    num_linhas = len(resultado)
    num_colunas = len(resultado[0])

    solucao = [0] * (num_colunas - 1) # vetor x1, x2, ..., xn

    for j in range(num_colunas -1 ): #ignora a coluna "b"
        coluna = [resultado[i][j] for i in range(num_linhas)]
        if coluna.count(1) == 1 and coluna.count(0) == num_linhas - 1:
            lin = coluna.index(1)
            solucao[j] = resultado[lin][-1]
    
    Z = resultado[0][-1]
    return solucao, Z

if __name__ == "__main__":
    tabela = ler_tabela("entrada.txt")

    print("Tabela inicial do Simplex:")
    for linha in tabela:
        print(linha)

resultado = simplex(tabela)

print("\nTabela Final:")
for linha in resultado:
    print(linha)

solucao, Z = resposta(resultado)

print("\nSolução Ótima:")
for i, val in enumerate(solucao, start=1):
    print(f"x{i} = {val}")
print(f"Z = {-Z}")
