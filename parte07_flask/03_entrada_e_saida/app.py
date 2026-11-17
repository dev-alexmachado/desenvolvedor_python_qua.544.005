from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/maioridade", methods = ['POST'])
def maioridade():
    nome = None
    idade = None
    if request.method == 'POST':
        nome = request.form.get('nome', '')
        idade = int(request.form.get('idade',''))
        result = f"é maior de idade" if idade >= 18 else "é menor de idade"
    return render_template("result.html",nome=nome,result=result)


if __name__ == "__main__":
    app.run(debug=True)