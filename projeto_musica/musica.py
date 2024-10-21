from flask import Flask,render_template,request,redirect

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://{usuario}:{senha}@\
{servidor}:{porta}/{sid}'.format(
usuario = 'BD13082422',
senha = 'Iseeh7',
servidor = 'BD-ACD',
porta = '1521',
sid = 'xe'
)
db = SQLAlchemy(app)

@app.route('/testeBD')
def testar_conexao():
    try:
        resultado = db.session.execute(text('SELECT * FROM MUSICAS')).fetchall()
        print(resultado)
        if(resultado):
            return "Conexao bem-sucedida"
        else:
            return "conexao Falhou"
    except Exception as e:
        return f"Erro ao tentar conectar: {str(e)}"
     
lista_musicas = [
        {"nome":"Musica1", "Artista": "Artista1", "Genero": "Genero1"},
        {"nome":"Show das poderosas", "Artista": "Anitta", "Genero": "Funk"},
        {"nome":"Empreguetes", "Artista": "3 marias", "Genero": "POP"},
]
@app.route('/inicio')
def hello():
    return "<h1>Hello World</h1>"

@app.route('/musicas')
def listarMusicas():
    resultado = db.session.execute(text('SELECT * FROM MUSICAS')).fetchall()
    lista_musicas = []
    for registro in resultado:
        musica = {
            'nome':registro[0],
            'Artista':registro[1],
            'Genero':registro[2]
        }
        lista_musicas.append(musica)
    
    return render_template('listar_musica.html', 
                           titulo="Musicas preferidas dos Alunos",
                           musicas = lista_musicas)
@app.route("/cadastrar")
def cadastra_musica():
    return render_template("cadastrar_musicas.html")

@app.route("/adicionar", methods = ['POST'])
def adicionar_musica():
    nome = request.form['txtNome']
    artista = request.form['txtArtista']
    genero = request.form['txtGenero']
    novaMusica = {"nome":nome,"Artista": artista, "Genero":genero}
    lista_musicas.append(novaMusica)
    #return render_template('listar_musica.html', 
    #                       titulo="Musicas preferidas dos Alunos",
    #                       musicas = lista_musicas)
    return redirect('/musicas')

app.run(debug=True)