function enviarRequisicao(endpoint, valor1, valor2) {
    fetch(endpoint, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ valor1: valor1, valor2: valor2 })
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById("resultado").innerText = "Resultado: " + data.resultado;
        })
        .catch(error => {
            console.error("Erro:", error);
            document.getElementById("resultado").innerText = "Erro ao calcular.";
        });
}

function calcularSoma() {
    let v1 = document.getElementById("valor1").value;
    let v2 = document.getElementById("valor2").value;
    enviarRequisicao("/api/soma", v1, v2);
}

function calcularSubtracao() {
    let v1 = document.getElementById("valor1").value;
    let v2 = document.getElementById("valor2").value;
    enviarRequisicao("/api/subtracao", v1, v2);
}

function calcularMultiplicacao() {
    let v1 = document.getElementById("valor1").value;
    let v2 = document.getElementById("valor2").value;
    enviarRequisicao("/api/multiplicacao", v1, v2);
}

function calcularDivisao() {
    let v1 = document.getElementById("valor1").value;
    let v2 = document.getElementById("valor2").value;
    enviarRequisicao("/api/divisao", v1, v2);
}