import re

class NameFinder:
    """
    Klass inimeste nimede leidmiseks tekstist regulaaravaldiste abil.
    """

    NAME_REGEX = re.compile(
        r'\b[A-ZÕÄÖÜ][a-zõäöü]+(?:[- ][A-ZÕÄÖÜ][a-zõäöü\.]+){1,3}\b'
    )

    def leia_nimed(self, tekstid: list[str]) -> list[str]:
        """
        Leiab nimed pealkirjadest.
        """
        nimed = set()
        for tekst in tekstid:
            leitud = self.NAME_REGEX.findall(tekst)
            nimed.update(leitud)
        return sorted(nimed)
