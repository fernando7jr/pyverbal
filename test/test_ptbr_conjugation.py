import unittest
from pyverbal.conjugation import load_lang_data, get_language_conjugator, Conjugator
from pyverbal.lang import PortugueseConjugation as PtBrConjugation


suffixes = [
    "ar",
    "er",
    "ir"
]
people = [
    "eu",
    "tu",
    "ele",
    "nos",
    "vos",
    "eles"
]
verbs = {
    "andar": {
        PtBrConjugation.PresenteDoIndicativo: [
            "ando",
            "andas",
            "anda",
            "andamos",
            "andais",
            "andam"
        ],
        PtBrConjugation.PreteritoImperfeitoDoIndicativo: [
            "andava",
            "andavas",
            "andava",
            "andávamos",
            "andáveis",
            "andavam"
        ],
        PtBrConjugation.PreteritoPerfeitoDoIndicativo: [
            "andei",
            "andaste",
            "andou",
            "andamos",
            "andastes",
            "andaram"
        ],
        PtBrConjugation.PreteritoMaisQuePerfeitoDoIndicativo: [
            "andara",
            "andaras",
            "andara",
            "andáramos",
            "andáreis",
            "andaram",
        ],
        PtBrConjugation.FuturoDoPresente: [
            "andarei",
            "andarás",
            "andará",
            "andaremos",
            "andareis",
            "andarão",
        ],
        PtBrConjugation.FuturoDoPreterito: [
            "andaria",
            "andarias",
            "andaria",
            "andaríamos",
            "andaríeis",
            "andariam",
        ],
        PtBrConjugation.PresenteDoSubjuntivo: [
            "ande",
            "andes",
            "ande",
            "andemos",
            "andeis",
            "andem",
        ],
        PtBrConjugation.PreteritoDoSubjuntivo: [
            "andasse",
            "andasses",
            "andasse",
            "andássemos",
            "andásseis",
            "andassem",
        ],
        PtBrConjugation.FuturoDoSubjuntivo: [
            "andar",
            "andares",
            "andar",
            "andarmos",
            "andardes",
            "andarem",
        ],
        PtBrConjugation.ImperativoAfirmativo: [
            "anda",
            "ande",
            "andemos",
            "andai",
            "andem"
        ],
        PtBrConjugation.ImperativoNegativo: [
            "andes",
            "ande",
            "andemos",
            "andeis",
            "andem"
        ],
        PtBrConjugation.InfinitivoPessoal: [
            "andar",
            "andares",
            "andar",
            "andarmos",
            "andardes",
            "andarem"
        ],
        PtBrConjugation.Participio: "andado",
        PtBrConjugation.Gerundio: "andando",
    },
    "comer": {
        PtBrConjugation.PresenteDoIndicativo: [
            "como",
            "comes",
            "come",
            "comemos",
            "comeis",
            "comem"
        ],
        PtBrConjugation.PreteritoImperfeitoDoIndicativo: [
            "comia",
            "comias",
            "comia",
            "comíamos",
            "comíeis",
            "comiam",
        ],
        PtBrConjugation.PreteritoPerfeitoDoIndicativo: [
            "comi",
            "comeste",
            "comeu",
            "comemos",
            "comestes",
            "comeram",
        ],
        PtBrConjugation.PreteritoMaisQuePerfeitoDoIndicativo: [
            "comera",
            "comeras",
            "comera",
            "comêramos",
            "comêreis",
            "comeram",
        ],
        PtBrConjugation.FuturoDoPresente: [
            "comerei",
            "comerás",
            "comerá",
            "comeremos",
            "comereis",
            "comerão",
        ],
        PtBrConjugation.FuturoDoPreterito: [
            "comeria",
            "comerias",
            "comeria",
            "comeríamos",
            "comeríeis",
            "comeriam",
        ],
        PtBrConjugation.PresenteDoSubjuntivo: [
            "coma",
            "comas",
            "coma",
            "comamos",
            "comais",
            "comam",
        ],
        PtBrConjugation.PreteritoDoSubjuntivo: [
            "comesse",
            "comesses",
            "comesse",
            "comêssemos",
            "comêsseis",
            "comessem",
        ],
        PtBrConjugation.FuturoDoSubjuntivo: [
            "comer",
            "comeres",
            "comer",
            "comermos",
            "comerdes",
            "comerem",
        ],
        PtBrConjugation.ImperativoAfirmativo: [
            "come",
            "coma",
            "comamos",
            "comei",
            "comam"
        ],
        PtBrConjugation.ImperativoNegativo: [
            "comas",
            "coma",
            "comamos",
            "comais",
            "comam"
        ],
        PtBrConjugation.InfinitivoPessoal: [
            "comer",
            "comeres",
            "comer",
            "comermos",
            "comerdes",
            "comerem"
        ],
        PtBrConjugation.Participio: "comido",
        PtBrConjugation.Gerundio: "comendo",
    },
    "dirigir": {
        PtBrConjugation.PresenteDoIndicativo: [
            "dirigo",
            "diriges",
            "dirige",
            "dirigimos",
            "dirigis",
            "dirigem"
        ],
        PtBrConjugation.PreteritoImperfeitoDoIndicativo: [
            "dirigia",
            "dirigias",
            "dirigia",
            "dirigíamos",
            "dirigíeis",
            "dirigiam"
        ],
        PtBrConjugation.PreteritoPerfeitoDoIndicativo: [
            "dirigi",
            "dirigiste",
            "dirigiu",
            "dirigimos",
            "dirigistes",
            "dirigiram"
        ],
        PtBrConjugation.PreteritoMaisQuePerfeitoDoIndicativo: [
            "dirigira",
            "dirigiras",
            "dirigira",
            "dirigíramos",
            "dirigíreis",
            "dirigiram",
        ],
        PtBrConjugation.FuturoDoPresente: [
            "dirigirei",
            "dirigirás",
            "dirigirá",
            "dirigiremos",
            "dirigireis",
            "dirigirão",
        ],
        PtBrConjugation.FuturoDoPreterito: [
            "dirigiria",
            "dirigirias",
            "dirigiria",
            "dirigiríamos",
            "dirigiríeis",
            "dirigiriam",
        ],
        PtBrConjugation.PresenteDoSubjuntivo: [
            "diriga",
            "dirigas",
            "diriga",
            "dirigamos",
            "dirigais",
            "dirigam",
        ],
        PtBrConjugation.PreteritoDoSubjuntivo: [
            "dirigisse",
            "dirigisses",
            "dirigisse",
            "dirigíssemos",
            "dirigísseis",
            "dirigissem",
        ],
        PtBrConjugation.FuturoDoSubjuntivo: [
            "dirigir",
            "dirigires",
            "dirigir",
            "dirigirmos",
            "dirigirdes",
            "dirigirem",
        ],
        PtBrConjugation.ImperativoAfirmativo: [
            "dirige",
            "diriga",
            "dirigamos",
            "dirigi",
            "dirigam"
        ],
        PtBrConjugation.ImperativoNegativo: [
            "dirigas",
            "diriga",
            "dirigamos",
            "dirigais",
            "dirigam"
        ],
        PtBrConjugation.InfinitivoPessoal: [
            "dirigir",
            "dirigires",
            "dirigir",
            "dirigirmos",
            "dirigirdes",
            "dirigirem"
        ],
        PtBrConjugation.Participio: "dirigido",
        PtBrConjugation.Gerundio: "dirigindo",
    },
}


class TestPtBrConjugationMethods(unittest.TestCase):
    def __get_conjugator(self) -> Conjugator:
        return get_language_conjugator("pt-Br")

    def __run_conjugations(self, conjugator, conjugation_form, for_people=None):
        for_people = people if for_people is None else for_people
        for verb in verbs:
            conjugations = verbs[verb][conjugation_form]
            for i in range(0, len(conjugations)):
                person = for_people[i]
                expected = conjugations[i]
                result = conjugator.conjugate(
                    verb, 
                    conjugation_form,
                    person=person
                )
                yield result, expected

    def test_load_lang_data(self):
        try:
            data = load_lang_data("pt-Br")
        except:
            data = None
        self.assertIsNotNone(data)
        self.assertIsInstance(data, dict)
    
    def test_get_language_conjugator(self):
        conjugator = self.__get_conjugator()
        self.assertIsNotNone(conjugator)

    def test_conjugates_presente_indicativo(self):
        conjugator = self.__get_conjugator()
        conjugation_form = PtBrConjugation.PresenteDoIndicativo
        iterations = self.__run_conjugations(conjugator, conjugation_form)
        for result, expected in iterations:
            self.assertEqual(result, expected)
    
    def test_conjugates_preterito_imperfeito_indicativo(self):
        conjugator = self.__get_conjugator()
        conjugation_form = PtBrConjugation.PreteritoImperfeitoDoIndicativo
        iterations = self.__run_conjugations(conjugator, conjugation_form)
        for result, expected in iterations:
            self.assertEqual(result, expected)
    
    def test_conjugates_preterito_perfeito_indicativo(self):
        conjugator = self.__get_conjugator()
        conjugation_form = PtBrConjugation.PreteritoPerfeitoDoIndicativo
        iterations = self.__run_conjugations(conjugator, conjugation_form)
        for result, expected in iterations:
            self.assertEqual(result, expected)
    
    def test_conjugates_preterito_mais_que_perfeito_indicativo(self):
        conjugator = self.__get_conjugator()
        conjugation_form = PtBrConjugation.PreteritoMaisQuePerfeitoDoIndicativo
        iterations = self.__run_conjugations(conjugator, conjugation_form)
        for result, expected in iterations:
            self.assertEqual(result, expected)
    
    def test_conjugates_futuro_presente_indicativo(self):
        conjugator = self.__get_conjugator()
        conjugation_form = PtBrConjugation.FuturoDoPresente
        iterations = self.__run_conjugations(conjugator, conjugation_form)
        for result, expected in iterations:
            self.assertEqual(result, expected)

    def test_conjugates_futuro_preterito_indicativo(self):
        conjugator = self.__get_conjugator()
        conjugation_form = PtBrConjugation.FuturoDoPreterito
        iterations = self.__run_conjugations(conjugator, conjugation_form)
        for result, expected in iterations:
            self.assertEqual(result, expected)
    
    def test_conjugates_presente_subjuntivo(self):
        conjugator = self.__get_conjugator()
        conjugation_form = PtBrConjugation.PresenteDoSubjuntivo
        iterations = self.__run_conjugations(conjugator, conjugation_form)
        for result, expected in iterations:
            self.assertEqual(result, expected)
    
    def test_conjugates_preterito_subjuntivo(self):
        conjugator = self.__get_conjugator()
        conjugation_form = PtBrConjugation.PreteritoDoSubjuntivo
        iterations = self.__run_conjugations(conjugator, conjugation_form)
        for result, expected in iterations:
            self.assertEqual(result, expected)
    
    def test_conjugates_futuro_subjuntivo(self):
        conjugator = self.__get_conjugator()
        conjugation_form = PtBrConjugation.FuturoDoSubjuntivo
        iterations = self.__run_conjugations(conjugator, conjugation_form)
        for result, expected in iterations:
            self.assertEqual(result, expected)
    
    def test_conjugates_imperativo_afirmativo(self):
        conjugator = self.__get_conjugator()
        conjugation_form = PtBrConjugation.ImperativoAfirmativo
        for_people = people[1:]
        iterations = self.__run_conjugations(
            conjugator, 
            conjugation_form,
            for_people=for_people
        )
        for result, expected in iterations:
            self.assertEqual(result, expected)
    
    def test_conjugates_imperativo_negativo(self):
        conjugator = self.__get_conjugator()
        conjugation_form = PtBrConjugation.ImperativoNegativo
        for_people = people[1:]
        iterations = self.__run_conjugations(
            conjugator, 
            conjugation_form,
            for_people=for_people
        )
        for result, expected in iterations:
            self.assertEqual(result, expected)
    
    def test_conjugates_infinitivo_pessoal(self):
        conjugator = self.__get_conjugator()
        conjugation_form = PtBrConjugation.InfinitivoPessoal
        iterations = self.__run_conjugations(
            conjugator, 
            conjugation_form
        )
        for result, expected in iterations:
            self.assertEqual(result, expected)
    
    def test_conjugates_participio(self):
        conjugator = self.__get_conjugator()
        conjugation_form = PtBrConjugation.Participio
        for verb in verbs:
            expected = verbs[verb][conjugation_form]
            result = conjugator.conjugate(verb, conjugation_form)
            self.assertEqual(result, expected)
    
    def test_conjugates_gerundio(self):
        conjugator = self.__get_conjugator()
        conjugation_form = PtBrConjugation.Gerundio
        for verb in verbs:
            expected = verbs[verb][conjugation_form]
            result = conjugator.conjugate(verb, conjugation_form)
            self.assertEqual(result, expected)
        

if __name__ == '__main__':
    unittest.main()