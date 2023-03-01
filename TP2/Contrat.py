from datetime import datetime



class Contrat:
    def __init__(self, id_contrat, date_contrat, client, employe, grade):
        self.id_contrat = id_contrat
        self.date_contrat = date_contrat
        self.client = client
        self.employe = employe
        self.grade = grade
        self.interventions = []
        
    def ajouter_intervention(self, intervention):
        self.interventions.append(intervention)
        
    def cout_total(self):
        duree_totale = sum([intervention.duree() for intervention in self.interventions], datetime.min - datetime.min)
        nb_heures = duree_totale.total_seconds() / 3600
        return nb_heures * self.tarif_horaire
