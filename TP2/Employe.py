from datetime import datetime


class Employe:
    def __init__(self, numero: int, nom: str, qualification: 'Grade', date_embauche: str):
        self.numero = numero
        self.nom = nom
        self.qualification = qualification
        self.date_embauche = datetime.strptime(date_embauche, '%d/%m/%Y')

    def cout_horaire(self) -> float:
        anciennete = datetime.now().year - self.date_embauche.year
        cout_base = self.qualification.tarif_horaire
        cout_anciennete = 0.0
        if anciennete >= 5 and anciennete < 10:
            cout_anciennete = cout_base * 0.05
        elif anciennete >= 10 and anciennete < 15:
            cout_anciennete = cout_base * 0.10
        elif anciennete >= 15:
            cout_anciennete = cout_base * 0.15
        return cout_base + cout_anciennete

    def get_numero(self) -> int:
        return self.numero

    def get_nom(self) -> str:
        return self.nom

    def get_qualification(self) -> 'Grade':
        return self.qualification

    def get_date_embauche(self) -> str:
        return self.date_embauche.strftime('%d/%m/%Y')

    def get_anciennete(self, date: str) -> int:
        date_obj = datetime.strptime(date, '%d/%m/%Y')
        anciennete = datetime.now().year - date_obj.year
        if date_obj > self.date_embauche.replace(year=date_obj.year):
            anciennete -= 1
        return anciennete
