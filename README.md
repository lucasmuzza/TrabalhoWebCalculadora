# Calculadora Web (Python Flask HTML e JavaScript)

Este projeto é um exemplo didático de como usar **Python + Flask + HTML + JavaScript** para criar uma calculadora simples com páginas de **Soma** e **Subtração**.

---

## Requisitos

- Python 3 instalado
- VS Code (com extensão de Python)
- Ambiente virtual (venv)
- Flask instalado

---

## Estrutura do Projeto

```
projeto_calculadora_web/
│
├── app.py              # Rotas Flask
├── operacoes.py        # Funções matemáticas
├── requirements.txt    # Dependências
├── templates/          # Páginas HTML
│   ├── index.html
│   ├── soma.html
│   └── subtracao.html
└── static/             # Arquivos estáticos
└── script.js
```

---

## Clonando o projeto para o computador local

Instale o Git, abra um terminal na pasta onde deseja salvar o projeto e clone o repositório:

```powershell
git clone https://github.com/usuario/nome-do-repositorio.git
```

Substitua o endereço de exemplo pela URL do repositório deste projeto. Em seguida, acesse a pasta criada pelo Git:

```powershell
cd nome-do-repositorio
```

## Criando e ativando o ambiente virtual no Windows

Abra o terminal na pasta do projeto e crie o ambiente virtual:

```powershell
py -m venv .venv
```

Para ativá-lo no PowerShell, execute:

```powershell
.\.venv\Scripts\Activate.ps1
```

Se estiver usando o Prompt de Comando (cmd), execute:

```cmd
.venv\Scripts\activate.bat
```

Com o ambiente ativado, o nome `.venv` aparecerá no início da linha do terminal.

## Instalando o Flask

Com o terminal ainda na pasta do projeto e o ambiente virtual ativado, instale as dependências listadas em `requirements.txt`:

```powershell
python -m pip install -r requirements.txt
```

## Executando a aplicação

Na pasta do projeto, com o ambiente virtual ativado, execute:

```powershell
python app.py
```

Quando o servidor iniciar, abra o navegador e acesse:

```text
http://127.0.0.1:5000
```

Para encerrar a aplicação, volte ao terminal e pressione `Ctrl+C`.