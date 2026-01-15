import json

class JsonWriter:
    """
    Klass tulemuste salvestamiseks JSON-faili.
    """

    def kirjuta_faili(self, failinimi: str, nimed: list[str]):
        """
        Salvestab nimed JSON-faili.
        """
        with open(failinimi, "w", encoding="utf-8") as f:
            json.dump(
                {"nimed": nimed},
                f,
                ensure_ascii=False,
                indent=2
            )
