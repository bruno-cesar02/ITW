from flask import Flask, render_template, request, redirect,send_from_directory

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os

UPLOAD_PASTA = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
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
        print (resultado)
        if(resultado):
            return "Conexão bem-sucedida"
        else:
            return "Conexão Falhou!"
    except Exception as e:
        return f"Erro ao tentar conectar: {str(e)}"

@app.route('/')
def listarMusicas():
    resultado = db.session.execute(text('SELECT * FROM MUSICAS')).fetchall()
    lista_musicas = []
    for registro in resultado:
        musica = {
            'nome':registro[0],
            'Artista': registro[1],
            'Genero':registro[2]
        }
        lista_musicas.append(musica)
    

    return render_template('listar_musicas.html',
                           titulo = "Músicas Preferidas dos Alunos",
                           musicas = lista_musicas)

@app.route("/cadastrar")
def cadastra_musica():
    return render_template("cadastrar_musicas.html")

@app.route("/adicionar", methods=['POST',])
def adicionar_musica():
    nome = request.form['txtNome']
    artista = request.form['txtArtista']
    genero = request.form['txtGenero']
    #novaMusica = {"nome": nome, "Artista": artista, "Genero": genero}
    #return render_template('listar_musicas.html',
    #                       titulo = "Músicas Preferidas dos Alunos",
    #                       musicas = lista_musicas)
    comando = f"INSERT INTO MUSICAS VALUES('{nome}','{artista}','{genero}')"
    db.session.execute(text(comando))
    db.session.commit()
    arquivo = request.files['arquivo']
    arquivo.save(f'{UPLOAD_PASTA}/album{nome}.jpg')
    return redirect('/')

@app.route("/editar/<string:nome>")
def editar(nome):
    comando = f"SELECT * FROM MUSICAS WHERE nome like '{nome}'"
    musicaBuscada = db.session.execute(text(comando)).fetchone()
    return render_template('editar_musicas.html',
                           musica = musicaBuscada)

@app.route("/atualizar", methods=['POST',])
def atualizar_musica():
    nome = request.form['txtNome']
    comando = f"SELECT * FROM MUSICAS WHERE nome like '{nome}'"
    musicaBuscada = db.session.execute(text(comando)).fetchone()

    artista = request.form['txtArtista']
    genero = request.form['txtGenero']

    comando = f"UPDATE MUSICAS SET artista = '{artista}',genero='{genero}' WHERE nome like '{nome}'"
    
    db.session.execute(text(comando))
    db.session.commit()
    arquivo = request.files['arquivo']
    nome_arquivo = arquivo.filename
    extensao_arquivo = nome_arquivo.split('.')[1]
    arquivo.save(f'{UPLOAD_PASTA}/album{nome}.es')
    return redirect('/')

@app.route("/excluir/<string:nome>")
def excluir(nome):
    comando = f"DELETE FROM MUSICAS WHERE nome like '{nome}'"
    db.session.execute(text(comando))
    db.session.commit()
    return redirect("/")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['txtSenha'] == 'admin':
        return redirect('/')
    else:
        return redirect('/login')
def recupera_imagem(nome):
    for nome_imagem in os.listdir(UPLOAD_PASTA):
        nomeSemExtensao = str(nome_imagem).split('.')[0]
        if nomeSemExtensao == f'album{nome}':
            return nome_imagem
        return 'defalut.png'
@app.route('/uploas/<nome_imagem>')
def imagem(nome_imagem):
    return send_from_directory('uploads',nome_imagem)
app.run(debug=True)