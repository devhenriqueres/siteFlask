from flask import Flask

app = Flask(__name__)

# Criar a primeira página do site
# route _ caminho(meusite.com/)

# função _ o que você quer exibir naquela página
@app.route("/")
def homepage():
    return "Esse é meu site"

# Colocar o site no ar
if __name__ == '__main__':
    app.run(debug=True)