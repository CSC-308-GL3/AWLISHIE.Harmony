from datetime import datetime, timedelta
from employe import Employe
from intervention import Intervention


class Contrat:
    def __init__(self, reference: str, date_debut: str, date_fin: str, client):
        self.reference = reference
        self.date_debut = datetime.strptime(date_debut, '%d/%m/%Y')
        self.date_fin = datetime.strptime(date_fin, '%d/%m/%Y')
        self.client = client
        self.interventions = []

    def ajouter_intervention(self, intervention: Intervention):
        if self.date_debut <= intervention.date <= self.date_fin:
            self.interventions.append(intervention)
        else:
            raise ValueError('La date de l\'intervention est en dehors de la période du contrat.')

    def cout_total(self):
        duree_totale = sum([intervention.duree for intervention in self.interventions], timedelta(0))
        nb_heures = duree_totale.total_seconds() / 3600
        return nb_heures * self.client.tarif_horaire
