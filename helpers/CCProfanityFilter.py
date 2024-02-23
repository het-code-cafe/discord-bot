"""
CCProfanityFilter.py

Verboden woorden en zinnen worden gefilterd. Nederlandse filters zijn bagger.

Gerelateerde files:
- Resources/forbidden_words.txt
"""


class CCProfanityFilter:

    def __init__(self):
        # Lees onze eigen verboden woorden uit, aangezien het begrip van het filter voor het Nederlands beperkt is.
        self._forbidden: list = CCProfanityFilter.read_words_from_file("Resources/forbidden_words.txt")

    def forbidden(self, content: str) -> bool:
        """
        Is de content van dit bericht ongepast?
        (Alleen als het verboden woorden bevat)
        """
        # Komen er verboden woorden voor?
        for word in content.split():
            if word in self._forbidden:
                # Verboden woord gevonden
                return True

        # Bevinden zich verboden zinnen in deze content?
        for forbidden in self._forbidden:
            if forbidden in content:
                # Verboden zin gevonden
                return True

        return False

    @staticmethod
    def read_words_from_file(fpath) -> list:
        """
        Lees de file met verboden woorden/zinnen uit
        """
        forbidden_words = []
        with open(fpath, 'r') as file:
            for line in file:
                word: str = line.strip()
                forbidden_words.append(word)
        return forbidden_words
