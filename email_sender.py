__author__ = 'Андрій'
import smtplib
from email.mime.text import MIMEText

_fromaddress = 'takemybigthing@gmail.com'
_toaddress = 'cleo.hack@gmail.com'
_username = "takemybigthing"
_password = "trololopassword"


def send(message):
    msg = MIMEText(message)
    msg['Subject'] = 'Website feedback'
    msg['From'] = _fromaddress
    msg['To'] = _toaddress

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(_username, _password)
    s.sendmail(_fromaddress, _toaddress, msg.as_string())
    s.quit()