import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

class ConexaoGmail:

    def enviar_email_arquivo(self, subject, from_, to, corpo_email, filename):

        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = from_
        msg["To"] = to
        password = ""  # Essa senha não é a do email é a senha do app do gmail
        msg.add_header("Content-Type", "text/html")

        msg.attach(MIMEText(corpo_email))

        with open(filename, "rb") as arquivo:
            att = MIMEBase("application", "octet-stream")
            att.set_payload(arquivo.read())
        encoders.encode_base64(att)

        att.add_header("Content-Disposition", f"attachment; filename= {filename}")

        msg.attach(att)
        s = smtplib.SMTP("smtp.gmail.com: 587")
        s.starttls()
        s.login(msg["From"], password)
        s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
        s.quit()

    def enviar_email(self, subject, from_, to, corpo_email):

        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = from_
        msg["To"] = to
        password = "" # Essa senha não é a do email, é a senha do app do gmail
        msg.add_header("Content-Type", "text/html")

        msg.attach(MIMEText(corpo_email))

        s = smtplib.SMTP("smtp.gmail.com: 587")
        s.starttls()
        s.login(msg["From"], password)
        s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
        s.quit()