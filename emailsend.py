



import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()


email_address = "testemailamit3@gmail.com"
email_password = os.environ.get('EMAIL_PASSWORD')
print(email_password)
subject = "request.form.get('subject')"
body =" request.form.get('body')"

msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = email_address
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

# try:
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(email_address, email_password)
#     text = msg.as_string()
#     server.sendmail(email_address, email_address, text)
#     server.quit()
#     print('email sent')
# except:
#     print('Email failed to send')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_address, email_password)
text = msg.as_string()
server.sendmail(email_address, email_address, text)
server.quit()
print('email sent')
