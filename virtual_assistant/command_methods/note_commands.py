import datetime
import smtplib

from virtual_assistant.virtual_assistant import speak, takeCommand


def local_notes(query):
    # Read & Write Notes_________________________________________
    if "write a note" in query:
        speak("What should i write,")
        note = takeCommand()
        speak("How you want to save it?")
        file_name = takeCommand()
        file = open(file_name, 'w')
        speak("Mis, Should i include date and time")
        snfm = takeCommand()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now()
            file.write(str(strTime))
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)

    elif "show note" in query:
        speak("Which file you want to open?")
        file_name = takeCommand()
        file = open(file_name, 'r')

        print(file.read())
        speak(file.read(6))

    if 'send a mail' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            speak("Whom should i send")
            to = input()
            send_email(to, content)
            speak("Email has been sent !")
        except Exception as e:
            print(e)
            speak("I am not able to send this email")


def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('roratest2020', 'Demo2020')
    server.sendmail('roratest2020', to, content)
    server.close()
