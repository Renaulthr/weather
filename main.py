import requests
import json
import win32com.client as wincom

City = input("Enter the name of city that you wants yo know about its weather:\n")

url = f"http://api.weatherapi.com/v1/current.json?key=6f7c7617dda64198b1095355241401&q={City}"

speak = wincom.Dispatch("SAPI.SpVoice")
r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
speak.Speak(f"My friend the current weather of {City} is {w} degree")


