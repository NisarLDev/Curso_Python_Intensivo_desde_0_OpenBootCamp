import requests

def datosMeteorologicos():
  ciudad=input("Escriba el numbre del municipio que desea consultar: ")
  parametros={"q":ciudad,
            "units":"metric",
            "APPID":""}
  respuesta=requests.get("http://api.openweathermap.org/data/2.5/weather",params=parametros)
  if respuesta.status_code == 200:
    # La respuesta json se convierte en un diccionario
    datos = respuesta.json()
    # Se obtienen los valores del diccionario
    print("La temperatura actual es:",datos["main"]["temp"],"ºC")
    print("La sensación térmica es:",datos["main"]["feels_like"],"ºC")
    print("La temperatura mínima es:",datos["main"]["temp_min"],"ºC")
    print("La temperatura máxima es:",datos["main"]["temp_max"],"ºC")
    print("La presión es:",datos["main"]["pressure"],"hPa")
    print("La humedad es:",datos["main"]["humidity"],"%")
  else:
    print("De esa ciudad no tengo datos.")
    
    
if __name__ == '__main__':
    datosMeteorologicos()
