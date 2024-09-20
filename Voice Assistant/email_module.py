import smtplib

def send_email(to, subject, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('youremail@gmail.com', 'yourpassword')
    email_message = f"Subject: {subject}\n\n{body}"
    server.sendmail('youremail@gmail.com', to, email_message)
    server.close()
