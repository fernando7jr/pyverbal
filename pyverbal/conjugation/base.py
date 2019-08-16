from abc import abstractmethod, abstractproperty
from typing import List


class Conjugator:
    @abstractmethod
    def conjugate(self, verb: str, conjugation_class, **kwargs) -> str:
        """Conjugate the verb according to the conjugation_class
        Other params can passed through kwargs depending on the conjugator
        """

        pass
    
    @abstractmethod
    def get_conjugation_classes(self) -> List[str]:
        """Get all the available conjugation classes for this conjugator"""

        pass
    
    @abstractmethod
    def language(self):
        """Get this conjugator language name"""

        pass
