import sympy as sp

def falsa_posicao(funcao_str, a, b, tol=1e-6, max_iter=100):
    x = sp.symbols('x')
    f = sp.lambdify(x, sp.sympify(funcao_str))

    if f(a) * f(b) > 0:
        return "Intervalo inválido"

    iteracoes = []

    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        iteracoes.append({
            "iteracao": i + 1,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": f(c)
        })

        if abs(f(c)) < tol:
            return c, iteracoes

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c, iteracoes