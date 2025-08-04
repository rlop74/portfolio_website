import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 465

sender = "drussellopez@gmail.com"
password = "wpiy ajfy tufz wjjn"
recipient = "rlopez@russellopez.com"

context = ssl.create_default_context()

message = """\
Subject: Testing email via Python
Hi Dudong!

Testing email. Bleh!

Regards,
Russel Lopez
Backend Engineer
444-44-4444
"""

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, recipient, message)