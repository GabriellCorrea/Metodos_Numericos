import sympy as sp

def secante(funcao_str, x0, x1, tol=1e-6, max_iter=100):
    x = sp.symbols('x')
    f = sp.lambdify(x, sp.sympify(funcao_str))

    iteracoes = []

    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

        iteracoes.append({
            "iteracao": i + 1,
            "x0": x0,
            "x1": x1,
            "x2": x2
        })

        if abs(x2 - x1) < tol:
            return x2, iteracoes

        x0 = x1
        x1 = x2

    return x2, iteracoes