from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)

def db_execute(query, params=()):
    with sqlite3.connect('cadastro.db') as con:
        cur = con.cursor()
        cur.execute(query, params)
        con.commit()
        return cur.fetchall()

# Cria a tabela se não existir
db_execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        sexo TEXT,
        unidade TEXT,
        graduacao TEXT,
        camiseta TEXT
    )
''')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    idade = request.form['idade']
    sexo = request.form['sexo']
    unidade = request.form['unidade']
    graduacao = request.form['graduacao']
    camiseta = request.form['camiseta']
    if nome and idade and sexo and unidade and graduacao and camiseta:
        db_execute(
            'INSERT INTO usuarios (nome, idade, sexo, unidade, graduacao, camiseta) VALUES (?, ?, ?, ?, ?, ?)',
            (nome, int(idade), sexo, unidade, graduacao, camiseta)
        )
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

