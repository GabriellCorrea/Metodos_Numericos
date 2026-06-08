from falsaposicao import falsa_posicao
from secante import secante
from eliminacao_de_gauss import eliminacao_gauss

while True:
    print("\n=== MÉTODOS NUMÉRICOS ===")
    print("1 - Falsa Posição")
    print("2 - Secante")
    print("3 - Eliminação de Gauss")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        funcao = input("Digite a função (ex: x**3 - x - 2): ")
        a = float(input("Digite a: "))
        b = float(input("Digite b: "))

        raiz, iteracoes = falsa_posicao(funcao, a, b)

        print(f"\nRaiz encontrada: {raiz}")

        for it in iteracoes:
            print(it)

    elif opcao == "2":
        funcao = input("Digite a função (ex: x**3 - x - 2): ")
        x0 = float(input("Digite x0: "))
        x1 = float(input("Digite x1: "))

        raiz, iteracoes = secante(funcao, x0, x1)

        print(f"\nRaiz encontrada: {raiz}")

        for it in iteracoes:
            print(it)

    elif opcao == "3":

        n = int(input("Digite a quantidade de incógnitas: "))

        A = []
        b = []

        print("\nDigite os coeficientes da matriz:")

        for i in range(n):
            linha = list(map(float, input(f"Linha {i+1}: ").split()))
            A.append(linha)

        print("\nDigite os valores do vetor b:")

        for i in range(n):
            valor = float(input(f"b[{i+1}]: "))
            b.append(valor)

        resultado = eliminacao_gauss(A, b)

        print("\nSolução:")

        for i, valor in enumerate(resultado):
            print(f"x{i+1} = {valor}")