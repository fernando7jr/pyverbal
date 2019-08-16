from .base import Conjugator
from ..lang import PortugueseConjugation


class PortugueseBrazilConjugator(Conjugator):
    """
    Implements the base class Conjugator for the Portuguese language.
    Supports all the verbal times.

    * Presente do Indicativo
    * Preterito Imperfeito do Indicativo
    * Preterito Perfeito do Indicativo
    * Preterito Mais que Perfeito do Indicativo
    * Futuro do Presente
    * Futuro do Preterito
    * Presente do Subjuntivo
    * Preterito do Subjuntivo
    * Futuro do Subjuntivo
    * Imperativo Afirmativo
    * Imperativo Negativo
    * Infinitivo Pessoal
    * Infinitivo Impessoal
    * Participio
    * Gerundio
    """

    def __init__(self, data: dict):
        self.__conjugations = data

    @property
    def language(self):
        """Get this conjugator language name"""

        return "pt-Br"

    def __conjugate_common(self, verb: str, family: str, time: str, person: str) -> str:
        suffixes = {"ar", "er", "ir"}
        verb_ending = verb[-2:]
        suffix = "ar" if verb_ending not in suffixes else verb_ending

        try:
            _suffix = self.__conjugations[family][time][suffix][person]
        except KeyError as error:
            import sys

            print(error, file=sys.stderr)
            return None

        if suffix is not None:
            return f"{verb[:-2]}{_suffix}"

        return verb + _suffix
    
    def __conjugate_others(self, verb: str, family: str, time: str):
        suffixes = {"ar": 0, "er": 1, "ir": 2}
        verb_ending = verb[-2:]
        suffix = suffixes.get(verb_ending, None)

        try:
            _suffix = self.__conjugations[family][time][suffix or 0]
        except:
            return None
        
        if suffix is not None:
            return f"{verb[:-2]}{_suffix}"
        return verb + _suffix
    
    def conjugate(self, verb: str, conjugation: PortugueseConjugation, person=None) -> str:
        """Conjugate the verb according to the conjugation
        The param person may be necessary depending on the conjugation
        """

        family, time  = conjugation.value.split(".")
        if family == "nominal" and time != "infinitivo_pessoal":
            return self.__conjugate_others(verb, family, time)
        return self.__conjugate_common(verb, family, time, person)
    
    def get_conjugation_classes(self):
        """Get all the available conjugation classes for this conjugator"""

        return list(PortugueseConjugation)
