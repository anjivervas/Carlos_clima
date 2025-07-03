import requests
from typing import Optional
from bs4 import BeautifulSoup

from app.settings import Config

class ClimaScrap():
    """Clase del objeto scraper para scrapear el clima del día"""
    
    def __init__(self):
        self.url = Config().URL_BASE
        self.soup = self._get_soup()

    def _get_soup(self) -> Optional[BeautifulSoup]:
        """Obtiene y parsea el HTML de la página del clima."""
        try:
            response = requests.get(self.url, timeout=5)
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as e:
            print(f"[Scraper] Error al obtener la página del clima: {e}")
            return None

    def _get_card(self) -> Optional[BeautifulSoup]:
        """Busca el card con la información del clima en un objeto de BeautifulSoup"""

        card = self.soup.find(
            "div", 
            {"class": "CurrentConditions--body--r20G9"}
        )

        return card

    def get_temperature_average(self) -> Optional[str]:
        """Obtiene la temperatura promedio"""
        card = self._get_card()
        temperatura_promedio = card.find("span", {"class": "CurrentConditions--tempValue--zUBSz"})

        return temperatura_promedio.text

    def clima_del_dia(self) -> Optional[str]:
        """Obtiene la previsión del clima del día"""
        card = self._get_card()
        clima = card.find("div", {"class": "CurrentConditions--phraseValue---VS-k"})

        return clima.text

    def obtener_temperatura_en_el_dia(self) -> Optional[str]:
        """Obtiene la temperatura promedio"""
        card = self._get_card()
        temperatura_promedio = card.find("div", {"class": "CurrentConditions--tempHiLoValue--Og9IG"})

        return temperatura_promedio.text

    def obtener_temperatura_en_el_noche(self) -> Optional[str]:
        """Obtiene la temperatura promedio"""
        card = self._get_card()
        temperatura_promedio = card.find("span", {"data-testid": "TemperatureValue"})

        return temperatura_promedio.text

"""
sopa = get_soup(Config().URL_BASE)
card = get_card(sopa)
clima = clima_del_dia(card)
print(clima)
temperatura_dia = obtener_temperatura_en_el_noche(card)
"""