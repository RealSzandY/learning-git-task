from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/mypage/me', methods=['GET'])
def hello():
    return render_template('me.html')

@app.route('/mypage/contact', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       return render_template("contact.html")
   elif request.method == 'POST':
       return render_template("contact.html")
