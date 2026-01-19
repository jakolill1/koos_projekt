import requests
from bs4 import BeautifulSoup
from json_output.json_writer import JsonWriter

class NewsScraper:
    def __init__(self, url):
        self.url = url
        self.writer = JsonWriter()

    def leia_pealkirjad(self):
        """
        Laeb lehe HTML ja kogub pealkirjad.
        Tagastab listi pealkirjadest.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # kontrollib, kas leht saadeti
        except requests.RequestException:
            return ["Lehte ei saanud laadida"]

        soup = BeautifulSoup(response.text, "html.parser")

        pealkirjad = []

        # Delfi pealkirjad
        if "delfi.ee" in self.url:
            for elem in soup.select("h2.headline, h3.headline, a.headline"):
                pealkirjad.append(elem.get_text(strip=True))

        # Postimees pealkirjad
        elif "postimees.ee" in self.url:
            for elem in soup.select("h3.teaser__title, h2.article-title"):
                pealkirjad.append(elem.get_text(strip=True))

        # ERR pealkirjad
        elif "err.ee" in self.url:
            for elem in soup.select("h2, h3"):
                pealkirjad.append(elem.get_text(strip=True))

        else:
            # Kui tundmatu URL, lihtsalt tagasta HTML pealkirjad
            for elem in soup.find_all(["h1","h2","h3"]):
                pealkirjad.append(elem.get_text(strip=True))

        return pealkirjad

    def salvage_json(self, filename=None):
        """
        Salvestab pealkirjad JSON-i.
        Kui faili nimi pole antud, luuakse automaatselt URL põhjal.
        """
        pealkirjad = self.leia_pealkirjad()

        if not filename:
            if "delfi.ee" in self.url:
                filename = "delfi.json"
            elif "postimees.ee" in self.url:
                filename = "postimees.json"
            elif "err.ee" in self.url:
                filename = "err.json"
            else:
                filename = "uudised.json"

        self.writer.write(filename, pealkirjad)
        return pealkirjad

    # Lühikood GUI jaoks
    def scrape(self):
        return self.salvage_json()





