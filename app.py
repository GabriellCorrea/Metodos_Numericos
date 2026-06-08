from flask import Flask, render_template, request
from falsaposicao import falsa_posicao
from secante import secante
from eliminacao_de_gauss import eliminacao_gauss

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# FALSA POSIÇÃO
# ==========================

@app.route("/falsa-posicao", methods=["GET", "POST"])
def falsa():

    resultado = None
    iteracoes = None

    if request.method == "POST":

        funcao = request.form["funcao"]
        a = float(request.form["a"])
        b = float(request.form["b"])

        raiz, iteracoes = falsa_posicao(funcao, a, b)

        resultado = raiz

    return render_template(
        "falsa_posicao.html",
        resultado=resultado,
        iteracoes=iteracoes
    )


# ==========================
# SECANTE
# ==========================

@app.route("/secante", methods=["GET", "POST"])
def sec():

    resultado = None
    iteracoes = None

    if request.method == "POST":

        funcao = request.form["funcao"]
        x0 = float(request.form["x0"])
        x1 = float(request.form["x1"])

        raiz, iteracoes = secante(funcao, x0, x1)

        resultado = raiz

    return render_template(
        "secante.html",
        resultado=resultado,
        iteracoes=iteracoes
    )


# ==========================
# GAUSS
# ==========================

@app.route("/gauss", methods=["GET", "POST"])
def gauss():

    resultado = None
    n = None

    if request.method == "POST":

        if "gerar" in request.form:

            n = int(request.form["n"])

            return render_template(
                "gauss.html",
                n=n
            )

        elif "resolver" in request.form:

            n = int(request.form["n"])

            A = []
            b = []

            for i in range(n):
                linha = []

                for j in range(n):
                    linha.append(float(request.form[f"a{i}_{j}"]))

                A.append(linha)

            for i in range(n):
                b.append(float(request.form[f"b{i}"]))

            print("MATRIZ:")
            for linha in A:
                print(linha)

            print("VETOR B:")
            print(b)

            resultado = eliminacao_gauss(A, b)

            return render_template(
                "gauss.html",
                n=n,
                resultado=resultado
            )

    return render_template("gauss.html")


if __name__ == "__main__":
    app.run(debug=True)