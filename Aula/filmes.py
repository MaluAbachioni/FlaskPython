from flask import Flask, jsonify

app = Flask(__name__)


lista_filmes = ["As vantagens de ser invsível", "Miss Simpatia", "Gente Grande", "Caramelo", "Fale comigo" ]

# Links
@app.route('/')
def home():
    return 'BOM DIA! Acesse: /filmes'


@app.route('/filmes')
def get_filmes():
    return jsonify(lista_filmes)


if __name__ == '__main__':
    app.run(debug=True)