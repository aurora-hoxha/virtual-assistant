import os
import time

from virtual_assistant import virtual_assistant
from virtual_assistant.command_methods.basic_commands import basic_commands
from virtual_assistant.command_methods.internet_commands import access_internet
from virtual_assistant.command_methods.note_commands import local_notes
from virtual_assistant.command_methods.os_commands import os_commands
from virtual_assistant.virtual_assistant import speak, takeCommand, \
    ASSISTANT_NAME, greetings, user_name


def text_or_speech():
    switcher = {
        0: 'TEXT',
        1: 'VOICE',
    }
    key = input("Enter 0 for TEXT and 1 for VOICE: ")

    if int(key) == 0:  # 0 is for Text
        virtual_assistant.ASSISTANT_STATE = 0
    return switcher.get(int(key), "nothing")


if __name__ == '__main__':
    clear = lambda: os.system('cls')
    print(text_or_speech())

    # This Function will clean any
    # command before execution of this python file
    clear()
    greetings()
    user_name()

    while True:
        query = takeCommand().lower()
        assistant_name = ASSISTANT_NAME


        access_internet(query)
        basic_commands(query, assistant_name)
        local_notes(query)
        os_commands(query)

        # Stop Listening_____________________________________________
        if "don't listen" in query or "stop listening" in query:
            speak(f"for how much time you want to stop {ASSISTANT_NAME} from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif 'stop' in query:
            speak("Thanks for giving me your time")
            exit()
