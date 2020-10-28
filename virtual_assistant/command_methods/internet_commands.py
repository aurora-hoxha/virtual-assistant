import json
import webbrowser
from urllib.request import urlopen

import requests
import wolframalpha

from api.instagram_api import search_users
from virtual_assistant.virtual_assistant import takeCommand, speak


def access_internet(query):
    if "instagram" in query:
        instagram_index = query.find('instagram')
        new_query = query[instagram_index:]
        new_query = new_query.replace("instagram", "")
        search_users(new_query)

    if "wikipedia" in query:
        webbrowser.open("wikipedia.com")

    elif 'open youtube' in query:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        speak("Here you go to Google\n")
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        speak("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("stackoverflow.com")

    elif 'search' in query or 'play' in query:
        query = query.replace("search", "")
        query = query.replace("play", "")
        webbrowser.open(query)

    elif "where is" in query:
        query = query.replace("where is", "")
        location = query
        speak("User asked to Locate")
        speak(location)
        webbrowser.open("https://www.google.com/maps/place/" + location + "")

    # News
    elif 'news' in query:
        try:
            jsonObj = urlopen(
                '''http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=67d469c7e70c4603a637f906ee1c6865''')
            data = json.load(jsonObj)
            i = 1

            speak('Top business headlines in the US right now')
            print('''=============== Business============''' + '\n')

            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                speak(str(i) + '. ' + item['title'] + '\n')
                i += 1
        except Exception as e:

            print(str(e))

    elif "what is" in query or "who is" in query:
        client = wolframalpha.Client("GRJP5Y-A95X2U7LG2")
        res = client.query(query)

        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except StopIteration:
            print("No results")

    # Weather_____________________________________________________
    elif "weather" in query:
        # Google Open weather website
        api_key = "6688c1d18864bf462ae7831066734608"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        speak(" City name ")
        print("City name : ")
        city_name = takeCommand()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()

        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(" Temperature (in kelvin unit) = " + str(
                current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                current_pressure) + "\n humidity (in percentage) = " + str(
                current_humidiy) + "\n description = " + str(weather_description))

        else:
            speak(" City Not Found ")
