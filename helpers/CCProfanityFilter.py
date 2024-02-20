"""
CCProfanityFilter.py

Een simpel filter tegen schuttingtaal dat gebruik maakt van de python library profanityfilter in combinatie met
een lijst verboden woorden en zinnen.

Omdat het filter wel erg agressief is en ongewenste consequenties kan hebben, is er een lijst van geëxcuseerde woorden
die prioriteit hebben over het filter.

Gerelateerde files:
- Resources/forbidden_words.txt
- Resources/excused.txt
"""
from profanityfilter import ProfanityFilter


class CCProfanityFilter:

    def __init__(self):
        # Gebruik een filter uit de profanityfilter lib
        self._filter: ProfanityFilter = ProfanityFilter(languages=["nl", "en"])

        # Lees onze eigen verboden woorden uit, aangezien het begrip van het filter voor het Nederlands beperkt is.
        self._forbidden: list = CCProfanityFilter.read_words_from_file("Resources/forbidden_words.txt")

        # Lees de geëxcuseerde woorden uit, om te voorkomen dat het filter té enthousiast wordt
        self._excused: list = CCProfanityFilter.read_words_from_file("Resources/excused_words.txt")

    def forbidden(self, content: str) -> bool:
        """
        Is de content van dit bericht ongepast?
        """
        # Bevat dit bericht verboden woorden/zinnen?
        if any(word in self._forbidden for word in content):
            return True

        # Is dit woord geëxcuseerd?
        elif self.__excused(content):
            return False

        # Check het geheel nog eens tegen het filter om gesplitste scheldwoorden etc. te detecteren
        return self._filter.is_profane(content)

    def __excused(self, text: str) -> bool:
        # Zoek alle woorden die het filter aanstootgevend vindt
        profane = self.__find_profane_words(text)

        # Als alle aanstootgevende woorden geëxcuseerd zijn, wordt het bericht zelf geëxcuseerd
        # (python sets en verzamelingentheorie zijn lit)
        return set(profane).issubset(set(self._excused))

    def __find_profane_words(self, text: str):
        """
        Het filter zelf is vrij agressief en geeft niet aan welke woorden aanstootgevend zijn. Dan kunnen
        we dus ook niet checken of ze eventueel geëxcuseerd zijn. Dat is stom. Daarom deze workaround,
        die alle woorden apart bekijkt.
        """
        profane_words = []

        # Bekijk elk woord apart
        for word in text.split():
            if self._filter.is_profane(word):
                profane_words.append(word)

        return profane_words

    @staticmethod
    def read_words_from_file(fpath):
        """
        Lees de file met verboden woorden/zinnen uit
        """
        forbidden_words = []
        with open(fpath, 'r') as file:
            for line in file:
                word = line.strip()
                forbidden_words.append(word)
        return forbidden_words
