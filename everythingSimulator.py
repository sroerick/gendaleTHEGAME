import time
import smtplib
import random
import gendaleHangman
import credentials

def void():
    print("You find your self hanging in the void.")
    response = input("What do you want to do?\n")
    # while True:
    if response == "dance":
        dance(response)
    elif response == "play hangman":
        gendaleHangman.play() 
    else:
        bug(response)


def dance(response):
    print("You dance your heart out like nobody is watching")
    void()


#if the thing breaks
def bug(response):
    print(response + " will be in the next release!")

    TO = ["sweeney@roerick.me"]

    SUBJECT = "new command request"

    TEXT = response

    message = """\
From: %s
To: %s
Subject: %s

%s

""" % (credentials.EMAIL, ", ".join(TO),SUBJECT, TEXT)
    server = smtplib.SMTP(credentials.SERVER)
    server.login(credentials.USERNAME, credentials.PASSWORD)
    server.sendmail(credentials.EMAIL, TO, message)
    server.quit


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


if __name__ == '__main__':
    credits()
