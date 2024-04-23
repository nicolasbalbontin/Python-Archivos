import requests
import json
import datetime as dt




class Mindicador:
    def __init__(self, indicador, year):
        self.indicador = indicador
        self.year = year

    def InfoApi(self):
        url = f'https://mindicador.cl/api/{self.indicador}/{self.year}'
        response = requests.get(url,verify=False)
        data = json.loads(response.text)
        return data

dato1 = Mindicador('dolar', 2024)
tipo_cambio = dato1.InfoApi()

date=dt.datetime.now()

hour=date.hour
minute=date.minute
second=date.second
day=date.day
month=date.month
year=date.year


#print("Valor Dolar a hoy:(",str(day),"/",str(month),"/",str(year),"):",tipo_cambio['serie'][0]['valor'])

print(f'Valor Dolar a hoy:({str(day)}/{str(month)}/{str(year)}): {tipo_cambio["serie"][0]["valor"]}')