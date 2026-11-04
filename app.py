from flask import Flask, request, jsonify, render_template
import operacoes  # importa funções do arquivo separado

# Como executar:
# 1. Certifique-se de ter o Flask instalado: pip install flask
# 2. Execute este arquivo: python app.py
# python.exe -m pip install --upgrade pip

app = Flask(__name__)

# Página inicial
@app.route("/")
def index():
    return render_template("index.html")

# Página de soma
@app.route("/soma")
def soma_page():
    return render_template("soma.html")

@app.route("/api/soma", methods=["POST"])
def soma():
    dados = request.get_json()
    valor1 = float(dados["valor1"])
    valor2 = float(dados["valor2"])
    resultado = operacoes.calcular_soma(valor1, valor2)
    return jsonify({"resultado": resultado})

# Página de subtração
@app.route("/subtracao")
def subtracao_page():
    return render_template("subtracao.html")

@app.route("/api/subtracao", methods=["POST"])
def subtracao():
    dados = request.get_json()
    valor1 = float(dados["valor1"])
    valor2 = float(dados["valor2"])
    resultado = operacoes.calcular_subtracao(valor1, valor2)
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)
