class Grade:
    def __init__(self, code: str, libelle: str, taux: float):
        self.code = code
        self.libelle = libelle
        self.taux = taux

    def get_code(self) -> str:
        return self.code

    def get_libelle(self) -> str:
        return self.libelle

    def taux_horaire(self) -> float:
        return self.taux
