from flask import Flask, jsonify

app = Flask(__name__)

# Lista de frutas
lista_frutas = ["Maçã", "Morango", "Uva", "Abacate", "Bergamota" ]

# Links
@app.route('/')
def home():
    return 'Minha primeira API! BOM DIA! Acesse: /frutas'


@app.route('/frutas')
def get_frutas():
    return jsonify(lista_frutas)


if __name__ == '__main__':
    app.run(debug=True)