import smtplib, ssl

def send_emails(message):
    host = "smtp.gmail.com"
    port = 465

    username = "g.eeman3742@gmail.com"
    password = "loaa nazc pnip cfgc"

    receiver = "g.eeman3742@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
