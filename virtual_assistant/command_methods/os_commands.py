import ctypes
import datetime
import os
import subprocess
import time

import winshell

from virtual_assistant.virtual_assistant import speak


def os_commands(query):
    if 'play music' in query or "play song" in query:
        speak("Here you go with music")
        music_dir = "C:\\Users\\User\\Music"
        songs = os.listdir(music_dir)
        print(songs)
        random = os.startfile(os.path.join(music_dir, songs[1]))

    elif 'the time' in query:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(str_time)
        speak(f"Sir, the time is {str_time}")

    elif 'open Chrome' in query:
        os.system('start chrome.exe')

    elif 'open edge' in query:
        os.system('start msedge.exe')

    elif 'open screenshot' in query:
        os.system('start SnippingTool')

    # OS actions
    elif 'lock window' in query:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()

    elif 'shutdown system' in query:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')

    elif 'empty recycle bin' in query:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Recycle Bin Recycled")

    elif "restart" in query:
        subprocess.call(["shutdown", "/r"])

    elif "hibernate" in query or "sleep" in query:
        speak("Hibernating")
        subprocess.call("shutdown / h")

    elif "log off" in query or "sign out" in query:
        speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])
