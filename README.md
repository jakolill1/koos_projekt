# Uudisteportaali pealkirjadest nimede otsing

## Projekti kirjeldus

projekt on Pythonis kirjutatud programm, mis analüüsib Eesti
uudisteportaalide avalehti ning otsib pealkirjadest inimeste nimesid.
Programm laeb valitud portaali HTML-lehe, leiab sealt pealkirjad ning
tuvastab regulaaravaldiste abil 2–4-sõnalised inimeste nimed.
Leitud nimed salvestatakse JSON-faili eraldi iga portaali kohta.

## Nõuded

- Python 3.14
- Internetiühendus
- Järgmised Python paketid:
  - requests
  - beautifulsoup4

## Paigaldus ja käivitamine

1. Klooni või laadi alla projektikataloog.
2. Liigu projekti juurkausta.
3. Loo virtuaalkeskkond:

```bash
python -m venv venv

