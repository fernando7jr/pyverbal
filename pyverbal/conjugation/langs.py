from os import path
from yaml import safe_load as __load_yaml
from .base import Conjugator
from .ptbr import PortugueseBrazilConjugator


def __read_file(file_name: str) -> dict:
    data = None
    with open(file_name, "r", encoding="utf-8") as f:
        data = __load_yaml(f)
    return data


__langs = {
    'pt-Br': PortugueseBrazilConjugator
}


def load_lang_data(lang: str) -> dict:
    """Load the conjugation grammar for the requested language"""
    public_dir = path.normpath( 
        path.join( 
            path.split(__file__)[0], "../data"
        ) 
    )
    return __read_file(f"{public_dir}/{lang}/conjugation.yaml")


def get_language_conjugator(lang: str) -> Conjugator:
    """Get a conjugator for the requested language if available.
    Raise KeyError if the language is not implemented"""

    if lang not in __langs:
        available = list(__langs.values)
        raise KeyError(
            f"Language not found. The available laguages are: {available}"
        )
    constructor = __langs[lang]
    data = load_lang_data(lang)
    return constructor(data)
