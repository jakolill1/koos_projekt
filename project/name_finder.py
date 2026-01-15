import re

class NameFinder:
    """
    Klass inimeste nimede leidmiseks pealkirjadest.
    """

    REGEX = re.compile(
        r'\b[A-ZÕÄÖÜ][a-zõäöü]+(?:[- ][A-ZÕÄÖÜ][a-zõäöü\.]+){1,3}\b'
    )

    def leia_nimed(self, pealkirjad: list[str]) -> list[str]:
        """
        Leiab 2–4-osalised inimeste nimed.
        """
        nimed = set()
        for p in pealkirjad:
            nimed.update(self.REGEX.findall(p))
        return sorted(nimed)
