import requests

def tiempo():
  ciudad=input("Dime el nombre de una ciudad:")
  parametros={"q":ciudad,
            "units":"metric",
            "APPID":""}
