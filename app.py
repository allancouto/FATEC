from flask import Flask, render_template, request, redirect 

from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "12345678"

app.config['MYSQL_HOST'] = 'localhost' #'127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'calculadora'
app.config['MYSQL_DB'] = 'barco'
mysql = MySQL(app)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/quem-somos")
def quemsomos():
    return render_template("quem-somos.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/AV-1_Explorer")
def modelo1():
    return render_template("modelo1.html")

@app.route("/AV-2_Voyager")
def modelo2():
    return render_template("modelo2.html")

@app.route("/AV-3_Summit")
def modelo3():
    return render_template("modelo3.html")

@app.route("/AV-4")
def modelo4():
    return render_template("modelo4.html")

@app.route("/enviar",methods=['POST'])
def enviar(): 
    name= request.form.get('fnome')
    email= request.form.get('femail')
    cpf= request.form.get('CPF')
    fdescricao= request.form.get('fdescricao')
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO contatos (nome, email, cpf, duvidas) VALUES (%s, %s, %s, %s)", (name, email, cpf, fdescricao))
    mysql.connection.commit()
    cur.close()
    return redirect('/')



if __name__== "__main__":
    app.run(debug=True)
    
