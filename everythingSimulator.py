import time
import smtplib
import random

from email.mime.text import MIMEText

def void():
    print("You find your self hanging in the void.")
    response = input("What do you want to do?")
    if response == "dance":
        dance()
    else:
        bug()
def dance():
    print("You dance your heart out like nobody is watching")
    void()

#if the thing breaks
def bug():
    print(response + " will be in the next release!")

    FROM ='simulation@gendale.net'

    TO = ["sweeney@roerick.me"]

    SUBJECT = "new command request"

    TEXT = response

    message = """\
    From: %s
    To: %s
    Subject: %s

    %s

    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    server = smtplib.SMTP('mail.gendale.net')
    server.login('simulation@gendale.net', 'farkle621')
    server.sendmail(FROM, TO, message)
    server.quit
    sys.exit()
def credits():
    print("Welcome to the Everything Simulator.")
    time.sleep(3)
    print("Brought to you by Gendale Entertainment")
    time.sleep(3)
    print("Written and coded by Roerick Sweeney")
    time.sleep(2)
    print()
    time.sleep(2)
    print()
    time.sleep(2)
    void()
credits()
