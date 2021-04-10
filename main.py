import os
from flask import Flask, render_template, url_for, redirect,request, flash
from flask_mysqldb import MySQL
from datetime import datetime
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename

app =Flask(__name__)
#conexion DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
#mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'lucaslunaclaraso@gmail.com'
app.config['MAIL_PASSWORD'] = 'lukasluna78'
app.config['DONT_REPLY_FROM_EMAIL'] = '(Lucas, lucaslunaclaraso@gmail.com)'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_ASCII_ATTACHMENTS'] =True
mail = Mail(app)

#######################################
mysql = MySQL(app)
@app.context_processor
def fecha():
    return {'ahora': datetime.utcnow()}
#creacion de pantallas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/libreta', methods=['GET', 'POST'])
def libreta():
    if request.method == 'POST':
        email = request.form['email']
        asunto = request.form['asunto']
        archivo = request.files['archivo']
        filename = secure_filename(archivo.filename)
        archivo.save(os.path.join( filename))
        
        enviar = Message(asunto,sender='lucaslunaclaraso@gmail.com', recipients=[email], attachments=None)
        enviar.body = archivo
        mail.send(enviar)
        #flash("El mail se envío correctamente")
        return redirect(url_for('libreta'))
    return render_template('libreta.html')

@app.route('/whatsapp')
def whatsapp():
    return render_template('whatsapp.html')

@app.route('/cuota')
def cuota():
    return render_template('cuota.html')
if __name__ == '__main__':
    app.run(debug=True)