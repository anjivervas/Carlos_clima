import requests
from typing import Optional
from bs4 import BeautifulSoup

url = "https://weather.com/es-VE/tiempo/hoy/l/VEXX0008:1:VE"

def get_soup(url: str) -> Optional[BeautifulSoup]:
    """Obtiene y parsea el HTML de la página del clima."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as e:
        print(f"[Scraper] Error al obtener la página del clima: {e}")
        return None

def get_card(soup: BeautifulSoup) -> Optional[BeautifulSoup]:
    """Busca el card con la información del clima en un objeto de BeautifulSoup"""

    card = soup.find(
        "div", 
        {"class": "CurrentConditions--body--r20G9"}
    )

    return card

def get_temperature_average(card: BeautifulSoup) -> Optional[str]:
    """Obtiene la temperatura promedio"""
    temperatura_promedio = card.find("span", {"class": "CurrentConditions--tempValue--zUBSz"})

    return temperatura_promedio.text

def clima_del_dia(card: BeautifulSoup) -> Optional[str]:
    """Obtiene la previsión del clima del día"""
    clima = card.find("div", {"class": "CurrentConditions--phraseValue---VS-k"})

    return clima.text

def obtener_temperatura_en_el_dia(card: BeautifulSoup) -> Optional[str]:
    """Obtiene la temperatura promedio"""
    temperatura_promedio = card.find("div", {"class": "CurrentConditions--tempHiLoValue--Og9IG"})

    return temperatura_promedio.text

def obtener_temperatura_en_el_noche(card: BeautifulSoup) -> Optional[str]:
    """Obtiene la temperatura promedio"""
    temperatura_promedio = card.find("span", {"data-testid": "TemperatureValue"})

    return temperatura_promedio.text


sopa = get_soup(url)
card = get_card(sopa)
clima = clima_del_dia(card)
print(clima)
temperatura_dia = obtener_temperatura_en_el_noche(card)