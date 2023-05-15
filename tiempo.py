import requests

def tiempo():
  ciudad=input("Dime el nombre de una ciudad:")
  parametros={"q":ciudad,
            "units":"metric",
            "APPID":""}
  respuesta=requests.get("http://api.openweathermap.org/data/2.5/weather",params=parametros)
