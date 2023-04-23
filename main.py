from flask import Flask, render_template, request
import yfinance as yf
from datetime import datetime

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from twilio.rest import Client

import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    stock_symbol = request.form['stock_symbol']
    price_threshold = request.form['price_threshold']
    frequency = request.form['frequency']
    notification_type = request.form['notification_type']
    email_address = request.form['email']
    contact_number = request.form['country-code'] + request.form['contact-number']

    # Process the user input and retrieve stock market data
    ticker_yahoo = yf.Ticker(stock_symbol)
    data = ticker_yahoo.history()
    last_quote = data['Close'].iloc[-1]
    price = round(float(last_quote), 2)
    

    now = datetime.now()

    current_time = now.strftime("%I:%M:%S %p")
    # print(stock_symbol, last_quote)
    # Implement notification system

    # return render_template('result.html', stock_symbol=stock_symbol, price_threshold=price_threshold, frequency=frequency, notification_type=notification_type)
    return render_template('result.html', stock_symbol=stock_symbol,price = price,current_time = current_time,frequency = frequency, price_threshold = price_threshold, notification_type=notification_type, email_address=email_address, contact_number = contact_number)

@app.route('/get_price')
def get_price():
    stock_symbol = request.args.get('symbol')
    print(stock_symbol)
    ticker_yahoo = yf.Ticker(stock_symbol)
    data = ticker_yahoo.history()
    last_quote = data['Close'].iloc[-1]
    print(last_quote)
    return str(last_quote)



@app.route('/send_email', methods=['POST'])
def send_email():
    email_address = "testemailamit3@gmail.com"
    email_password = os.environ.get('EMAIL_PASSWORD')
    # print(email_password)
    subject = request.form.get('subject')
    body =request.form.get('body')

    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = email_address
    msg['Subject'] = subject

    destination_address = request.form.get('email_address')

    msg.attach(MIMEText(body, 'plain'))
    print("*"*33)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_address, email_password)
        text = msg.as_string()
        server.sendmail(email_address, destination_address, text)
        server.quit()
        print('Email sent')
        return 'Email Sent'
    except:
        print('Email failed to send')
        return 'Email failed to send'
    

@app.route('/send_message', methods=['POST'])
def send_message():
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')

    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=request.form.get('body'),
            from_='+19787170614',  # replace with your Twilio phone number
            to=request.form.get('contact_number')  # replace with the recipient's phone number
        )

        print(message.sid)
        return "message sent"
    except:
        print("message not sent")
        return "message not sent"

if __name__ == '__main__':
    app.run(debug=True)
