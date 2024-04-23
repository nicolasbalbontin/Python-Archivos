import requests
from bs4 import BeautifulSoup

response = requests.get("http://mindicador.cl/api/dolar/2024",verify=False)
soup = BeautifulSoup(response.content, "html.parser")

tipo_cambio = soup.prettify()

print(tipo_cambio['serie'][0]['valor'])

