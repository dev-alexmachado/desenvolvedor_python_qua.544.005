# importa a biblioteca Flask
from flask import Flask


# ativa o framework
app = Flask(__name__)

# cria uma rota para o conteúdo a ser exibido no navegador
@app.route("/")
def hello_world():
    return "Olá, Mundo! 👋🌍"

# executa a aplicação
if __name__ == "__main__":
    app.run(debug=True)