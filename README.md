# Métodos Numéricos

Projeto acadêmico desenvolvido para a disciplina de Modelagem Computacional.

O sistema apresenta três métodos numéricos através de uma interface web inspirada nas Princesas da Disney:

* **Bela** — Método da Falsa Posição
* **Ariel** — Método da Secante
* **Elsa** — Eliminação de Gauss

---

## 📚 Métodos Implementados

### Método da Falsa Posição

Permite encontrar raízes de funções não lineares utilizando um intervalo inicial `[a,b]`.

O usuário informa:

* Função
* Valor de `a`
* Valor de `b`

O sistema exibe:

* Raiz encontrada
* Tabela completa de iterações

---

### Método da Secante

Calcula aproximações sucessivas para encontrar a raiz de uma função.

O usuário informa:

* Função
* Valor inicial `x0`
* Valor inicial `x1`

O sistema exibe:

* Raiz encontrada
* Histórico de iterações

---

### Eliminação de Gauss

Resolve sistemas lineares através do método de eliminação de Gauss.

O usuário pode escolher:

* Matriz 2x2
* Matriz 3x3
* Matriz 4x4
* Matriz 5x5

Após informar a matriz dos coeficientes e o vetor independente, o sistema retorna a solução do sistema.

---

# 🛠 Tecnologias Utilizadas

* Python
* Flask
* NumPy
* SymPy
* HTML5
* CSS3

---

# 📂 Estrutura do Projeto

```text
Metodos_Numericos/
│
├── app.py
├── main.py
├── falsaposicao.py
├── secante.py
├── eliminacao_de_gauss.py
│
├── templates/
│   ├── index.html
│   ├── falsa_posicao.html
│   ├── secante.html
│   └── gauss.html
│
├── static/
│   ├── style.css
│   ├── castelo.png
│   ├── bela.png
│   ├── ariel.png
│   ├── elsa.png
│   └── demais imagens
│
└── README.md
```

---

# ▶️ Como Executar o Projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/GabriellCorrea/Metodos_Numericos.git
```

## 2. Entrar na pasta

```bash
cd Metodos_Numericos
```

## 3. Criar ambiente virtual

Windows:

```bash
python -m venv .venv
```

## 4. Ativar ambiente virtual

PowerShell:

```bash
.venv\Scripts\Activate
```

---

## 5. Instalar dependências

```bash
pip install flask numpy sympy
```

---

## 6. Executar o sistema

```bash
python app.py
```

---

## 7. Acessar no navegador

```text
http://127.0.0.1:5000
```

---

# 👨‍💻 Autores

Gabriel Corrêa
Marcelle Lohane
Luã Japiassú
Mateus Sachinho

Projeto desenvolvido para fins acadêmicos na disciplina de Modelagem Computacional.
