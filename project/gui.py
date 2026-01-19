import tkinter as tk
from tkinter import ttk
from scraper import NewsScraper
from name_finder import NameFinder
from json_output.json_writer import JsonWriter

PORTAALID = {
    "Delfi": "https://www.delfi.ee",
    "Postimees": "https://www.postimees.ee",
    "Õhtuleht": "https://www.ohtuleht.ee"
}

class NewsGUI:
    """
    Graafiline kasutajaliides portaali valimiseks ja analüüsiks.
    """

    def __init__(self):
        """
        Loob GUI akna ja komponendid.
        """
        self.aken = tk.Tk()
        self.aken.title("Uudiste nimede otsing")

        self.valik = ttk.Combobox(
            self.aken,
            values=list(PORTAALID.keys()),
            state="readonly"
        )
        self.valik.current(0)
        self.valik.pack(padx=10, pady=5)

        ttk.Button(
            self.aken,
            text="Käivita analüüs",
            command=self.kaivita
        ).pack(pady=5)

    def kaivita(self):
        """
        Käivitab portaali analüüsi ja salvestab tulemuse JSON-faili.
        """
        portaal = self.valik.get()
        url = PORTAALID[portaal]

        scraper = NewsScraper(url)
        pealkirjad = scraper.leia_pealkirjad()

        finder = NameFinder()
        nimed = finder.leia_nimed(pealkirjad)

        writer = JsonWriter()
        failinimi = f"{portaal.lower()}.json_output"
        writer.write(failinimi, nimed)

        scraper = NewsScraper("https://www.delfi.ee")
        pealkirjad = scraper.scrape_delfi()
        print(pealkirjad)  # nüüd näeb tegelikke pealkirju

    def kaivita_gui(self):
        """
        Käivitab GUI põhitsükli.
        """
        self.aken.mainloop()
