import smtplib

response = input("what do you want to do?")
print(response + "will be in the next release!")

SERVER = 'mail.gendale.net'

FROM = 'simulation@gendale.net'	

TO = ["sweeney@roerick.me"]

SUBJECT = "new command request" 

TEXT = response

message = """\
From: %s
To: %s
Subject: %s

%s

""" % (FROM, ", ".join(TO),SUBJECT, TEXT)

server = smtplib.SMTP(SERVER)
server.login('simulation@gendale.net', 'farkle621')
server.sendmail(FROM, TO, message)
server.quit
