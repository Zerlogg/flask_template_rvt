from flask import Flask, render_template

app = Flask('app')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/admin_tekst')
def admin_tekst():
    return render_template("admin_tekst.html")

@app.route('/administratora_lapa')
def administatora_lapa():
    return render_template("administratora_lapa.html")

@app.route('/meklet_arstu')
def meklet_arstu():
    return render_template("meklet_arstu.html")

@app.route('/meklet_viziti')
def meklet_viziti():
    return render_template("meklet_viziti.html")

@app.route('/pieteikt_viziti')
def pieteikt_viziti():
    return render_template("pieteikt_viziti.html")

@app.route('/pievienot_arstu')
def pievienot_arstu():
    return render_template("pievienot_arstu.html")

@app.route('/pievienot_slimnicu')
def pievienot_slimnicu():
    return render_template("pievienot_slimnicu.html")

@app.route('/statistika')
def statistika():
    return render_template("statistika.html")

@app.route('/tekst')
def tekst():
    return render_template("tekst.html")


app.run(host='0.0.0.0', port=8080)