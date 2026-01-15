import requests
from bs4 import BeautifulSoup




class NewsScraper:
    """
    Klass uudisteportaali HTML-i allalaadimiseks ja pealkirjade leidmiseks.
    """

    def __init__(self, url: str):
        """
        Initsialiseerib objekti portaali URL-iga.
        """
        self.url = url

    def lae_html(self) -> str:
        """
        Laeb veebilehe HTML-i ja tagastab selle tekstina.
        """
        vastus = requests.get(self.url, timeout=10)
        vastus.raise_for_status()
        return vastus.text

    def leia_pealkirjad(self) -> list[str]:
        """
        Leiab HTML-ist kõik pealkirjad (h1–h6).
        """
        soup = BeautifulSoup(self.lae_html(), "html.parser")
        pealkirjad = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
        return [p.get_text(strip=True) for p in pealkirjad]
