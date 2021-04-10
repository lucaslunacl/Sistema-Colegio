
from flask import Flask, render_template, url_for, redirect,request
from flask_mysqldb import MySQL
from datetime import datetime
from flask_mail import Mail, Message

app =Flask(__name__)
#conexion DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
#mail
mail = Mail(app)
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = 'lucaslunaclaraso@gmail.com'
MAIL_PASSWORD = 'lukasluna78'
DONT_REPLY_FROM_EMAIL = '(Lucas, lucaslunaclaraso@gmail.com)'
ADMINS = ('lucaslunaclaraso@gmail.com', )
MAIL_USE_TLS = True
#######################################
mysql = MySQL(app)
@app.context_processor
def fecha():
    return {'ahora': datetime.utcnow()}
#creacion de pantallas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/libreta')
def libreta():
    if request.method == 'POST':
        email = request.form['email']
        asunto = request.form['asunto']
        archivo = request.form['archivo']

        #enviar = Message(asunto,sender='lucaslunaclaraso@gmail.com', recipients=[email])
        message.body = archivo
        #mail.send(enviar)
        return render_template('libreta.html')

@app.route('/whatsapp')
def whatsapp():
    return render_template('whatsapp.html')

@app.route('/cuota')
def cuota():
    return render_template('cuota.html')
if __name__ == '__main__':
    app.run(debug=True)