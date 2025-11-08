from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# "Banco de dados" - Lista
lista_tarefas = [
    "Aprender HTML",
    "Nadar",
    "Fazer a janta"
]

# Rotas
#GET - Listar, POST - Cadastrar
@app.route("/", methods=['GET', 'POST'])
def index():
    #Cadastro
    if request.method == 'POST':
        nova_tarefa = request.form['tarefa']

        #Adiciona nova tarefa
        lista_tarefas.append(nova_tarefa)

        #Recarga da pagina
        return redirect(url_for('index'))

    return render_template("index.html", tarefas = lista_tarefas)

if __name__ == '__main__':
    app.run(debug=True)
# Da "play" no codigo