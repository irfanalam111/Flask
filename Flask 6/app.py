from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/",method=['GET','POST'])
def index():
    if request.method=='GET':
        name=request.args.form("name","world")
        return render_template("index.html",placeholder=name)
    elif request.method=='POST':
        return render_template("index.html")

@app.route("/secucess")
def secucess():
    name=request
