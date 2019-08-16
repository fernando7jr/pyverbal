# PyVerbal

Verb conjugator for Brazilian Portuguese

It is compatible with Python 3.6 and above

## Instalation

```batch
pip install pyverbal
```

## Usage

### Get the conjugator

```python
from pyverbal.conjugation import get_language_conjugator


conjugator = get_language_conjugator("pt-Br")
```

### Conjugate a verb

```python
from pyverbal.lang import PortugueseConjugation


people = [
    "eu",
    "tu",
    "ele",
    "nos",
    "vos",
    "eles"
]

conjugation = PortugueseConjugation.PresenteDoIndicativo
for person in people:
    conjugated_verb = conjugator.conjugate(
        "comer", 
        conjugation,
        person=person
    )
    print(f"For {person}: {verb} conjugated on {conjuugation} is {conjugated_verb}")
```

## Future

* Implement conjugation for irregular verbs and other cases
* Implement verb desconjugation
* Expand the work for English and other languages
