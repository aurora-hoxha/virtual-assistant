import pyjokes

from virtual_assistant.virtual_assistant import speak


def basic_commands(query, assistant_name):
    if "good morning" in query:
        speak("A warm" + query)
        speak("How are you Miss")
        speak(assistant_name)

    elif 'how are you' in query:
        speak("I am fine, Thank you")
        speak("How are you, Miss")

    elif 'fine' in query or "good" in query:
        speak("It's good to know that your fine")

    elif "who made you" in query or "who created you" in query:
        speak("I have been created by Aurora.")

    elif "who i am" in query:
        speak("If you talk then definately your human.")

    elif "why you came to world" in query:
        speak("Thanks to Aurora, further It's a secret")

    elif 'is love' in query:
        speak("It is 7th sense that destroy all other senses")

    elif "who are you" in query:
        speak("I am your virtual assistant created by Aurora")

    elif 'reason for you' in query:
        speak("I was created as a Minor project by Miss Aurora ")

        # most asked question from google Assistant
    elif "will you be my girlfriend" in query or "will you be my boyfriend" in query:
        speak("I'm not sure about, may be you should give me some time")

    elif "how are you" in query:
        speak("I'm fine, glad you me that")

    elif "i love you" in query:
        speak("It's hard to understand")

    elif 'joke' in query:
        speak(pyjokes.get_joke())

    elif "what's your name" in query or "What is your name" in query:
        speak("My friends call me {}".format(assistant_name))
        print("My friends call me", assistant_name)
