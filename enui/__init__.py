import os
import pickle
import random
import re

PHRASE_STRUCTURE = [
    "adjective-noun-verb",
    "noun-adjective-verb",
    "verb-adverb-noun",
    "noun-verb-noun"
]


def is_valid_phrase_structure(phrase_structure):
    """
    Returns True if the phrase structure is valid, False otherwise
    and uses regex to check if the phrase structure is valid
    """
    return re.match(r"^(adjective|noun|verb|adverb)-(adjective|noun|verb|adverb)-(adjective|noun|verb|adverb)$",
                    phrase_structure) is not None


def get_phrase_structure(index):
    """
    Returns the phrase structure based on the index provided
    If IndexError is raised, the index is invalid
    """
    return PHRASE_STRUCTURE[index - 1]


class Enui:
    """
    Enui is a python module that generates a UID on request
    much like the standard uiid4 module, but it makes use of word phrases
    instead of random characters.

    Example:
        enui = Enui("noun-noun-verb")
        print(enui.get_uid())

        # Output: "cat-dog-run"
    """

    def __init__(self, phrase_structure=None):
        self._word_dict = self._load_word_dict()
        self.phrase_structure = self._get_phrase_structure(phrase_structure)

    @staticmethod
    def _load_word_dict():
        """
        Loads the word dictionary from the pickle file.
        """
        module_dir = os.path.dirname(__file__)
        pickle_path = os.path.join(module_dir, "word_dict.pckl")
        with open(pickle_path, "rb") as pickle_file:
            word_dict = pickle.load(pickle_file)
        return word_dict

    @staticmethod
    def _get_phrase_structure(phrase_structure):
        """
        Returns the phrase structure based on the index or string provided.
        ...
        """
        if phrase_structure is None:
            phrase_structure = random.randint(1, 4)
        elif isinstance(phrase_structure, int):
            if not 1 <= phrase_structure <= 5:
                raise ValueError("Phrase structure index must be between 1 and 5")
        elif isinstance(phrase_structure, str):
            if not is_valid_phrase_structure(phrase_structure):
                raise ValueError("Phrase structure string is invalid")
        else:
            raise ValueError("Phrase structure must be an integer or a string")

        if isinstance(phrase_structure, int):
            phrase_structure = get_phrase_structure(phrase_structure)
        return phrase_structure

    def _get_word(self, word_type):
        """
        Returns a random word of the given type
        """
        return random.choice(self._word_dict[word_type])

    def get_uid(self):
        phrase_pieces = self.phrase_structure.split('-')
        uids = []

        for piece in phrase_pieces:
            uids.append(self._get_word(piece.lower()))

        return '-'.join(uids)
