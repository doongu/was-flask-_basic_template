from flask import Flask, redirect, url_for, request, render_template, jsonify
import Connect_DB
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'hellllo3627@gmail.com'
app.config['MAIL_PASSWORD'] = 'rlflsdPrh12'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/to_main_page', methods=["POST"])
def send_mail():
    email = request.form['email_address']
    msg = Message('테스트', sender = 'hellllo3627@gmail.com', recipients=[email])
    msg.body = 'mail서버 테스트입니다.'
    mail.send(msg)
    Connect_DB.insert_email(email)
    return render_template("result.html")

if __name__ == '__main__':
    app.run('0.0.0.0', port=80)


