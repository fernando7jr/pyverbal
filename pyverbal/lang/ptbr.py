from enum import Enum


class PortugueseConjugation(Enum):
    PresenteDoIndicativo = "indicativo.presente"
    PreteritoImperfeitoDoIndicativo = "indicativo.preterito_imperfeito"
    PreteritoPerfeitoDoIndicativo = "indicativo.preterito_perfeito"
    PreteritoMaisQuePerfeitoDoIndicativo = "indicativo.preterito_mais_que_perfeito"
    FuturoDoPresente = "indicativo.futuro_presente"
    FuturoDoPreterito = "indicativo.futuro_preterito"
    PresenteDoSubjuntivo = "subjuntivo.presente"
    PreteritoDoSubjuntivo = "subjuntivo.preterito"
    FuturoDoSubjuntivo = "subjuntivo.futuro"
    ImperativoAfirmativo = "imperativo.afirmativo"
    ImperativoNegativo = "imperativo.negativo"
    InfinitivoPessoal = "nominal.infinitivo_pessoal"
    InfinitivoImpessoal = "nominal.infinitivo_impessoal"
    Participio = "nominal.participio"
    Gerundio = "nominal.gerundio"
