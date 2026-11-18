from flask import Flask, request, jsonify, render_template
import operacoes

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soma")
def soma_page():
    return render_template("soma.html")

@app.route("/api/soma", methods=["POST"])
def soma():
    dados = request.get_json()
    resultado = operacoes.calcular_soma(float(dados["valor1"]), float(dados["valor2"]))
    return jsonify({"resultado": resultado})

@app.route("/subtracao")
def subtracao_page():
    return render_template("subtracao.html")

@app.route("/api/subtracao", methods=["POST"])
def subtracao():
    dados = request.get_json()
    resultado = operacoes.calcular_subtracao(float(dados["valor1"]), float(dados["valor2"]))
    return jsonify({"resultado": resultado})

@app.route("/multiplicacao")
def multiplicacao_page():
    return render_template("multiplicacao.html")

@app.route("/api/multiplicacao", methods=["POST"])
def multiplicacao():
    dados = request.get_json()
    resultado = operacoes.calcular_multiplicao(float(dados["valor1"]), float(dados["valor2"]))
    return jsonify({"resultado": resultado})

@app.route("/divisao")
def divisao_page():
    return render_template("divisao.html")

@app.route("/api/divisao", methods=["POST"])
def divisao():
    dados = request.get_json()
    resultado = operacoes.calcular_divisao(float(dados["valor1"]), float(dados["valor2"]))
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)