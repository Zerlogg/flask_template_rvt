from flask import Flask, render_template

app = Flask('app')


@app.route('/')
def index():
    return render_template("index.html")


app.run(host='0.0.0.0', port=8080)

@app.route('/')
def admin_tekst():
    return render_template("admin_tekst.html")


app.run(host='0.0.0.0', port=8080)

@app.route('/')
def administatora_lapa():
    return render_template("administatora_lapa.html")


app.run(host='0.0.0.0', port=8080)

@app.route('/')
def meklet_arstu():
    return render_template("meklet_arstu.html")


app.run(host='0.0.0.0', port=8080)

@app.route('/')
def meklet_viziti():
    return render_template("meklet_viziti.html")


app.run(host='0.0.0.0', port=8080)

@app.route('/')
def pieteikt_viziti():
    return render_template("pieteikt_viziti.html")


app.run(host='0.0.0.0', port=8080)

@app.route('/')
def pievienot_arstu():
    return render_template("pievienot_arstu.html")


app.run(host='0.0.0.0', port=8080)

@app.route('/')
def pievienot_slimnicu():
    return render_template("pievienot_slimnicu.html")


app.run(host='0.0.0.0', port=8080)

@app.route('/')
def statistika():
    return render_template("statistika.html")


app.run(host='0.0.0.0', port=8080)

@app.route('/')
def tekst():
    return render_template("tekst.html")


app.run(host='0.0.0.0', port=8080)