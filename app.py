from flask import Flask, render_template

app = Flask(__name__)

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


if __name__== "__main__":
    app.run(debug=True)